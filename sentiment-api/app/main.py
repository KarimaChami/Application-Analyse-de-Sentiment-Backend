from fastapi import FastAPI, Depends
from .auth import create_access_token, authenticate_user, verify_token 
# from app.schemas import TextInput, SentimentResult
from app.sentiment import analyze_sentiment, simplify_sentiment
from app.schemas import SentimentRequest
from app.db import get_db
from app.models import Sentiment
from sqlalchemy.orm import Session
from .db import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sentiment API running successfully."}

# @app.post("/api/sentiment", response_model=list)
# def sentiment_route(data: TextInput):
#     result = analyze_sentiment(data.text)
#     return result
@app.post("/sentiment")
def get_sentiment(request: SentimentRequest, username: str = Depends(verify_token),db: Session = Depends(get_db)):
    hf_response = analyze_sentiment(request.text)
    
    # Si Hugging Face renvoie une erreur
    if "error" in hf_response[0]:
        return hf_response

    # Transformer la réponse en POSITIVE/NEUTRAL/NEGATIVE
    result = simplify_sentiment(hf_response)
    # Save to DB
    sentiment = Sentiment(
        text=request.text,
        label=result[0]["label"],
        score=result[0]["score"],
        username=username
    )
    db.add(sentiment)
    db.commit()
    db.refresh(sentiment)
    return result