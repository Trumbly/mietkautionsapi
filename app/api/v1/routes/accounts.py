from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from api.v1.models.accounts.account import Account as AccountSchema
from api.v1.models.accounts.subaccount import Subaccount as SubaccountSchema
from api.v1.models.accounts.interest_rate import InterestRate as InterestRateSchema
from api.v1.repositories.accounts import AccountRepository, SubaccountRepository, InterestRateRepository
from core.db import get_db

router = APIRouter(prefix="/accounts", tags=["accounts"])

# Account endpoints
@router.post("", response_model=AccountSchema)
async def create_account(
    account: AccountSchema,
    db: Session = Depends(get_db)
):
    repo = AccountRepository()
    return repo.create(db, account)

@router.get("", response_model=List[AccountSchema])
async def get_accounts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = AccountRepository()
    return repo.get_multi(db, skip=skip, limit=limit)

@router.get("/{account_id}", response_model=AccountSchema)
async def get_account(
    account_id: UUID,
    db: Session = Depends(get_db)
):
    repo = AccountRepository()
    account = repo.get(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

# Subaccount endpoints
@router.post("/subaccounts", response_model=SubaccountSchema)
async def create_subaccount(
    subaccount: SubaccountSchema,
    db: Session = Depends(get_db)
):
    repo = SubaccountRepository()
    return repo.create(db, subaccount)

@router.get("/subaccounts", response_model=List[SubaccountSchema])
async def get_subaccounts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = SubaccountRepository()
    return repo.get_multi(db, skip=skip, limit=limit)

@router.get("/subaccounts/{subaccount_id}", response_model=SubaccountSchema)
async def get_subaccount(
    subaccount_id: UUID,
    db: Session = Depends(get_db)
):
    repo = SubaccountRepository()
    subaccount = repo.get(db, subaccount_id)
    if not subaccount:
        raise HTTPException(status_code=404, detail="Subaccount not found")
    return subaccount

# Interest rate endpoints
@router.post("/interest-rates", response_model=InterestRateSchema)
async def create_interest_rate(
    interest_rate: InterestRateSchema,
    db: Session = Depends(get_db)
):
    repo = InterestRateRepository()
    return repo.create(db, interest_rate)

@router.get("/interest-rates", response_model=List[InterestRateSchema])
async def get_interest_rates(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    repo = InterestRateRepository()
    return repo.get_multi(db, skip=skip, limit=limit)

@router.get("/interest-rates/{interest_rate_id}", response_model=InterestRateSchema)
async def get_interest_rate(
    interest_rate_id: UUID,
    db: Session = Depends(get_db)
):
    repo = InterestRateRepository()
    interest_rate = repo.get(db, interest_rate_id)
    if not interest_rate:
        raise HTTPException(status_code=404, detail="Interest rate not found")
    return interest_rate 