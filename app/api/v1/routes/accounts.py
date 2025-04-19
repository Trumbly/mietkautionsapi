from typing import List
from fastapi import APIRouter, HTTPException
from api.v1.models.accounts.account import Account
from api.v1.models.accounts.subaccount import Subaccount
from api.v1.models.accounts.interest_rate import InterestRate

router = APIRouter(prefix="/accounts", tags=["accounts"])

# Account endpoints
@router.post("", response_model=Account)
async def create_account(account: Account):
    # TODO: Add database integration
    return account

@router.get("", response_model=List[Account])
async def get_accounts():
    # TODO: Add database integration
    return []

@router.get("/{account_id}", response_model=Account)
async def get_account(account_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Account not found")

# Subaccount endpoints
@router.post("/subaccounts", response_model=Subaccount)
async def create_subaccount(subaccount: Subaccount):
    # TODO: Add database integration
    return subaccount

@router.get("/subaccounts", response_model=List[Subaccount])
async def get_subaccounts():
    # TODO: Add database integration
    return []

@router.get("/subaccounts/{subaccount_id}", response_model=Subaccount)
async def get_subaccount(subaccount_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Subaccount not found")

# Interest rate endpoints
@router.post("/interest-rates", response_model=InterestRate)
async def create_interest_rate(interest_rate: InterestRate):
    # TODO: Add database integration
    return interest_rate

@router.get("/interest-rates", response_model=List[InterestRate])
async def get_interest_rates():
    # TODO: Add database integration
    return []

@router.get("/interest-rates/{interest_rate_id}", response_model=InterestRate)
async def get_interest_rate(interest_rate_id: str):
    # TODO: Add database integration
    raise HTTPException(status_code=404, detail="Interest rate not found") 