from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_positive_sentiment():
    response = client.post("/v1/analyze/sentiment", json={"text": "I love this product!"})

    assert response.status_code == 200
    
    data = response.json()

    assert data["label"] == "positive"
    assert data["score"] == 0.8
    assert data["input_length"] == len("I love this product!")


def test_sentiment_empty_text_rejected():
    response = client.post("/v1/analyze/sentiment", json={"text": ""})

    assert response.status_code == 422