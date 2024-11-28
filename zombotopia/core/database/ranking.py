from sqlalchemy.orm import Session

from .models import Ranking
from .models.ranking import Ranking
from typing import List, Optional, Type


class RankingService:
    def __init__(self, db: Session):
        self.db = db

    def get_rankings(self) -> list[Ranking]:
        rankings = self.db.query(Ranking).order_by(Ranking.score.desc()).all()

        return rankings

    def create_ranking(self, user_id: str, score: int) -> Ranking:
        ranking = Ranking(user_id=user_id, score=score)
        self.db.add(ranking)
        self.db.commit()
        self.db.refresh(ranking)
        return ranking

    def get_ranking_by_id(self, user_id: str) -> Optional[tuple[Ranking, int]]:
        rankings = self.db.query(Ranking).order_by(Ranking.score.desc()).all()

        for rank, ranking in enumerate(rankings, 1):
            if ranking.user_id == user_id:
                return (ranking, rank)

        return None

    def update_ranking(self, user_id: str, score: int) -> Optional[Ranking]:
        ranking = self.get_ranking_by_id(user_id)
        if ranking:
            if ranking[0].score < score:
                ranking[0].score = score
                self.db.commit()
                self.db.refresh(ranking[0])
        else:
            ranking = self.create_ranking(user_id, score)
        return ranking

    def delete_ranking(self, user_id: str) -> bool:
        ranking = self.get_ranking_by_id(user_id)
        if ranking:
            self.db.delete(ranking)
            self.db.commit()
            return True
        return False
