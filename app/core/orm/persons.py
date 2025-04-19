from sqlalchemy import Column, String, Date, Enum
from sqlalchemy.orm import relationship
from core.orm.base import BaseModel
from api.v1.models.enums import PersonType

class Person(BaseModel):
    __tablename__ = "persons"
    
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    type = Column(Enum(PersonType), nullable=False)
    
    # Relationships
    tenant_contracts = relationship("Contract", back_populates="tenant", foreign_keys="Contract.tenant_id")
    landlord_contracts = relationship("Contract", back_populates="landlord", foreign_keys="Contract.landlord_id") 