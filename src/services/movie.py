import uuid
from src.schemas.movie import ResponseMovie, CreateMovie, UpdateMovie
from src.utils.repository import AbstractRepository


class MovieService:
    def __init__(self, movie_repo: AbstractRepository):
        self.movie_repo: AbstractRepository = movie_repo()

    async def get_movie(self, movie_id: uuid.UUID) -> ResponseMovie:
        movie = await self.movie_repo.find_one(movie_id)
        return ResponseMovie.model_validate(movie)

    async def create_movie(self, movie: CreateMovie) -> ResponseMovie:
        movie_dict = movie.model_dump()
        created_movie = await self.movie_repo.insert(movie_dict)
        return ResponseMovie.model_validate(created_movie)

    async def update_movie(self,movie: UpdateMovie) -> ResponseMovie:
        movie_dict = movie.model_dump()
        update_movie = await self.movie_repo.update(movie_dict)
        return ResponseMovie.model_validate(update_movie)

    async def delete_movie(self, movie_id: uuid.UUID) -> None:
        await self.movie_repo.delete(movie_id)

    async def get_movies(self, page: int, per_page: int) -> list[ResponseMovie]:
        movies: list[ResponseMovie] = await self.movie_repo.find_several(page, per_page)
        return movies


