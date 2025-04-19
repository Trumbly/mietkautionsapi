from sqlalchemy import Column, Date, Numeric, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from api.v1.orms.base import BaseModel

class Deposit(BaseModel):
    __tablename__ = "deposits"
    
    amount = Column(Numeric(10, 2), nullable=False)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    deposit_subaccount_id = Column(UUID(as_uuid=True), ForeignKey("subaccounts.id"), nullable=False)
    paid_date = Column(Date, nullable=False)
    release_date = Column(Date, nullable=True)
    released_amount = Column(Numeric(10, 2), nullable=True)
    purpose = Column(String, nullable=False)
    
    # Relationships
    account = relationship("Account", back_populates="deposits")
    subaccount = relationship("Subaccount", back_populates="deposit")
    contract = relationship("Contract", back_populates="deposit") 