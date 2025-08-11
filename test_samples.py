import json
from model_utils import load_pipeline, predict_texts

pipeline = load_pipeline("best_pipeline.joblib")

samples = [
    "Bilet almak istiyorum, 2 yetişkin, 1 çocuk, 21:00 seansı.",
    "Rezervasyonumu iptal etmek istiyorum, numara: 12345.",
    "Salon çok soğuktu, şikayet etmek istiyorum.",
    "Yeni çıkan filmleri nasıl görebilirim?",
    "Ödeme sırasında kartım reddedildi, yardım lütfen."
]

preds, probs = predict_texts(pipeline, samples)

results = []
for text, p, pr in zip(samples, preds, (probs or [None]*len(samples))):
    results.append({"text": text, "prediction": p, "probability": pr})

with open('pred_samples.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print('Saved pred_samples.json with', len(results), 'items')
