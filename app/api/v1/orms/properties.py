from sqlalchemy import Column, String, Float, Boolean, Integer, Enum
from sqlalchemy.orm import relationship
from api.v1.orms.base import BaseModel
from api.v1.models.enums import PropertyType

class PropertyBase(BaseModel):
    __abstract__ = True
    
    address = Column(String, nullable=False)
    area_m2 = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

class Garage(PropertyBase):
    __tablename__ = "garages"
    
    parking_space_number = Column(String, nullable=False)
    type = Column(Enum(PropertyType), nullable=False)
    
    # Relationships
    contracts = relationship("Contract", back_populates="property")

class Apartment(PropertyBase):
    __tablename__ = "apartments"
    
    number_of_rooms = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    construction_year = Column(Integer, nullable=False)
    
    # Relationships
    contracts = relationship("Contract", back_populates="property")

class House(PropertyBase):
    __tablename__ = "houses"
    
    number_of_apartments = Column(Integer, nullable=False)
    land_area_m2 = Column(Float, nullable=False)
    construction_year = Column(Integer, nullable=False)
    
    # Relationships
    contracts = relationship("Contract", back_populates="property") 