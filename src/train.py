import os, time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import joblib

from data import load_data, simple_clean

def main(random_state: int = 42):
    X, y, ds = load_data()
    X = simple_clean(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=random_state
    )

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average="binary"
    )

    os.makedirs("results", exist_ok=True)
    metrics = pd.DataFrame([{
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "dataset": "sklearn_breast_cancer",
        "model": "StandardScaler+LogisticRegression",
        "test_size": 0.2,
        "random_state": random_state,
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }])
    metrics.to_csv("results/metrics.csv", index=False)
    joblib.dump(pipe, "results/model.joblib")

    print(metrics.to_string(index=False))

if __name__ == "__main__":
    main()
