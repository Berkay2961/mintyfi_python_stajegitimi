# Transfer Learning Notları

## Kullanılan Modeller
- **ResNet18 (ImageNet)**  
  Çıkış boyutu: [1, 1000]  
  Gözlem: Model 1000 sınıflı ImageNet için eğitilmiş.

- **DistilBERT (distilbert-base-uncased)**  
  Çıkış boyutu: [1, token_sayısı, 768]  
  CLS token boyutu: [1, 768]  
  Gözlem: Her token için 768 boyutlu embedding üretiyor.
