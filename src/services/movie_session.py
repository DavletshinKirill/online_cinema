from src.utils.repository import AbstractRepository


class MovieSessionService:
    def __init__(self, movie_session_repo: AbstractRepository):
        self.movie_session_repo: AbstractRepository = movie_session_repo()