from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# FastAPI uygulamasını başlat
app = FastAPI()

# İstek gövdesi modeli
class TextRequest(BaseModel):
    text: str

# Uygulama başladığında model dosyasını yükle
@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("model.pkl")  # Model dosyası proje klasöründe olmalı

# /predict endpoint'i
@app.post("/predict")
def predict(request: TextRequest):
    prediction = model.predict([request.text])[0]
    probability = max(model.predict_proba([request.text])[0])
    return {
        "prediction": prediction,
        "probability": float(probability)
    }
