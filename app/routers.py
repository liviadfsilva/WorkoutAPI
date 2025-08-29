from fastapi import APIRouter
from app.athletes.controller import router as athlete
from app.categories.controller import router as category

api_router = APIRouter()
api_router.include_router(athlete, prefix="/athletes", tags=["Athletes"])
api_router.include_router(category, prefix="/categories", tags=["Categories"])