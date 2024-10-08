from fastapi import FastAPI

from src.movie.router import movie_router

app = FastAPI()

app.include_router(
    movie_router, prefix="/api/v1/movies", tags=["movies"]
)
