from fastapi import APIRouter

from .ranking import router as ranking_router

router = APIRouter()


router.include_router(ranking_router, prefix="/ranking", tags=["ranking"])