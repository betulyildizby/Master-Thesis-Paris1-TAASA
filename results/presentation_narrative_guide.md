# T-AASA vs. SDMAE: Main Research Question & Defense Presentation Guide

**Ana Araştırma Sorunuz (Main Research Question):**  
> *"In what ways can sentiment-based review analysis support trend detection and decision-making processes in e-commerce?"*  
> *(Duygu odaklı yorum analizi, e-ticarette trend tespitini ve karar verme süreçlerini hangi yollarla destekleyebilir?)*

---

## 🎬 1. BÖLÜM: PROBLEM VE ANA ARAŞTIRMA SORUSUNUN SUNUMU

### 📌 Sunum Metni / Konuşma Akışı:
> "Hocam, tezimizin temel araştırma sorusu şudur: **'Duygu odaklı yorum analizi, e-ticarette trend tespitini ve karar verme süreçlerini hangi yollarla destekleyebilir?'**
> 
> Geleneksel e-ticaret platformları kararlarını statik yıldız ortalamalarına ($R_{base}$) dayandırır. Ancak yıldız puanları zaman körüdür (5 yıl önceki yorumla dünkü yorumu bir tutar) ve trend körüdür (piyasadaki veya kullanıcıdaki özellik önceliklerini görmez).
> 
> Geliştirdiğimiz **T-AASA (Trend-Aware Aspect Sentiment Alignment)** modeli ile SDMAE baseline'ını entegre ederek, duygu analizinin e-ticarette karar vermeyi **3 somut yolla** desteklediğini kanıtladık."

---

## 🔬 2. BÖLÜM: ANA SORUNUN 3 TEMEL CEVABI (3 PILLARS OF DECISION SUPPORT)

### 📌 Sunum Metni / Konuşma Akışı:
> "Duygu odaklı yorum analizi, karar verme süreçlerini şu 3 ana mekanizmayla destekler:
>
> 1. **1. Yol - Piyasa Trend Hızının Tespiti ($T_k$ Çarpanı):**
>    - Yorum metinlerindeki duygu ve bahsedilme sıklığı zaman boyutunda incelenerek trendler otomatik tespit edilir.
>    - *Deney Bulgumuz:* Batarya (`battery`) konusundaki bahsedilme hızı son 1 yılda **%8.93 artmış ($\text{Velocity}=1.0893$)** ve $T_k=1.134$ trend çarpanı tetiklenmiştir. Kamera ve fiyat gibi düşüşteki özellikler nötr kalmıştır.
>
> 2. **2. Yol - 'Yıldız Puanı Tuzağını' Aşmak (Zamansal Aşınma $e^{-\lambda \Delta t}$):**
>    - Yüksek genel yıldıza sahip ancak son zamanlarda kalitesi düşmüş ürünler tespit edilerek alıcının yanlış karar vermesi önlenir.
>    - *Deney Bulgumuz:* **Product_D** ürünü 4.42 genel yıldıza sahipti ve SDMAE'de 1. sıradaydı. Ancak son yorumlardaki batarya memnuniyetsizliği ($S=0.100$) tespit edilerek **3. sıraya düşürülmüştür.**
>
> 3. **3. Yol - Kullanıcı Tercihleri ile Aspect Sentimeti Hizalamak ($W_{u,k}$):**
>    - Ürün yorumları aspect seviyesinde ayrıştırılır ve kullanıcının kişisel önem matrisi ile eşleştirilir.
>    - *Deney Bulgumuz:* **Product_B** ürünü 4.24 yıldız ile SDMAE'de 4. sıradaydı. Ancak batarya ve ses aspect'lerindeki yüksek sentiment skoru sayesinde **1. sıraya yükseltilmiştir.**"

---

## 📊 3. BÖLÜM: ANA SORUYA İLİŞKİN SAYISAL KANITLAR TABLOSU

### 📌 Sunum Metni / Konuşma Akışı:
> "Duygu analizinin karar vermedeki üstünlüğü, `results/taasa_vs_sdmae_quantitative_metrics.csv` dosyasındaki şu verilerle kanıtlanmıştır:

| Karar Destek Metriği | Orijinal SDMAE | Tasarlanan T-AASA | **Fark / Kazanım Oranı (%)** | Karar Vermeye Katkısı |
| :--- | :---: | :---: | :---: | :--- |
| **Top-1 Öneri Aspect Memnuniyeti** | `0.1621` | `0.2382` | **+%46.95 daha iyi** | Kullanıcı beklentisini karşılayan ürünü %46.95 daha yüksek doğrulukla bulur. |
| **Top-2 Öneri Ortalama Uyum** | `0.1643` | `0.2190` | **+%33.32 daha iyi** | Alternatif ürün önerilerinin kalitesini artırır. |
| **Manuel Okuma (Verification) Uyumu** | `%20.0` | `%90.0` | **+%350.0 bağıl kazanç** | Yorumlardaki gerçek duygu durumuyla %90 oranında tam eşleşir. |
| **Yanıltıcı Sıralama Düzeltme Oranı** | `%0.0` | `%100.0` | **%100 Dinamik Düzeltme** | Statik yıldız tuzaklarının tamamını (%100) ortadan kaldırır. |

---

## 🎯 4. BÖLÜM: TEZ KAPANIŞ CÜMLESİ (DIRECT CONCLUSION TO MAIN RQ)

### 📌 Sunum Metni / Konuşma Akışı:
> *"Özetle Hocam; 'Duygu odaklı yorum analizi, e-ticarette trend tespitini ve karar verme süreçlerini hangi yollarla destekleyebilir?' sorusunun cevabı şudur:*
> 
> *Duygu analizi; ham müşteri yorumlarını zaman boyutunda işleyerek (1) anlık piyasa trendlerini otomatik algılar ($T_k=1.134$), (2) eski yıldız puanlarının yanıltıcılığını engeller (%100 sıralama düzeltmesi) ve (3) kullanıcı tercihlerine özel dinamik öneriler sunarak karar verme kalitesini **%46.95 oranında** artırır."*
