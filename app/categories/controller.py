from uuid import uuid4
from pydantic import UUID4
from fastapi import APIRouter, status, Body, HTTPException
from app.core.dependencies import DatabaseDependency
from app.categories.schemas import CategorySchema, CategoryOut
from app.categories.models import Category
from sqlalchemy.future import select

router = APIRouter()

@router.post(
    "/",
    summary="Create New Category",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryOut
)
async def post(
    db_session: DatabaseDependency, 
    category_in: CategorySchema = Body(...)
) -> CategoryOut:
    
    category_out = CategoryOut(id=uuid4(), **category_in.model_dump())
    category_model = Category(**category_out.model_dump())
    
    db_session.add(category_model)
    await db_session.commit()
    
    return category_out

@router.get(
    "/",
    summary="Get All Categories",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoryOut]
)
async def query(db_session: DatabaseDependency) -> list[CategoryOut]:
    categories: list[CategoryOut] = (await db_session.execute(select(Category))).scalars().all()
    
    return categories

@router.get(
    "/{id}",
    summary="Get Category by ID",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoryOut:
    category: CategoryOut = (await db_session.execute(select(Category).filter_by(id=id))).scalars().first()
    
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Category by ID {id} not found.')
    
    return category