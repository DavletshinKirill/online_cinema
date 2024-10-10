import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import hall_service
from src.schemas.hall import ResponseHall, UpdateHall, CreateHall
from src.services.hall import HallService

hall_router = APIRouter()


@hall_router.get("/hall/{id}", response_model=ResponseHall)
async def get_movie(
        hall_id: uuid.UUID,
        halls_service: Annotated[HallService, Depends(hall_service)]
):
    hall_response = await halls_service.get_hall(hall_id)
    return hall_response



@hall_router.post("/hall")
async def create_hall(
        hall_dto: CreateHall,
        halls_service: Annotated[HallService, Depends(hall_service)]
):
    entity_hall = await halls_service.create_hall(hall_dto)
    return entity_hall

@hall_router.put("/hall")
async def update_hall(
        movie_dto: UpdateHall,
        halls_service: Annotated[HallService, Depends(hall_service)]
):

    entity_hall = await halls_service.update_hall(movie_dto)
    return entity_hall

@hall_router.delete("/hall/{hall_id}")
async def delete_halls(
        hall_id: uuid.UUID,
        halls_service: Annotated[HallService, Depends(hall_service)]
):
    await halls_service.delete_hall(hall_id)
    return {
        "data": "Delete was successful"
    }

@hall_router.get("/halls/get")
async def get_halls(
        halls_service: Annotated[HallService, Depends(hall_service)],
        page: int = 1, per_page: int = 5
) -> list[ResponseHall]:
    get_list_halls = await halls_service.get_halls(page, per_page)
    return [ResponseHall.model_validate(hall) for hall in get_list_halls]