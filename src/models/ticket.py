import uuid
from email.policy import default
from typing import Optional

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, relationship
import enum

from sqlalchemy.testing.schema import mapped_column

from src.database import Base, uuid_pk

class Status(enum.Enum):
    free = "free"
    booked = "booked"
    bought = "bought"

class Ticket(Base):
    __tablename__ = 'ticket'
    id: Mapped[uuid_pk]
    status: Mapped[Status] = mapped_column(default=Status.free)
    movie_session_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("movie_session.id"))