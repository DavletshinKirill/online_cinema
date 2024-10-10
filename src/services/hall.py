import uuid

from src.schemas.hall import ResponseHall, CreateHall, UpdateHall
from src.utils.repository import AbstractRepository


class HallService:
    def __init__(self, hall_repo: AbstractRepository):
        self.hall_repo: AbstractRepository = hall_repo()

    async def get_hall(self, hall_id: uuid.UUID):
        hall = await self.hall_repo.find_one(hall_id)
        return hall

    async def get_halls(self, page: int, per_page: int):
        halls: list[ResponseHall] = await self.hall_repo.find_several(page, per_page)
        return halls

    async def delete_hall(self, hall_id: uuid.UUID):
        await self.hall_repo.delete(hall_id)

    async def create_hall(self, hall: CreateHall) -> ResponseHall:
        hall_dict = hall.model_dump()
        created_hall = await self.hall_repo.insert(hall_dict)
        return ResponseHall.model_validate(created_hall)

    async def update_hall(self,hall: UpdateHall) -> ResponseHall:
        hall_dict = hall.model_dump()
        created_hall = await self.hall_repo.update(hall_dict)
        return ResponseHall.model_validate(created_hall)