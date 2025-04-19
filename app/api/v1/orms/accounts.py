from sqlalchemy import Column, String, Numeric, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from core.orm.base import BaseModel

class Account(BaseModel):
    __tablename__ = "accounts"
    
    bank_name = Column(String, nullable=False)
    iban = Column(String, nullable=False, unique=True)
    bic = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    current_total_balance = Column(Numeric(10, 2), nullable=False)
    
    # Relationships
    subaccounts = relationship("Subaccount", back_populates="main_account")
    deposits = relationship("Deposit", back_populates="account")
    interest_rates = relationship("InterestRate", back_populates="account")

class Subaccount(BaseModel):
    __tablename__ = "subaccounts"
    
    main_account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    name = Column(String, nullable=False)
    current_balance = Column(Numeric(10, 2), nullable=False)
    assigned_deposit_id = Column(UUID(as_uuid=True), ForeignKey("deposits.id"), nullable=True)
    
    # Relationships
    main_account = relationship("Account", back_populates="subaccounts")
    deposit = relationship("Deposit", back_populates="subaccount")

class InterestRate(BaseModel):
    __tablename__ = "interest_rates"
    
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    valid_from = Column(Date, nullable=False)
    valid_until = Column(Date, nullable=True)
    interest_rate_pa = Column(Numeric(5, 2), nullable=False)
    
    # Relationships
    account = relationship("Account", back_populates="interest_rates") 