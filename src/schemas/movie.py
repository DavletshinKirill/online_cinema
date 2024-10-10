import uuid

from pydantic import BaseModel, ConfigDict, PositiveInt, Field


class CreateMovie(BaseModel):
    title: str  = Field("Начало", max_length=64)
    director: str = "Кристофер Нолан"
    poster: str   = "https://www.google.com/example"
    duration_minutes: PositiveInt
    model_config = ConfigDict(from_attributes=True)

class UpdateMovie(CreateMovie):
    id: uuid.UUID

class ResponseMovie(UpdateMovie):
    pass
