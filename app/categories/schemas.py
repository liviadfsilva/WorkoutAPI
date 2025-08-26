from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Category(BaseModel):
    name: Annotated[str, Field(description="Category's Name", example="Soccer", max_length=10)]