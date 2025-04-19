from app.core.orm.base import Base, BaseModel
from app.core.orm.properties import Garage, Apartment, House
from app.core.orm.persons import Person
from app.core.orm.contracts import Contract
from app.core.orm.deposits import Deposit
from app.core.orm.accounts import Account, Subaccount, InterestRate

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