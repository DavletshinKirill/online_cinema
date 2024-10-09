import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.database import Base, uuid_pk


class MovieSession(Base):
    __tablename__ = "movie_session"
    id: Mapped[uuid_pk]
    date_start: Mapped[datetime]
    price: Mapped[float]
    movie: Mapped["Movie"] = relationship(back_populates="movie_session")
    movie_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("movie.id", ondelete="CASCADE"))
