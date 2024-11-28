from pydantic import BaseModel


class RankingModel(BaseModel):
    user_id: str
    score: int

class UserRankingModel(BaseModel):
    user_id: str
    score: int
    rank: int
