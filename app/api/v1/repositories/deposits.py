from typing import List, Optional
from uuid import UUID
from datetime import date
from sqlalchemy.orm import Session

from api.v1.repositories.base import BaseRepository
from api.v1.orms.deposits import Deposit
from api.v1.models.deposits.deposit import Deposit as DepositSchema

class DepositRepository(BaseRepository[Deposit, DepositSchema, DepositSchema]):
    def get_by_account(self, db: Session, account_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Deposit]:
        """Get deposits by account ID."""
        return db.query(Deposit).filter(Deposit.account_id == account_id).offset(skip).limit(limit).all()
    
    def get_by_subaccount(self, db: Session, subaccount_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Deposit]:
        """Get deposits by subaccount ID."""
        return db.query(Deposit).filter(Deposit.deposit_subaccount_id == subaccount_id).offset(skip).limit(limit).all()
    
    def get_by_paid_date_range(self, db: Session, start_date: date, end_date: date, *, skip: int = 0, limit: int = 100) -> List[Deposit]:
        """Get deposits within a paid date range."""
        return db.query(Deposit).filter(
            Deposit.paid_date >= start_date,
            Deposit.paid_date <= end_date
        ).offset(skip).limit(limit).all()
    
    def get_by_release_date_range(self, db: Session, start_date: date, end_date: date, *, skip: int = 0, limit: int = 100) -> List[Deposit]:
        """Get deposits within a release date range."""
        return db.query(Deposit).filter(
            Deposit.release_date >= start_date,
            Deposit.release_date <= end_date
        ).offset(skip).limit(limit).all()
    
    def get_unreleased_deposits(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Deposit]:
        """Get all unreleased deposits."""
        return db.query(Deposit).filter(Deposit.release_date == None).offset(skip).limit(limit).all() 