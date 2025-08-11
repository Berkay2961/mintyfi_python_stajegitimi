from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

X = [
    "Bilet almak istiyorum",
    "Rezervasyon iptal",
    "Film çok güzeldi",
    "Ödeme hata verdi",
    "Bilgi almak istiyorum",
    "Salon soğuktu",
    "Kampanya var mı",
    "Bilet iadesi yapıldı"
]
y = [1, 0, 1, 0, 1, 0, 1, 0]

pipeline = Pipeline([
    ("vect", TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)
joblib.dump(pipeline, "best_pipeline.joblib")
print("Saved best_pipeline.joblib")
