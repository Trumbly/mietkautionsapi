from api.v1.models.properties.base import PropertyBase
from pydantic import Field

class Apartment(PropertyBase):
    number_of_rooms: int = Field(..., description="Anzahl der Zimmer")
    floor: int = Field(..., description="Etage")
    construction_year: int = Field(..., description="Baujahr") 