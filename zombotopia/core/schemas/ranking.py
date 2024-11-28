from pydantic import BaseModel


class RankingModel(BaseModel):
    user_id: str
    score: int
