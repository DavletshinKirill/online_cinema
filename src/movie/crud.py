import uuid

from sqlalchemy import select

from src.database import async_session_factory
from src.exceptions import MovieNotFoundException
from src.movie.model import Movie
from src.movie.schema import CreateMovie, UpdateMovie

class MovieORM:
    # TODO: fix type issue
    @staticmethod
    async def insert_movies(movie: CreateMovie) -> None:
        async with async_session_factory() as session:
            movie_entity = Movie(**movie.model_dump())
            session.add(movie_entity)
            await session.commit()

    @staticmethod
    async def get_movie_by_id(movie_id: uuid.UUID):
        async with async_session_factory() as session:
            movie = await session.get(Movie, movie_id)
            if movie:
                return movie
            else:
                raise MovieNotFoundException(f"Movie with ID {movie_id} not found")


    @staticmethod
    async def update_movie(updated_movie: UpdateMovie) -> Movie:
        async with async_session_factory() as session:
            current_movie = await MovieORM.get_movie_by_id(updated_movie.id)
            if current_movie:
                current_movie.title = updated_movie.title
                current_movie.poster = updated_movie.poster
                current_movie.director = updated_movie.director
                current_movie.duration_minutes = updated_movie.duration_minutes
                session.add(current_movie)
            await session.commit()
            return Movie(**updated_movie.model_dump())

    @staticmethod
    async def delete(movie_id: uuid.UUID) -> Movie:
        async with async_session_factory() as session:
            movie = await MovieORM.get_movie_by_id(movie_id)
            await session.delete(movie)
            await session.commit()
            return movie

    @staticmethod
    async def get_movies(page: int, per_page: int) -> list[Movie]:
        async with async_session_factory() as session:
            offset = (page - 1) * per_page
            select_query = select(Movie).limit(per_page).offset(offset)
            result = await session.execute(select_query)
            return result.scalars().all()
