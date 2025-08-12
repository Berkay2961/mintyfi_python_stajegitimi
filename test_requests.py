from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Örnek eğitim verisi (sen burayı kendi verinle değiştirebilirsin)
X_train = [
    "bu film harikaydı",
    "çok kötü bir deneyim",
    "mükemmel performans",
    "berbat oyunculuk",
    "şahane bir yapım",
    "tam bir zaman kaybı"
]
y_train = ["pozitif", "negatif", "pozitif", "negatif", "pozitif", "negatif"]

# Model pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Modeli eğit
model.fit(X_train, y_train)

# Modeli kaydet
joblib.dump(model, "model.pkl")

print("Model başarıyla kaydedildi: model.pkl")
