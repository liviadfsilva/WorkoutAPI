from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.models import BaseModel

class Category(BaseModel):
    __tablename__ = "categories"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)