from pydantic import Field
from app.api.v1.models.base import BaseModelWithUUID

class PropertyBase(BaseModelWithUUID):
    address: str = Field(..., description="Adresse")
    area_m2: float = Field(..., description="Fläche in Quadratmetern")
    description: str = Field(..., description="Beschreibung")
    active: bool = Field(default=True, description="Aktiv") 