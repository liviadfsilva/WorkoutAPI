from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated
from app.core.schemas import OutMixin

class AthleteSchema(BaseModel):
    name: Annotated[str, Field(description="Athlete's Name", example="Brunoa Muller", max_length=50)]
    ssn: Annotated[str, Field(description="Athlete's SSN", example="123456789", max_length=9)]
    age: Annotated[int, Field(description="Athlete's Age", example="24")]
    weight: Annotated[PositiveFloat, Field(description="Athlete's Weight", example="83.5")]
    height: Annotated[PositiveFloat, Field(description="Athlete's Height", example="1.75")]
    gender: Annotated[PositiveFloat, Field(description="Athlete's Gender", example="W", max_length=1)]
    
class AthleteIn(AthleteSchema):
    pass
    
class AthleteOut(AthleteSchema, OutMixin):
    pass