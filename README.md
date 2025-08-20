<<<<<<< HEAD
# mintyfi_python_stajegitimi
=======
# MNIST MLP (1000 Örnek, 5 Epoch)

Bu proje, **MNIST veri kümesi** üzerinde basit bir **MLP (Multi-Layer Perceptron)** eğitimi örneğini gösterir.  
Amaç: Eğitim döngüsünü uçtan uca görmek (dataloading → training → validation → sonuçların kaydı).

## Özellikler
- **Veri:** MNIST, eğitimden 1000 örnek altküme
- **Model:** 3 katmanlı MLP (256 → 128 → 10)
- **Loss:** CrossEntropyLoss
- **Optimizer:** Adam
- **Epoch:** 5
- **Çıktılar:**
  - `mlp_loss.png` → Eğitim & validation kaybı grafiği
  - `mlp_metrics.json` → Nihai metrikler (train/val loss & accuracy)

## Kullanım
```bash
# Ortamı oluştur
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Eğitimi çalıştır
python train_mnist_mlp.py
>>>>>>> 0374ba6 (init: MNIST MLP sinir ağı (1000 örnek, 5 epoch))
