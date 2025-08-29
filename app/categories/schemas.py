from pydantic import UUID4, BaseModel, Field
from typing import Annotated

class CategorySchema(BaseModel):
    name: Annotated[str, Field(description="Category's Name", example="Soccer", max_length=10)]
    
class CategoryOut(CategorySchema):
    id: Annotated[UUID4, Field(description="Category Identifier")]