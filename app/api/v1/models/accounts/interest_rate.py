from datetime import date
from decimal import Decimal
from typing import Optional
from uuid import UUID
from pydantic import Field
from app.api.v1.models.base import BaseModelWithUUID

class InterestRate(BaseModelWithUUID):
    account_id: UUID = Field(..., description="Konto ID")
    valid_from: date = Field(..., description="Gültig von")
    valid_until: Optional[date] = Field(None, description="Gültig bis")
    interest_rate_pa: Decimal = Field(..., description="Zinssatz pro Jahr") 