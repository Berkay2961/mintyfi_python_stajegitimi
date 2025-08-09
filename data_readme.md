import pandas as pd

# Temiz veri setini oku
df = pd.read_csv("sms_clean.csv")

# data_readme.md dosyasını yeniden oluştur
with open("data_readme.md", "w", encoding="utf-8") as f:
    f.write("# SMS Spam/Ham Dataset Notları\n")
    f.write(f"Toplam Kayıt: {len(df)}\n")
    f.write("## Sınıf Dağılımı:\n")
    f.write(str(df['label'].value_counts()) + "\n\n")
    f.write("## Veri Hakkında:\n")
    f.write("- Veri seti SMS mesajlarını içeriyor.\n")
    f.write("- 'label' kolonu mesajın spam olup olmadığını gösteriyor.\n")
    f.write("- 'message' kolonu mesaj içeriğini içeriyor.\n")
    f.write("- Eksik değerler ve yinelenen satırlar temizlendi.\n")

print("data_readme.md dosyası başarıyla oluşturuldu.")
