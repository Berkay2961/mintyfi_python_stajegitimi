from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello AI!"}

def test_predict_positive():
    response = client.post("/predict", json={"text": "abcd"})
    assert response.status_code == 200
    assert response.json()["prediction"] == "positive"

def test_predict_negative():
    response = client.post("/predict", json={"text": "abc"})
    assert response.status_code == 200
    assert response.json()["prediction"] == "negative"
