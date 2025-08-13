<<<<<<< HEAD
# mintyfi_python_stajegitimi
=======
# Mini ML Projesi — Göğüs Kanseri Sınıflandırma (Baseline)

Bu proje, **küçük ölçekli** bir makine öğrenimi projesini **uçtan uca** başlatmak için hazırlanmış bir iskelet sunar. 
Amaç: problem tanımı + temel pipeline + ilk sonuç tablosu.

## Problem
- **Veri seti:** `sklearn.datasets.load_breast_cancer` (Wisconsin Breast Cancer)
- **Görev:** İkili sınıflandırma (kitle **kötü huylu** mu **iyi huylu** mu)
- **Hedef değişken:** `target` (0 = malignant, 1 = benign)

## Baseline Pipeline
1. Veriyi yükle & temel temizlik (eksik değer kontrolü)
2. `train_test_split` (stratified)
3. `StandardScaler` + `LogisticRegression(max_iter=1000)`
4. Değerlendirme: Accuracy, Precision, Recall, F1
5. Sonuçları `results/metrics.csv` dosyasına yaz

## Kurulum (Windows / VS Code)
> **Öneri:** VS Code → Terminal (PowerShell) içerinden komutları çalıştırın.

```powershell
# 1) Sanal ortam oluştur
py -m venv .venv
.\.venv\Scripts\Activate

# 2) Bağımlılıkları kur
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) Eğitimi çalıştır ve sonuç üret
python src/train.py
```

> Çalışma bittiğinde `results/metrics.csv` dosyasında ilk sonuç tablosu oluşur, `results/model.joblib` ise kaydedilmiş baseline modeldir.

## Proje Yapısı
```
mini-ml-breast-cancer/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ data.py
│  └─ train.py
└─ results/
   └─ .gitkeep
```

## İlk Sonuç Tablosu (örnek başlıklar)
`results/metrics.csv` sütunları:
- `timestamp`, `dataset`, `model`, `test_size`, `random_state`, `accuracy`, `precision`, `recall`, `f1`

> Tabloyu görmek için: VS Code içinde `results/metrics.csv` dosyasını açın.

## Git & GitHub (klonlama olmadan, VS Code ile Yayımla)
1. VS Code **Source Control** (Ctrl+Shift+G) → **Initialize Repository**.
2. Dosyaları **Stage** edip mesajla **Commit** edin (örn: "init: baseline + readme + results").
3. Source Control panelindeki **Publish Branch** / **Publish to GitHub** seçeneği ile **yeni bir repo oluşturup** doğrudan GitHub’a gönderin.
   - **Not:** GitHub’da **yeni repo oluştururken README/License/.gitignore eklemeyin** (boş olsun). Aksi halde *"fetch first"* hatası alırsınız.
4. Alternatif CLI (manuel): GitHub’da **boş** repo oluşturduktan sonra:
   ```powershell
   git init
   git add .
   git commit -m "init: baseline + readme + results"
   git branch -M main
   git remote add origin https://github.com/<kullanici>/<repo-adi>.git
   git push -u origin main
   ```
   - Yanlışlıkla GitHub’da başlangıç README eklediyseniz ve *"fetch first"* hatası görürseniz:
     - Çözüm A (önerilen): GitHub’da boş repo oluşturup yukarıdaki adımları uygulayın.
     - Çözüm B: `git pull --rebase origin main` ardından tekrar `git push` (çakışma çözmeniz gerekebilir).

## Tekrarlanabilirlik
- Python 3.10+ önerilir.
- Determinizm için `random_state=42` kullanılır.
- `requirements.txt` ile ortamı sabitleyin.

## Yol Haritası
- [ ] Bazeline’ı çapraz doğrulama ile kıyasla
- [ ] Alternatif modeller (SVC, RandomForest)
- [ ] Özellik önemi & hata analizi
- [ ] Model seçimi ve raporlama

---

**Lisans:** Veri seti `scikit-learn` ile gelen örnek veri setidir. Eğitim kodu MIT benzeri serbest kullanım içindir.
>>>>>>> ad66513 (init: baseline + readme + results)
