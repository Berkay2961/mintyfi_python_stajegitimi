from sklearn.datasets import load_breast_cancer
import pandas as pd

def load_data():
    data = load_breast_cancer(as_frame=True)
    df = data.frame.copy()
    X = df.drop(columns=["target"])
    y = df["target"]
    return X, y, data

def simple_clean(X: pd.DataFrame) -> pd.DataFrame:
    X = X.copy()
    # Eksik değer yok; yine de güvenlik için doldurma örneği
    if X.isna().sum().sum() > 0:
        X = X.fillna(X.median(numeric_only=True))
    return X
