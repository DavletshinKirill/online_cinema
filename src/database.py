import uuid
from typing import Annotated


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.testing.schema import mapped_column

from src.config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)
async_session_factory = async_sessionmaker(engine)

uuid_pk = Annotated[uuid.UUID, mapped_column(primary_key=True, default=uuid.uuid4)]
