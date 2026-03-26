# Sustainlytics Kullanıcı Akışı (User Flow) 🔄

Bu belge, bir kullanıcının uygulamayı açtığı andan sonuç alana kadar takip edeceği adımları tanımlar.

## 🏢 Senaryo A: Şirket/Startup (Tedarikçi Optimizasyonu)

1. **Giriş:** Kullanıcı uygulamayı açar ve "İşletme Paneli" sekmesine tıklar.
2. **Parametre Girişi:**
    - Aradığı ham madde/hizmet türünü seçer.
    - Maksimum bütçesini rakam olarak girer.
    - "Öncelik Dengesi" sürgüsünü (Slider) ayarlar (Örn: %70 Maliyet, %30 Sürdürülebilirlik).
3. **AI Analiz Süreci:** "En Uygun Tedarikçiyi Bul" butonuna basar. AI, veri setindeki tedarikçileri bütçe ve karbon puanına göre skorlar.
4. **Sonuç:** Kullanıcıya "Maliyet Etkin", "En Çevreci" ve "Sustainlytics Önerisi (Dengeli)" başlıklarıyla 3 farklı kart sunulur.

---

## 🛒 Senaryo B: Bireysel Tüketici (Şirket Sorgulama)

1. **Giriş:** Kullanıcı ana sayfadaki "Şirket Puanı Sorgula" arama çubuğunu görür.
2. **Arama:** Sorgulamak istediği markanın adını yazar ve "Sorgula"ya tıklar.
3. **AI Doğrulama:** Gemini AI, markanın kamuya açık verilerini ve sürdürülebilirlik geçmişini anlık analiz eder.
4. **Sonuç:**
    - Şirketin 1-100 arası "Sustainlytics Güven Skoru" görüntülenir.
    - AI tarafından üretilen 3 maddelik kısa bir özet (Neden bu puanı aldı?) gösterilir.
    - "Yeşil Aklama (Greenwashing)" riski varsa kullanıcı bir uyarı ikonu ile bilgilendirilir.

---

## 🛠️ Teknik Akış (Arka Plan)
- **Input:** Kullanıcı verisi (Bütçe/Şirket adı).
- **Process:** Python algoritması filtreleme yapar + Gemini API metin analizi sağlar.
- **Output:** Optimize edilmiş liste veya şeffaf güven raporu.
