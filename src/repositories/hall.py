from src.models.hall import Hall
from src.utils.repository import SQLAlchemyRepository


class HallRepository(SQLAlchemyRepository):
    model = Hall