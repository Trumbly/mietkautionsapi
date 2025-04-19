from decimal import Decimal
from typing import List
from uuid import UUID
from pydantic import Field
from api.v1.models.accounts.subaccount import Subaccount
from api.v1.models.base import BaseModelWithUUID
from datetime import datetime
from api.v1.models.accounts.interest_rate import InterestRate
class Account(BaseModelWithUUID):
    bank_name: str = Field(..., description="Bankname")
    iban: str = Field(..., description="IBAN")
    bic: str = Field(..., description="BIC")
    owner: str = Field(..., description="Kontoinhaber")
    current_total_balance: Decimal = Field(..., description="Aktueller Gesamtsaldo")
    subaccounts: List[Subaccount] = Field(default_factory=list, description="Unterkonten")
    interest_rates: List[InterestRate] = Field(default_factory=list, description="Zinssätze")
    created_at: datetime = Field(..., description="Erstellungsdatum")