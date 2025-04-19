from fastapi import APIRouter
from .properties import router as properties_router
from .persons import router as persons_router
from .contracts import router as contracts_router
from .deposits import router as deposits_router
from .accounts import router as accounts_router

router = APIRouter()

router.include_router(properties_router)
router.include_router(persons_router)
router.include_router(contracts_router)
router.include_router(deposits_router)
router.include_router(accounts_router) 