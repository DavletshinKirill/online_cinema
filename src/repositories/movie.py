from src.models.movie import Movie
from src.utils.repository import SQLAlchemyRepository


class MovieRepository(SQLAlchemyRepository):
    model = Movie