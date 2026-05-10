from fastapi import FastAPI
from app.api.routes import health, sentiment, models


app = FastAPI(
    title="FastApi service",
    version = "0.1.0",
    description="A small FastAPI service for sentiment analysis",
)


app.include_router(health.router)
app.include_router(sentiment.router)
app.include_router(models.router)


