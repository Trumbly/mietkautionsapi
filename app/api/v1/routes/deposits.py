from typing import List
from fastapi import APIRouter, HTTPException
from api.v1.models.deposits.deposit import Deposit

router = APIRouter(prefix="/deposits", tags=["deposits"])

@router.post("", response_model=Deposit)
async def create_deposit(deposit: Deposit):
    # TODO: Add database integration
    return deposit

@router.get("", response_model=List[Deposit])
async def get_deposits():
    # TODO: Add database integration
    return []

@router.get("/{deposit_id}", response_model=Deposit)
async def get_deposit(deposit_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Deposit not found") 