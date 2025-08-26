from pydantic import BaseModel, Field
from typing import Annotated

class TrainingCenterSchema(BaseModel):
    name: Annotated[str, Field(description="Training Center's Name", example="St. Matthew's", max_length=20)]
    address: Annotated[str, Field(description="Training Center's Address", example="5628 Airlea Drive, Fairfax, VA", max_length=60)]
    owner: Annotated[str, Field(description="Owner's Name", example="Donald Duck", max_length=30)]