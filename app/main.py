from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import numpy as np
from typing import Any

class PredictRequest(BaseModel):
    text: str

app = FastAPI(title="Text Classifier API")

class ModelWrapper:
    def __init__(self, model: Any):
        self.model = model

    def predict(self, texts):
        if self.model is None:
            # Basit fallback
            return ["positive" if "good" in t.lower() or "love" in t.lower() else "negative" for t in texts]
        return self.model.predict(texts)

    def predict_proba(self, texts):
        if self.model is None:
            probs = []
            for t in texts:
                if "good" in t.lower() or "love" in t.lower():
                    probs.append([0.1, 0.9])
                else:
                    probs.append([0.8, 0.2])
            return np.array(probs)

        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(texts)
        preds = self.model.predict(texts)
        probs = []
        for p in preds:
            if p == preds[0]:
                probs.append([0.05, 0.95])
            else:
                probs.append([0.95, 0.05])
        return np.array(probs)

@app.on_event("startup")
def load_model():
    model_path = os.path.join(os.getcwd(), "model.pkl")
    if os.path.exists(model_path):
        try:
            m = joblib.load(model_path)
            app.state.model = ModelWrapper(m)
            print(f"Loaded model from {model_path}")
        except Exception as e:
            print("Failed to load model.pkl:", e)
            app.state.model = ModelWrapper(None)
    else:
        print("model.pkl not found — using dummy fallback model.")
        app.state.model = ModelWrapper(None)

@app.post("/predict")
def predict(req: PredictRequest):
    model_wrapper: ModelWrapper = app.state.model
    texts = [req.text]
    try:
        preds = model_wrapper.predict(texts)
        probs = model_wrapper.predict_proba(texts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if probs is None:
        top_class = preds[0]
        top_prob = None
    else:
        top_idx = int(np.argmax(probs[0]))
        top_prob = float(probs[0][top_idx])
        top_class = "positive" if top_idx == 1 else "negative"

    return {"class": top_class, "probability": round(top_prob, 4) if top_prob is not None else None}
