from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from api.v1.models.persons.person import Person as PersonSchema
from api.v1.repositories.persons import PersonRepository
from core.db import get_db

router = APIRouter(prefix="/persons", tags=["persons"])

@router.post("", response_model=PersonSchema)
async def create_person(
    person: PersonSchema,
    db: Session = Depends(get_db)
):
    repo = PersonRepository()
    return repo.create(db, person)

@router.get("", response_model=List[PersonSchema])
async def get_persons(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = PersonRepository()
    return repo.get_multi(db, skip=skip, limit=limit)

@router.get("/{person_id}", response_model=PersonSchema)
async def get_person(
    person_id: UUID,
    db: Session = Depends(get_db)
):
    repo = PersonRepository()
    person = repo.get(db, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person 