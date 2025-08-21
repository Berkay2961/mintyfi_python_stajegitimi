# Prompt Mühendisliği – 5 Varyasyon Karşılaştırması
**Tarih:** 2025-08-22  
**Hazırlayan:** Berkay Şahin

Bu dosyada aynı metin üzerinde 5 farklı prompt stilini deniyor ve sonuçları kısa bir tablo ile kıyaslıyoruz.  
Varyasyonlar: **Kısa**, **Detaylı**, **Örnekli (few-shot)**, **Rol tabanlı**, **Kısıtlı**.

---

## Kaynak Metin
> Yapay zeka modelleri, kullanıcı taleplerini doğru yorumlamak için iyi tasarlanmış istemlere (prompt) ihtiyaç duyar. 
> İyi bir prompt; açık hedef, yeterli bağlam, istenen çıktı formatı ve güvenlik/gizlilik kısıtları içerir. 
> Bu sayede modelden daha tekrarlanabilir ve denetlenebilir sonuçlar alınır.

---

## 1) Kısa Prompt
**Kullandığım prompt:**  
“Bu metni 2 maddede, öz ve nesnel biçimde özetle.”

**Örnek çıktı:**  
- İyi tasarlanmış prompt hedef, bağlam, çıktı formatı ve güvenlik kısıtları içerir.  
- Bu unsurlar, sonuçların tekrarlanabilir ve denetlenebilir olmasını sağlar.

---

## 2) Detaylı Prompt (adım, format, kalite ölçütleri)
**Kullandığım prompt:**  
“Aşağıdaki metni **iki maddelik özet**e dönüştür. Önce ana iddiayı, sonra faydayı yaz. 
Cümleleri kısa tut. Tarafsız kal. **JSON** formatında dön: `{"bullet_1": "...","bullet_2": "..."}`.
Güvenlik notu: Gizli/sensitive veri ekleme.”

**Örnek çıktı (JSON):**
{
  "bullet_1": "İyi bir prompt hedefi, bağlamı, çıktı biçimini ve güvenlik kısıtlarını tanımlar.",
  "bullet_2": "Bu sayede model çıktıları daha tekrarlanabilir ve denetlenebilir olur."
}

---

## 3) Örnekli (Few-shot) Prompt
**Kullandığım prompt:**  
**Örnek 1 — Girdi:** “Model değerlendirme yöntemlerini 2 maddede özetle.”  
**Örnek 1 — Çıktı:**  
- Metriği tanımla ve amaçla ilişkilendir.  
- Tutarlılığı artırmak için standardize edilmiş prosedürler uygula.  

**Talep edilen görev — Girdi:** “Kaynak metni 2 maddede özetle.”  
**Kurallar:** Madde başlarına fiil ile başla; 10–18 kelime aralığı.

**Örnek çıktı:**  
- Tanımla: Hedef, bağlam, çıktı biçimi ve güvenlik kısıtlarını açıkça belirle.  
- Sağla: Tekrarlanabilir, denetlenebilir ve tutarlı sonuçların üretimini kolaylaştır.

---

## 4) Rol Tabanlı Prompt
**Kullandığım prompt:**  
“**Kıdemli teknik editör** rolündesin. Metindeki ana iddiayı öncele, pazarlama dili kullanma.  
Çıktıyı Markdown’da iki madde olarak ver.”

**Örnek çıktı:**  
- İyi bir prompt; hedefi, bağlamı, çıktı formatını ve güvenlik kısıtlarını açıklar.  
- Bu yapı, çıktının tekrarlanabilirliğini ve denetlenebilirliğini artırır.

---

## 5) Kısıtlı Prompt (sınırlar, yasaklı sözcükler, uzunluk)
**Kullandığım prompt:**  
“Metni **tam iki** maddede özetle. **Her madde ≤ 16 kelime.**  
Yasaklı sözcükler: *devrim, çığır açan, inanılmaz*. Biçim: `-` ile başlayan maddeler.”

**Örnek çıktı:**  
- İyi prompt; hedef, bağlam, format ve güvenlik kısıtlarını içerir.  
- Bu, sonuçların tekrarlanabilir ve denetlenebilir olmasını sağlar.

---

## Karşılaştırma Tablosu (kısa değerlendirme)

| Varyasyon  | Format Uyum | Kısalık | Kapsam | Tutarlılık | Güvenlik/Gizlilik Notu |
|---|---|---|---|---|---|
| Kısa      | Orta      | Yüksek  | Orta  | Orta  | Güvenlik maddesi geçmeyebilir |
| Detaylı   | Çok yüksek| Orta    | Yüksek| Yüksek| Format (JSON) ve güvenlik açık |
| Örnekli   | Yüksek    | Orta    | Yüksek| Yüksek| Örnekler sayesinde üslup sabit |
| Rol tabanlı| Yüksek   | Orta    | Yüksek| Yüksek| Editör rolü tonda tutarlılık sağlar |
| Kısıtlı   | Yüksek    | Çok yüksek| Orta| Yüksek| Yasaklı sözcük/uzunluk koruması |

---

## Ne öğrendik?
- **Detay + format + kısıt** birlikte kullanıldığında kalite ve tekrarlanabilirlik artıyor.
- **Few-shot** üslubu standardize eder.  
- **Rol** tondaki sapmaları azaltır.  
- **Kısa** hızlıdır ama güvenlik/formatı unutabilir.
- **Kısıtlar** hallucination ve abartılı dil riskini düşürür.

> **Güvenlik/Gizlilik hatırlatması:** Kişisel veri (telefon, TC, e‑posta, özel müşteri içeriği) koyma. Gerekirse `[KİŞİSEL VERİ MASKELEME]` kullan.