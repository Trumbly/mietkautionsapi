from typing import List, Optional
from uuid import UUID
from datetime import date
from sqlalchemy.orm import Session

from core.repositories.base import BaseRepository
from core.orm.contracts import Contract
from api.v1.models.contracts.contract import Contract as ContractSchema
from api.v1.models.enums import ContractStatus

class ContractRepository(BaseRepository[Contract, ContractSchema, ContractSchema]):
    def get_by_property(self, db: Session, property_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Contract]:
        """Get contracts by property ID."""
        return db.query(Contract).filter(Contract.property_id == property_id).offset(skip).limit(limit).all()
    
    def get_by_tenant(self, db: Session, tenant_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Contract]:
        """Get contracts by tenant ID."""
        return db.query(Contract).filter(Contract.tenant_id == tenant_id).offset(skip).limit(limit).all()
    
    def get_by_landlord(self, db: Session, landlord_id: UUID, *, skip: int = 0, limit: int = 100) -> List[Contract]:
        """Get contracts by landlord ID."""
        return db.query(Contract).filter(Contract.landlord_id == landlord_id).offset(skip).limit(limit).all()
    
    def get_by_status(self, db: Session, status: ContractStatus, *, skip: int = 0, limit: int = 100) -> List[Contract]:
        """Get contracts by status."""
        return db.query(Contract).filter(Contract.status == status).offset(skip).limit(limit).all()
    
    def get_active_contracts(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Contract]:
        """Get all active contracts."""
        return self.get_by_status(db, ContractStatus.ACTIVE, skip=skip, limit=limit)
    
    def get_contracts_by_date_range(self, db: Session, start_date: date, end_date: date, *, skip: int = 0, limit: int = 100) -> List[Contract]:
        """Get contracts within a date range."""
        return db.query(Contract).filter(
            Contract.start_date >= start_date,
            Contract.end_date <= end_date
        ).offset(skip).limit(limit).all() 