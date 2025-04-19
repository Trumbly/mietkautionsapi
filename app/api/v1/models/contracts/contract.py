from uuid import UUID
from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import Field
from api.v1.models.enums import ContractStatus
from api.v1.models.base import BaseModelWithUUID

class Contract(BaseModelWithUUID):
    property_id: UUID = Field(..., description="Mietobjekt ID")
    tenant_id: UUID = Field(..., description="Mieter ID")
    landlord_id: UUID = Field(..., description="Vermieter ID")
    deposit_id: UUID = Field(..., description="Kaution ID")
    start_date: date = Field(..., description="Vertragsbeginn")
    end_date: Optional[date] = Field(None, description="Vertragsende")
    monthly_rent: Decimal = Field(..., description="Monatlicher Mietzins")
    monthly_utilities: Decimal|None = Field(..., description="Monatliche Nebenkosten")
    status: ContractStatus = Field(..., description="Vertragsstatus") 