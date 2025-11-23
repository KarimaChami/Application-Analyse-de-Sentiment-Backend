from fastapi import FastAPI, Depends, Request
from app.database.schemas import LoginRequest
from .auth import create_access_token, authenticate_user, verify_token
from app.sentiment import analyze_sentiment, simplify_sentiment
from app.database.schemas import SentimentRequest
from app.database.db import get_db
from app.database.models import Sentiment
from sqlalchemy.orm import Session
from app.database.db import Base, engine

from fastapi.middleware.cors import CORSMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# --------------------------
# CORS MIDDLEWARE
# --------------------------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://172.18.80.1:3000",  # Next.js dev IP
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------


@app.post("/login")
def login(request: LoginRequest):
    if not authenticate_user(request.username, request.password):
        return {"error": "Invalid !!!!"}

    token = create_access_token(request.username)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/sentiment")
def get_sentiment(
    body: SentimentRequest,
    username: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    hf_response = analyze_sentiment(body.text)

    if "error" in hf_response[0]:
        return hf_response

    result = simplify_sentiment(hf_response)

    sentiment = Sentiment(
        text=body.text,
        label=result[0]["label"],
        score=result[0]["score"],
        username=username,
    )

    db.add(sentiment)
    db.commit()
    db.refresh(sentiment)

    return result
