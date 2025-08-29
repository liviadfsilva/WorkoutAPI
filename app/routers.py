from fastapi import APIRouter
from app.athletes.controller import router as athlete

api_router = APIRouter()
api_router.include_router(athlete, prefix="/athletes", tags=["Athletes"])