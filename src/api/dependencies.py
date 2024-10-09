from src.repositories.movie import MovieRepository
from src.services.movie import MovieService


def movie_service():
    return MovieService(MovieRepository)


