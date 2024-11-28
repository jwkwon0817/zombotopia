from sqlalchemy import Column, Integer, String
from zombotopia.core.database import Base

class Ranking(Base):
    __tablename__ = "rankings"

    user_id = Column(String, primary_key=True, index=True)
    score = Column(Integer)
