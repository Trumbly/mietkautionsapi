from api.v1.orms.base import Base, BaseModel
from api.v1.orms.properties import Garage, Apartment, House
from api.v1.orms.persons import Person
from api.v1.orms.contracts import Contract
from api.v1.orms.deposits import Deposit
from api.v1.orms.accounts import Account, Subaccount, InterestRate

__all__ = [
    "Base",
    "BaseModel",
    "Garage",
    "Apartment",
    "House",
    "Person",
    "Contract",
    "Deposit",
    "Account",
    "Subaccount",
    "InterestRate",
] 