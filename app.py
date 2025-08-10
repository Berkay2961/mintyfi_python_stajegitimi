import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")


def train_and_log(ngram_range, C, max_features):
    print("Run başladı, parametreler:", ngram_range, C, max_features)

    # mlflow.start_run() olmadan sadece model eğitimi
    print("Veri yükleniyor...")
    data = fetch_20newsgroups(subset='train', categories=['rec.sport.baseball', 'sci.med'])
    print("Veri bölünüyor...")
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)
    print("Pipeline oluşturuluyor...")
    pipeline = Pipeline([
        ('vect', CountVectorizer(ngram_range=ngram_range, max_features=max_features)),
        ('clf', LogisticRegression(C=C, max_iter=1000))
    ])
    print("Model eğitiliyor...")
    pipeline.fit(X_train, y_train)
    print("Tahmin yapılıyor...")
    preds = pipeline.predict(X_test)
    print("Accuracy hesaplanıyor...")
    acc = accuracy_score(y_test, preds)
    print("Accuracy:", acc)

    # mlflow loglama olmadan devam edelim
    return acc, "dummy_run_id"
