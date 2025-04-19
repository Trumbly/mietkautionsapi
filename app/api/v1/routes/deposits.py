from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from api.v1.models.deposits.deposit import Deposit as DepositSchema
from api.v1.repositories.deposits import DepositRepository
from core.db import get_db

router = APIRouter(prefix="/deposits", tags=["deposits"])

@router.post("", response_model=DepositSchema)
async def create_deposit(
    deposit: DepositSchema,
    db: Session = Depends(get_db)
):
    repo = DepositRepository()
    return repo.create(db, deposit)

@router.get("", response_model=List[DepositSchema])
async def get_deposits(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = DepositRepository()
    return repo.get_unreleased_deposits(db, skip=skip, limit=limit)

@router.get("/{deposit_id}", response_model=DepositSchema)
async def get_deposit(
    deposit_id: UUID,
    db: Session = Depends(get_db)
):
    repo = DepositRepository()
    deposit = repo.get(db, deposit_id)
    if not deposit:
        raise HTTPException(status_code=404, detail="Deposit not found")
    return deposit 