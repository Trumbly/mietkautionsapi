from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from core.repositories.base import BaseRepository
from core.orm.persons import Person
from api.v1.models.persons.person import Person as PersonSchema
from api.v1.models.enums import PersonType

class PersonRepository(BaseRepository[Person, PersonSchema, PersonSchema]):
    def get_by_email(self, db: Session, email: str) -> Optional[Person]:
        """Get a person by email."""
        return db.query(Person).filter(Person.email == email).first()
    
    def get_by_type(self, db: Session, person_type: PersonType, *, skip: int = 0, limit: int = 100) -> List[Person]:
        """Get persons by type (tenant or landlord)."""
        return db.query(Person).filter(Person.type == person_type).offset(skip).limit(limit).all()
    
    def get_tenants(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Person]:
        """Get all tenants."""
        return self.get_by_type(db, PersonType.TENANT, skip=skip, limit=limit)
    
    def get_landlords(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Person]:
        """Get all landlords."""
        return self.get_by_type(db, PersonType.LANDLORD, skip=skip, limit=limit) 