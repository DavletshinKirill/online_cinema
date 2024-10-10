from src.models.ticket import Ticket
from src.utils.repository import SQLAlchemyRepository


class TicketRepository(SQLAlchemyRepository):
    model = Ticket