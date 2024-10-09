import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from src.database import Base, uuid_pk



class Movie(Base):
    __tablename__ = "movie"
    id: Mapped[uuid_pk]
    title: Mapped[str] = mapped_column(String(64), unique=True)
    director: Mapped[str] = mapped_column(String(64))
    poster: Mapped[str] = mapped_column(String(64))
    duration_minutes: Mapped[int]
