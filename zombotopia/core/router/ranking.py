# zombotopia/core/router/ranking.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from zombotopia.core.database import get_db
from zombotopia.core.database.ranking import RankingService
from zombotopia.core.schemas.base import SuccessSchema, ErrorSchema
from zombotopia.core.schemas.ranking import RankingModel

router = APIRouter()

@router.get('')
async def get_rankings(db: Session = Depends(get_db)) -> List[RankingModel]:
    ranking_service = RankingService(db)
    rankings = ranking_service.get_rankings()
    return [RankingModel(user_id=ranking.user_id, score=ranking.score) for ranking in rankings]

@router.get('/{user_id}')
async def get_ranking(user_id: str, db: Session = Depends(get_db)) -> RankingModel | ErrorSchema:
    try:
        ranking_service = RankingService(db)
        ranking = ranking_service.get_ranking_by_id(user_id)
        return RankingModel(
            user_id=ranking.user_id,
            score=ranking.score
        )
    except Exception as e:
        return ErrorSchema(message=str(e))

@router.post('')
async def create_ranking(ranking: RankingModel, db: Session = Depends(get_db)) -> SuccessSchema | ErrorSchema:
    try:
        ranking_service = RankingService(db)
        ranking_service.update_ranking(ranking.user_id, ranking.score)
        return SuccessSchema()
    except Exception as e:
        return ErrorSchema(message=str(e))

@router.delete('/{user_id}')
async def delete_ranking(user_id: str, db: Session = Depends(get_db)) -> SuccessSchema | ErrorSchema:
    try:
        ranking_service = RankingService(db)
        ranking_service.delete_ranking(user_id)

        return SuccessSchema()
    except Exception as e:
        return ErrorSchema(message=str(e))
