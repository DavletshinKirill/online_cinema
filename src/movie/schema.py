import uuid

from pydantic import BaseModel, ConfigDict


class CreateMovie(BaseModel):
    title: str  # = Field( ..., max_length=64, examples="Начало")
    director: str  # = Field(..., max_length=64, examples="Кристофер Нолан")
    poster: str  # = Field(..., max_length=64, examples="https://www.google.com/example")
    duration_minutes: int  # = Field(..., max_length=64, examples=148)
    model_config = ConfigDict(from_attributes=True)

class UpdateMovie(CreateMovie):
    id: uuid.UUID

class ResponseMovie(UpdateMovie):
    pass
