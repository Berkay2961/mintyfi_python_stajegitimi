import argparse
import json
from model_utils import load_pipeline, predict_texts

def predict_single(pipeline, text: str) -> dict:
    preds, probs = predict_texts(pipeline, [text])
    return {
        "text": text,
        "prediction": preds[0],
        "probability": probs[0] if probs is not None else None
    }

def main():
    parser = argparse.ArgumentParser(description="Predict CLI — python predict.py \"mesaj metni\"")
    parser.add_argument("text", type=str, help="Tahmin edilecek mesaj metni")
    args = parser.parse_args()

    pipeline = load_pipeline()
    out = predict_single(pipeline, args.text)
    print(json.dumps(out, ensure_ascii=False))

if __name__ == "__main__":
    main()
