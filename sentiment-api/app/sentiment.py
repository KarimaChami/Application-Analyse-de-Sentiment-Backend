import requests
from app.database.config import settings

API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"

headers = {"Authorization": f"Bearer {settings.HF_API_KEY}"}

def analyze_sentiment(text: str):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text}
    )

    data = response.json()

    # Hugging Face error handling
    if isinstance(data, dict) and "error" in data:
        return [{"label": "error", "score": 0.0, "detail": data["error"]}]

    return data
def simplify_sentiment(hf_response):
    scores = hf_response[0]  # Hugging Face renvoie [ [ ... ] ]
    best = max(scores, key=lambda x: x["score"])
    star = int(best["label"].split()[0])

    if star <= 2:
        sentiment = "NEGATIVE"
    elif star == 3:
        sentiment = "NEUTRAL"
    else:
        sentiment = "POSITIVE"

    return [{"label": sentiment, "score": best["score"]}]
