from sqlalchemy.orm import Session

from .models import Ranking
from .models.ranking import Ranking
from typing import List, Optional, Type


class RankingService:
    def __init__(self, db: Session):
        self.db = db

    def get_rankings(self) -> list[Ranking]:
        return self.db.query(Ranking).all()

    def create_ranking(self, user_id: str, score: int) -> Ranking:
        ranking = Ranking(user_id=user_id, score=score)
        self.db.add(ranking)
        self.db.commit()
        self.db.refresh(ranking)
        return ranking

    def get_ranking_by_id(self, user_id: str) -> Optional[Ranking]:
        return self.db.query(Ranking).filter(Ranking.user_id == user_id).first()

    def update_ranking(self, user_id: str, score: int) -> Optional[Ranking]:
        ranking = self.get_ranking_by_id(user_id)
        if ranking:
            if ranking.score < score:
                ranking.score = score
                self.db.commit()
                self.db.refresh(ranking)
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
