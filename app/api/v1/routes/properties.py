from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.v1.models.properties.garage import Garage as GarageSchema
from api.v1.models.properties.apartment import Apartment as ApartmentSchema
from api.v1.models.properties.house import House as HouseSchema
from api.v1.repositories.properties import GarageRepository, ApartmentRepository, HouseRepository
from core.db import get_db

router = APIRouter(prefix="/properties", tags=["properties"])

# Garage endpoints
@router.post("/garages", response_model=GarageSchema)
async def create_garage(
    garage: GarageSchema,
    db: Session = Depends(get_db)
):
    repo = GarageRepository()
    return repo.create(db, garage)

@router.get("/garages", response_model=List[GarageSchema])
async def get_garages(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = GarageRepository()
    return repo.get_active(db, skip=skip, limit=limit)

@router.get("/garages/{garage_id}", response_model=GarageSchema)
async def get_garage(
    garage_id: str,
    db: Session = Depends(get_db)
):
    repo = GarageRepository()
    garage = repo.get(db, garage_id)
    if not garage:
        raise HTTPException(status_code=404, detail="Garage not found")
    return garage

# Apartment endpoints
@router.post("/apartments", response_model=ApartmentSchema)
async def create_apartment(
    apartment: ApartmentSchema,
    db: Session = Depends(get_db)
):
    repo = ApartmentRepository()
    return repo.create(db, apartment)

@router.get("/apartments", response_model=List[ApartmentSchema])
async def get_apartments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = ApartmentRepository()
    return repo.get_active(db, skip=skip, limit=limit)

@router.get("/apartments/{apartment_id}", response_model=ApartmentSchema)
async def get_apartment(
    apartment_id: str,
    db: Session = Depends(get_db)
):
    repo = ApartmentRepository()
    apartment = repo.get(db, apartment_id)
    if not apartment:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return apartment

# House endpoints
@router.post("/houses", response_model=HouseSchema)
async def create_house(
    house: HouseSchema,
    db: Session = Depends(get_db)
):
    repo = HouseRepository()
    return repo.create(db, house)

@router.get("/houses", response_model=List[HouseSchema])
async def get_houses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = HouseRepository()
    return repo.get_active(db, skip=skip, limit=limit)

@router.get("/houses/{house_id}", response_model=HouseSchema)
async def get_house(
    house_id: str,
    db: Session = Depends(get_db)
):
    repo = HouseRepository()
    house = repo.get(db, house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return house 