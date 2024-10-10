import uuid

from pydantic import BaseModel, ConfigDict

from src.models.ticket import Status


class CreateTicket(BaseModel):
    movie_session_id: uuid.UUID
    status: Status
    model_config = ConfigDict(from_attributes=True)

class UpdateTicket(CreateTicket):
    id: uuid.UUID

class ResponseTicket(UpdateTicket):
    pass