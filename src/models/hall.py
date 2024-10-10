import uuid
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base, uuid_pk
from src.models.movie_session import MovieSession


class Hall(Base):
    __tablename__ = 'hall'
    id: Mapped[uuid_pk]
    row_seats: Mapped[int]
    amount_rows: Mapped[int]
    movie_sessions: Mapped[Optional[list["MovieSession"]]] = relationship("MovieSession", back_populates="hall")
