from  pydantic import BaseModel, Field


class SentimentRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=1000,
        description="Input text to analyze sentiment.",
    )


class SentimentResponse(BaseModel):
    label: str
    score: float
    input_length: int