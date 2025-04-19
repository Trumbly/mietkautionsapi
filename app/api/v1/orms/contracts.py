from sqlalchemy import Column, Date, Numeric, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from api.v1.orms.base import BaseModel
from api.v1.models.enums import ContractStatus

class Contract(BaseModel):
    __tablename__ = "contracts"
    
    property_id = Column(UUID(as_uuid=True), nullable=False)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("persons.id"), nullable=False)
    landlord_id = Column(UUID(as_uuid=True), ForeignKey("persons.id"), nullable=False)
    deposit_id = Column(UUID(as_uuid=True), ForeignKey("deposits.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    monthly_rent = Column(Numeric(10, 2), nullable=False)
    monthly_utilities = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(ContractStatus), nullable=False)
    
    # Relationships
    property = relationship("PropertyBase", back_populates="contracts")
    tenant = relationship("Person", back_populates="tenant_contracts", foreign_keys=[tenant_id])
    landlord = relationship("Person", back_populates="landlord_contracts", foreign_keys=[landlord_id])
    deposit = relationship("Deposit", back_populates="contract") 