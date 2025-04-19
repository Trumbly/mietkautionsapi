from app.api.v1.models.properties.base import PropertyBase
from pydantic import Field

class House(PropertyBase):
    number_of_apartments: int = Field(..., description="Anzahl der Wohnungen")
    land_area_m2: float = Field(..., description="Grundstücksfläche in Quadratmetern")
    construction_year: int = Field(..., description="Baujahr") 