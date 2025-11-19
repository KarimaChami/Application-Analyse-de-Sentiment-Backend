from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class SentimentResult(BaseModel):
    label: str
    score: float
