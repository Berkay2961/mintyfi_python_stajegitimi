# Veri Seti Temizleme Özeti (SMS Spam)

- Kaynak: https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv
- Orijinal veri boyutu: 5572 kayıt
- Temizlik adımları:
  - Boş değerler kaldırıldı
  - Yinelenen kayıtlar silindi
  - Etiketler sayısallaştırıldı (`ham` → 0, `spam` → 1)

## Sınıf Dağılımı (temiz veri)
- Ham: 4825
- Spam: 747
