import uuid
from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from src.api.dependencies import movie_service
from src.schemas.movie import CreateMovie, ResponseMovie, UpdateMovie
from src.services.movie import MovieService

movie_router = APIRouter()


@movie_router.get("/movie/{id}", response_model=ResponseMovie)
async def get_movie(
        movie_id: uuid.UUID,
        movies_service: Annotated[MovieService, Depends(movie_service)]
):
    movie_response = await movies_service.get_movie(movie_id)
    return movie_response



@movie_router.post("/movie")
async def create_movie(
        movie_dto: CreateMovie,
        movies_service: Annotated[MovieService, Depends(movie_service)]
):
    entity_movie = await movies_service.create_movie(movie_dto)
    return entity_movie

@movie_router.put("/movie")
async def update_movie(
        movie_dto: UpdateMovie,
        movies_service: Annotated[MovieService, Depends(movie_service)]
):

    entity_movie = await movies_service.update_movie(movie_dto)
    return entity_movie

@movie_router.delete("/movie/{movie_id}")
async def delete_movie(
        movie_id: uuid.UUID,
        movies_service: Annotated[MovieService, Depends(movie_service)]
):
    await movies_service.delete_movie(movie_id)
    return {
        "data": "Delete was successful"
    }

@movie_router.get("/movies/get")
async def get_movies(
        movies_service: Annotated[MovieService, Depends(movie_service)],
        page: int = 1, per_page: int = 5
) -> list[ResponseMovie]:
    get_list_movies = await movies_service.get_movies(page, per_page)
    return [ResponseMovie.model_validate(movie) for movie in get_list_movies]