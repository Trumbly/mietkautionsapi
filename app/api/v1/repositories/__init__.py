from api.v1.repositories.base import BaseRepository
from api.v1.repositories.properties import GarageRepository, ApartmentRepository, HouseRepository
from api.v1.repositories.persons import PersonRepository
from api.v1.repositories.contracts import ContractRepository
from api.v1.repositories.deposits import DepositRepository
from api.v1.repositories.accounts import AccountRepository, SubaccountRepository, InterestRateRepository

__all__ = [
    "BaseRepository",
    "GarageRepository",
    "ApartmentRepository",
    "HouseRepository",
    "PersonRepository",
    "ContractRepository",
    "DepositRepository",
    "AccountRepository",
    "SubaccountRepository",
    "InterestRateRepository",
] 