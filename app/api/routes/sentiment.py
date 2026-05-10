from fastapi import APIRouter, Depends
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.dependencies import get_sentiment_service
from app.services.sentiment import SentimentService
from typing import Annotated

router = APIRouter(tags=["sentiment"])

@router.post("/v1/analyze/sentiment", response_model=SentimentResponse, response_model_exclude_none=True)
def analyze_sentiment(
        request: SentimentRequest,
        sentiment_service=Annotated[SentimentService, Depends(get_sentiment_service)],
        include_debug: bool = False,
    ) -> SentimentResponse:

    result = sentiment_service.predict(request.text)

    if not include_debug:
        result["debug"] = None

    return SentimentResponse(
        label=result["label"],
        score=result["score"],
        input_length=result["input_length"],
        debug=result["debug"] if include_debug else None,
    )