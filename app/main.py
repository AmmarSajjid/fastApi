from fastapi import FastAPI
from app.schemas import SentimentRequest, SentimentResponse
from app.services import SentimentService

app = FastAPI(
    title="FastApi service",
    version = "0.1.0",
    description="A small FastAPI service for sentiment analysis",
)

sentiment_service = SentimentService()


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/v1/analyze/sentiment", response_model=SentimentResponse, response_model_exclude_none=True)
def analyze_sentiment(request: SentimentRequest, include_debug: bool = False) -> SentimentResponse:
    result = sentiment_service.predict(request.text)

    if not include_debug:
        result["debug_info"] = None

    return SentimentResponse(**result)