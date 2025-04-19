from typing import List, Optional
from uuid import UUID
from datetime import date
from sqlalchemy.orm import Session

from api.v1.repositories.base import BaseRepository
from api.v1.orms.accounts import Account, Subaccount, InterestRate
from api.v1.models.accounts.account import Account as AccountSchema
from api.v1.models.accounts.subaccount import Subaccount as SubaccountSchema
from api.v1.models.accounts.interest_rate import InterestRate as InterestRateSchema

class AccountRepository(BaseRepository[Account, AccountSchema, AccountSchema]):
    def get_by_iban(self, db: Session, iban: str) -> Optional[Account]:
        """Get an account by IBAN."""
        return db.query(Account).filter(Account.iban == iban).first()
    
    def get_by_owner(self, db: Session, owner: str, *, skip: int = 0, limit: int = 100) -> List[Account]:
        """Get accounts by owner."""
        return db.query(Account).filter(Account.owner == owner).offset(skip).limit(limit).all()

class SubaccountRepository(BaseRepository[Subaccount, SubaccountSchema, SubaccountSchema]):
    def get_by_main_account(self, db: Session, main_account_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Subaccount]:
        """Get subaccounts by main account ID."""
        return db.query(Subaccount).filter(Subaccount.main_account_id == main_account_id).offset(skip).limit(limit).all()
    
    def get_by_name(self, db: Session, name: str, main_account_id: UUID) -> Optional[Subaccount]:
        """Get a subaccount by name and main account ID."""
        return db.query(Subaccount).filter(
            Subaccount.name == name,
            Subaccount.main_account_id == main_account_id
        ).first()
    
    def get_unassigned_subaccounts(self, db: Session, main_account_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Subaccount]:
        """Get unassigned subaccounts for a main account."""
        return db.query(Subaccount).filter(
            Subaccount.main_account_id == main_account_id,
            Subaccount.assigned_deposit_id == None
        ).offset(skip).limit(limit).all()

class InterestRateRepository(BaseRepository[InterestRate, InterestRateSchema, InterestRateSchema]):
    def get_by_account(self, db: Session, account_id: UUID, *, skip: int = 0, limit: int = 100) -> List[InterestRate]:
        """Get interest rates by account ID."""
        return db.query(InterestRate).filter(InterestRate.account_id == account_id).offset(skip).limit(limit).all()
    
    def get_current_rate(self, db: Session, account_id: UUID) -> Optional[InterestRate]:
        """Get the current interest rate for an account."""
        return db.query(InterestRate).filter(
            InterestRate.account_id == account_id,
            InterestRate.valid_from <= date.today(),
            (InterestRate.valid_until >= date.today()) | (InterestRate.valid_until == None)
        ).first()
    
    def get_by_date_range(self, db: Session, account_id: UUID, start_date: date, end_date: date, *, skip: int = 0, limit: int = 100) -> List[InterestRate]:
        """Get interest rates within a date range for an account."""
        return db.query(InterestRate).filter(
            InterestRate.account_id == account_id,
            InterestRate.valid_from <= end_date,
            (InterestRate.valid_until >= start_date) | (InterestRate.valid_until == None)
        ).offset(skip).limit(limit).all() 