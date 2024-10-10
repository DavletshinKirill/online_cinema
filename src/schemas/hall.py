import uuid

from pydantic import BaseModel, ConfigDict


class CreateHall(BaseModel):
    row_seats: int
    amount_rows: int
    model_config = ConfigDict(from_attributes=True)

class UpdateHall(CreateHall):
    id: uuid.UUID

class ResponseHall(UpdateHall):
    pass