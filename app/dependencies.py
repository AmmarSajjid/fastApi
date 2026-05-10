from app.services.sentiment import SentimentService


def get_sentiment_service() -> SentimentService:
    return SentimentService()