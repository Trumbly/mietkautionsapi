from typing import List
from fastapi import APIRouter, HTTPException
from api.v1.models.properties.garage import Garage
from api.v1.models.properties.apartment import Apartment
from api.v1.models.properties.house import House

router = APIRouter(prefix="/properties", tags=["properties"])

# Garage endpoints
@router.post("/garages", response_model=Garage)
async def create_garage(garage: Garage):
    # TODO: Add database integration
    return garage

@router.get("/garages", response_model=List[Garage])
async def get_garages():
    # TODO: Add database integration
    return []

@router.get("/garages/{garage_id}", response_model=Garage)
async def get_garage(garage_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Garage not found")

# Apartment endpoints
@router.post("/apartments", response_model=Apartment)
async def create_apartment(apartment: Apartment):
    # TODO: Add database integration
    return apartment

@router.get("/apartments", response_model=List[Apartment])
async def get_apartments():
    # TODO: Add database integration
    return []

@router.get("/apartments/{apartment_id}", response_model=Apartment)
async def get_apartment(apartment_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Apartment not found")

# House endpoints
@router.post("/houses", response_model=House)
async def create_house(house: House):
    # TODO: Add database integration
    return house

@router.get("/houses", response_model=List[House])
async def get_houses():
    # TODO: Add database integration
    return []

@router.get("/houses/{house_id}", response_model=House)
async def get_house(house_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="House not found") 