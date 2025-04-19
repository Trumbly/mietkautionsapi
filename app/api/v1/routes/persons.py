from typing import List
from fastapi import APIRouter, HTTPException
from api.v1.models.persons.person import Person

router = APIRouter(prefix="/persons", tags=["persons"])

@router.post("", response_model=Person)
async def create_person(person: Person):
    # TODO: Add database integration
    return person

@router.get("", response_model=List[Person])
async def get_persons():
    # TODO: Add database integration
    return []

@router.get("/{person_id}", response_model=Person)
async def get_person(person_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Person not found") 