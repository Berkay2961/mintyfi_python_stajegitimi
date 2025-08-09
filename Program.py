import pandas as pd

# 1. Veri setini oku
df = pd.read_csv(
    "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# 2. İlk 5 satırı göster
print("İlk 5 satır:")
print(df.head())

# 3. Veri bilgisi
print("\nVeri Bilgisi:")
print(df.info())

# 4. Sınıf dağılımı
print("\nSınıf Sayıları:")
print(df['label'].value_counts())

# Eksik değer kontrolü
print("\nEksik değer sayısı:")
print(df.isnull().sum())

# Eksik satırları sil
df = df.dropna()

# Yinelenen kayıtları sil
df = df.drop_duplicates()

# Encoding sorunlarını gider (gerekiyorsa)
df['message'] = df['message'].apply(lambda x: x.encode('utf-8', errors='ignore').decode('utf-8'))

print(f"\nTemizlenmiş veri satır sayısı: {len(df)}")

# Temiz veri setini kaydet
df.to_csv("sms_clean.csv", index=False)
print("\nTemiz dosya sms_clean.csv olarak kaydedildi.")
