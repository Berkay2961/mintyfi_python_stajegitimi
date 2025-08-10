from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd

# Örnek veri (sen burada kendi verini yükle)
data = {
    "text": [
        "Ben çok mutluyum",
        "Bu film çok kötüydü",
        "Hava çok güzel",
        "Burası çok kalabalık",
        "Müzik harikaydı",
        "Yemek berbattı"
    ],
    "label": [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
X = df["text"]
y = df["label"]

# Train / Valid split (80/20, stratified)
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_valid_tfidf = vectorizer.transform(X_valid)

# Modeller
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
    "MultinomialNB": MultinomialNB(),
    "RandomForest": RandomForestClassifier(random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train_tfidf, y_train)
    y_pred = model.predict(X_valid_tfidf)

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_valid, y_pred),
        "Precision": precision_score(y_valid, y_pred, average="weighted", zero_division=0),
        "Recall": recall_score(y_valid, y_pred, average="weighted", zero_division=0),
        "F1": f1_score(y_valid, y_pred, average="weighted", zero_division=0),
        "Confusion Matrix": confusion_matrix(y_valid, y_pred)
    })

df_results = pd.DataFrame(results)

# Markdown çıktısı
with open("results_day3.md", "w", encoding="utf-8") as f:
    f.write("# Day 3 Model Kıyas Sonuçları\n\n")
    f.write(df_results[["Model", "Accuracy", "Precision", "Recall", "F1"]].to_markdown(index=False))
    f.write("\n\n**En İyi Model:** " + df_results.sort_values(by="F1", ascending=False).iloc[0]["Model"])
