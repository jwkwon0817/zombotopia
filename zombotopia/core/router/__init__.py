from fastapi import APIRouter

from .ranking import router as ranking_router

router = APIRouter()

@router.get('/test')
def test():
    return {"message": "Test dfasdfsdaf"}

router.include_router(ranking_router, prefix="/ranking", tags=["ranking"])