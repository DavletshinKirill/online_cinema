import uuid
from datetime import datetime

from pydantic import BaseModel, Field, PositiveInt, ConfigDict

from src.schemas.hall import UpdateHall
from src.schemas.movie import UpdateMovie
from src.schemas.ticket import UpdateTicket


class CreateMovieSession(BaseModel):
    date_start: datetime
    price: float
    movie: UpdateMovie
    hall: UpdateHall
    tickets: list[UpdateTicket]

    model_config = ConfigDict(from_attributes=True)

class UpdateMovieSession(CreateMovieSession):
    id: uuid.UUID

class ResponseMovieSession(CreateMovieSession):
    pass
