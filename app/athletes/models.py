from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.models import BaseModel
from app.centers.models import TrainingCenter

class Athlete(BaseModel):
    __tablename__ = "athletes"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    ssn: Mapped[str] = mapped_column(String(9), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer(), nullable=False)
    weight: Mapped[float] = mapped_column(Float(), nullable=False)
    height: Mapped[float] = mapped_column(Float(), nullable=False)
    gender: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    category: Mapped["Category"] = relationship("Category", back_populates="athlete")
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.pk_id"))
    
    centers: Mapped["TrainingCenter"] = relationship("TrainingCenter", back_populates="athlete")
    center_id: Mapped[int] = mapped_column(ForeignKey("centers.pk_id"))