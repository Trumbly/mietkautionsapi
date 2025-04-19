from decimal import Decimal
from typing import Optional
from uuid import UUID
from pydantic import Field
from app.api.v1.models.base import BaseModelWithUUID
from typing import List
from datetime import datetime
from app.api.v1.models.accounts.interest_rate import InterestRate

class Subaccount(BaseModelWithUUID):
    main_account_id: UUID = Field(..., description="Hauptkonto ID")
    name: str = Field(..., description="Bezeichnung")
    current_balance: Decimal = Field(..., description="Aktueller Saldo")
    assigned_deposit_id: Optional[UUID] = Field(None, description="Zugewiesene Kaution ID") 
    interest_rates: List[InterestRate] = Field(default_factory=list, description="Zinssätze")
    created_at: datetime = Field(..., description="Erstellungsdatum")