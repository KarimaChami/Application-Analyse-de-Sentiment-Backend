from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    label = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    username = Column(String, nullable=True)  # who sent the text
