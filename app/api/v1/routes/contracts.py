from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from api.v1.models.contracts.contract import Contract as ContractSchema
from api.v1.repositories.contracts import ContractRepository
from core.db import get_db

router = APIRouter(prefix="/contracts", tags=["contracts"])

@router.post("", response_model=ContractSchema)
async def create_contract(
    contract: ContractSchema,
    db: Session = Depends(get_db)
):
    repo = ContractRepository()
    return repo.create(db, contract)

@router.get("", response_model=List[ContractSchema])
async def get_contracts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = ContractRepository()
    return repo.get_active_contracts(db, skip=skip, limit=limit)

@router.get("/{contract_id}", response_model=ContractSchema)
async def get_contract(
    contract_id: UUID,
    db: Session = Depends(get_db)
):
    repo = ContractRepository()
    contract = repo.get(db, contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract 