from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Annotated, Field

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True

class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="Identifier")]
    created_at: Annotated[datetime, Field(description="Creation Date")]