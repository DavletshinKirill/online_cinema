from src.repositories.hall import HallRepository
from src.repositories.movie import MovieRepository
from src.repositories.movie_session import MovieSessionRepository
from src.repositories.ticket import TicketRepository
from src.services.hall import HallService
from src.services.movie import MovieService
from src.services.movie_session import MovieSessionService
from src.services.ticket import TicketService


def movie_service():
    return MovieService(MovieRepository)

def ticket_service():
    return TicketService(TicketRepository)

def movie_session_service():
    return MovieSessionService(MovieSessionRepository)

def hall_service():
    return HallService(HallRepository)


