from pydantic import BaseModel, Field
from typing import Annotated

class CategorySchema(BaseModel):
    name: Annotated[str, Field(description="Category's Name", example="Soccer", max_length=10)]