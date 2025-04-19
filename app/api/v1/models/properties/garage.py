from app.api.v1.models.properties.base import PropertyBase
from app.api.v1.models.enums import PropertyType
from pydantic import Field

class Garage(PropertyBase):
    parking_space_number: str = Field(..., description="Stellplatznummer")
    type: PropertyType = Field(..., description="Garagentyp") 