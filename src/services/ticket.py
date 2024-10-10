from src.utils.repository import AbstractRepository


class TicketService:
    def __init__(self, ticket_repo: AbstractRepository):
        self.ticket_repo: AbstractRepository = ticket_repo()