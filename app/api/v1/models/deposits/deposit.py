from datetime import date
from decimal import Decimal
from typing import Optional
from uuid import UUID
from pydantic import Field
from app.api.v1.models.base import BaseModelWithUUID

class Deposit(BaseModelWithUUID):
    amount: Decimal = Field(..., description="Kautionsbetrag")
    account_id: UUID = Field(..., description="Konto ID")
    deposit_subaccount_id: UUID = Field(..., description="Kautionskonto Unterkonto ID")
    paid_date: date = Field(..., description="Einzahlungsdatum")
    release_date: Optional[date] = Field(None, description="Freigabedatum")