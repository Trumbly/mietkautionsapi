from datetime import date
from pydantic import Field, EmailStr
from app.api.v1.models.enums import PersonType
from app.api.v1.models.base import BaseModelWithUUID

class Person(BaseModelWithUUID):
    first_name: str = Field(..., description="Vorname")
    last_name: str = Field(..., description="Nachname")
    birth_date: date = Field(..., description="Geburtsdatum")
    address: str = Field(..., description="Adresse")
    email: EmailStr = Field(..., description="E-Mail")
    phone_number: str = Field(..., description="Telefonnummer")
    type: PersonType = Field(..., description="Personentyp") 