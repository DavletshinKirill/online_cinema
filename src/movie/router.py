import uuid

from fastapi import APIRouter

from src.movie.schema import CreateMovie, ResponseMovie, UpdateMovie
from src.movie.crud import MovieORM
movie_router = APIRouter()


@movie_router.get("/movie/{id}", response_model=ResponseMovie)
async def get_movie(movie_id: uuid.UUID):
    get_storage_movie = await MovieORM.get_movie_by_id(movie_id)
    result_movie = ResponseMovie.model_validate(get_storage_movie)
    return result_movie


@movie_router.post("/movie")
async def create_movie(movie_dto: CreateMovie):

    entity_movie = await MovieORM.insert_movies(movie_dto)
    return entity_movie

@movie_router.put("/movie")
async def update_movie(movie_dto: UpdateMovie):

    entity_movie = await MovieORM.update_movie(movie_dto)
    return entity_movie

@movie_router.delete("/movie/{id}", response_model=ResponseMovie)
async def delete_movie(movie_id: uuid.UUID):
    get_storage_movie = await MovieORM.delete(movie_id)
    return ResponseMovie.model_validate(get_storage_movie)

@movie_router.get("/movies/get")
async def get_movies(page: int = 0, per_page: int = 5) -> list[ResponseMovie]:
    get_list_movies = await MovieORM.get_movies(page, per_page)
    return [ResponseMovie.model_validate(movie) for movie in get_list_movies]