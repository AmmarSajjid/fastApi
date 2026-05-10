from fastapi import FastAPI
from app.schemas import SentimentRequest, SentimentResponse
from app.services import SentimentService

app = FastAPI(
    text="FastApi service",
    version = "0.1.0",
    description="A small FastAPI service for sentiment analysis",
)

sentiment_service = SentimentService()


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/v1/analyze/sentiment", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest) -> SentimentResponse:
    result = sentiment_service.predict(request.text)
    return SentimentResponse(**result)