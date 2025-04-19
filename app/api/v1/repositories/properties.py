from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from core.repositories.base import BaseRepository
from core.orm.properties import Garage, Apartment, House
from api.v1.models.properties.garage import Garage as GarageSchema
from api.v1.models.properties.apartment import Apartment as ApartmentSchema
from api.v1.models.properties.house import House as HouseSchema

class GarageRepository(BaseRepository[Garage, GarageSchema, GarageSchema]):
    def get_by_parking_space(self, db: Session, parking_space_number: str) -> Optional[Garage]:
        """Get a garage by parking space number."""
        return db.query(Garage).filter(Garage.parking_space_number == parking_space_number).first()
    
    def get_active(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Garage]:
        """Get all active garages."""
        return db.query(Garage).filter(Garage.active == True).offset(skip).limit(limit).all()

class ApartmentRepository(BaseRepository[Apartment, ApartmentSchema, ApartmentSchema]):
    def get_by_floor(self, db: Session, floor: int, *, skip: int = 0, limit: int = 100) -> List[Apartment]:
        """Get apartments by floor."""
        return db.query(Apartment).filter(Apartment.floor == floor).offset(skip).limit(limit).all()
    
    def get_active(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Apartment]:
        """Get all active apartments."""
        return db.query(Apartment).filter(Apartment.active == True).offset(skip).limit(limit).all()

class HouseRepository(BaseRepository[House, HouseSchema, HouseSchema]):
    def get_by_construction_year(self, db: Session, year: int, *, skip: int = 0, limit: int = 100) -> List[House]:
        """Get houses by construction year."""
        return db.query(House).filter(House.construction_year == year).offset(skip).limit(limit).all()
    
    def get_active(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[House]:
        """Get all active houses."""
        return db.query(House).filter(House.active == True).offset(skip).limit(limit).all() 