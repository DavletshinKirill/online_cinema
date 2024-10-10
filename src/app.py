from fastapi import FastAPI

from src.api.hall import hall_router
from src.api.movie import movie_router
from src.api.movie_session import movie_session_router
from src.api.ticket import ticket_router

app = FastAPI()

app.include_router(
    movie_router, prefix="/api/v1", tags=["movies"]
)

app.include_router(
    ticket_router, prefix="/api/v1", tags=["tickets"]
)

app.include_router(
    movie_session_router, prefix="/api/v1", tags=["movie_sessions"]
)

app.include_router(
    hall_router, prefix="/api/v1", tags=["halls"]
)
