from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_positive_sentiment():
    response = client.post("/v1/analyze/sentiment", json={"text": "This is an excellent amazing product!"})

    assert response.status_code == 200
    
    data = response.json()

    assert data["label"] == "positive"
    assert data["score"] == 0.8
    assert data["input_length"] == len("This is an excellent amazing product!")


def test_negative_sentiment():
    response = client.post("/v1/analyze/sentiment", json={"text": "This is a terrible product!"})

    assert response.status_code == 200
    
    data = response.json()

    assert data["label"] == "negative"
    assert data["score"] == 0.8
    assert data["input_length"] == len("This is a terrible product!")


def test_query_sentiment_with_debug():
    response = client.post("/v1/analyze/sentiment?include_debug=true", json={"text": "This product is good"})

    assert response.status_code == 200
    
    data = response.json()

    assert data["label"] == "positive"
    assert data["score"] == 0.8
    assert data["input_length"] == len("This product is good")
    
    assert data["debug"] is not None
    assert data['debug']['positive_word_hits'] == 1
    assert data['debug']['negative_word_hits'] == 0


def test_query_sentiment_without_debug():
    response = client.post("/v1/analyze/sentiment?include_debug=false", json={"text": "This product is good"})

    assert response.status_code == 200
    
    data = response.json()

    assert data["label"] == "positive"
    assert data["score"] == 0.8
    assert data["input_length"] == len("This product is good")
    
    assert 'debug' not in data

def test_sentiment_empty_text_rejected():
    response = client.post("/v1/analyze/sentiment", json={"text": ""})

    assert response.status_code == 422