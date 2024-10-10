import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.database import Base, uuid_pk


class MovieSession(Base):
    __tablename__ = "movie_session"
    id: Mapped[uuid_pk]
    date_start: Mapped[datetime]
    price: Mapped[float]
    movie: Mapped[Optional["Movie"]] = relationship("Movie", back_populates="movie_sessions")
    movie_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("movie.id"))
    hall: Mapped[Optional["Hall"]] = relationship("Hall", back_populates="movie_sessions")
    hall_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("hall.id"))
    tickets: Mapped[Optional[list["Ticket"]]] = relationship("Ticket", back_populates="movie_session")



