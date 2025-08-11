import joblib
from typing import List, Tuple, Optional, Any

def save_pipeline(pipeline: Any, path: str = "best_pipeline.joblib") -> None:
    joblib.dump(pipeline, path)

def load_pipeline(path: str = "best_pipeline.joblib") -> Any:
    return joblib.load(path)

def predict_texts(pipeline: Any, texts: List[str]) -> Tuple[List[Any], Optional[List[List[float]]]]:
    preds = pipeline.predict(texts).tolist()
    probs = None
    try:
        if hasattr(pipeline, "predict_proba"):
            probs = pipeline.predict_proba(texts).tolist()
    except Exception:
        probs = None
    return preds, probs
