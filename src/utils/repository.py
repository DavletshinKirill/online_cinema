import uuid
from abc import abstractmethod, ABC
import copy

from sqlalchemy import insert, update, select, delete
from src.database import async_session_factory


class AbstractRepository(ABC):
    @abstractmethod
    async def insert(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, item_id: uuid.UUID):
        raise NotImplementedError

    @abstractmethod
    async def update(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, item_id: uuid.UUID):
        raise NotImplementedError

    @abstractmethod
    async def find_several(self, page: int, per_page: int):
        raise NotImplementedError

class SQLAlchemyRepository(AbstractRepository):
    model = None


    async def find_one(self, item_id: uuid.UUID) -> model:
        async with async_session_factory() as session:
            stmt = select(self.model).filter_by(id=item_id)
            res = await session.execute(stmt)
            res = res.scalar_one()
            return res

    async def update(self, data: dict) -> model:
        async with async_session_factory() as session:
            stmt = update(self.model).values(**data).filter_by(id=data['id']).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            updated_res = res.scalar_one()
            await session.refresh(updated_res)
            return updated_res

    async def delete(self, item_id: uuid.UUID):
        async with async_session_factory() as session:
            stmt = delete(self.model).filter_by(id=item_id).returning(self.model)
            await session.execute(stmt)
            await session.commit()

    async def find_several(self, page: int, per_page: int) -> list[model]:
        async with async_session_factory() as session:
            stmt = select(self.model).offset((page - 1) * per_page).limit(per_page)
            res = await session.execute(stmt)
            return list(res.scalars().all())

    async def insert(self, data: dict) -> model:
        async with async_session_factory() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            inserted_res = res.scalar_one()
            await session.refresh(inserted_res)
            return inserted_res