from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello AI!"}

@app.post("/predict")
def predict(request: PredictRequest):
    length = len(request.text)
    return {"length": length, "prediction": "positive" if length % 2 == 0 else "negative"}
