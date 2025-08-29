from app.athletes.schemas import AthleteIn
from fastapi import APIRouter, status, Body
from app.core.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', summary="Create New Athlete", status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency, atleta_in: AthleteIn = Body(...)):
    pass