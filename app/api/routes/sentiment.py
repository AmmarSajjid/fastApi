from fastapi import APIRouter
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.dependencies import get_sentiment_service

router = APIRouter(tags=["sentiment"])
sentiment_service = get_sentiment_service()

@router.post("/v1/analyze/sentiment", response_model=SentimentResponse, response_model_exclude_none=True)
def analyze_sentiment(request: SentimentRequest, include_debug: bool = False) -> SentimentResponse:
    result = sentiment_service.predict(request.text)

    if not include_debug:
        result["debug_info"] = None

    return SentimentResponse(
        label=result["label"],
        score=result["score"],
        input_length=result["input_length"],
        debug=result["debug"] if include_debug else None,
    )