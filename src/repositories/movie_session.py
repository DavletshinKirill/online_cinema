from src.models.movie_session import MovieSession
from src.utils.repository import SQLAlchemyRepository


class MovieSessionRepository(SQLAlchemyRepository):
    model = MovieSession