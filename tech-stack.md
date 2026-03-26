# Sustainlytics Teknoloji Yığını (Tech Stack) 🛠️

Bu projede, karmaşık kurulumlarla vakit kaybetmeden doğrudan sonuca odaklanmak için "en düşük bariyerli" araçlar seçilmiştir.

## 1. Önerilen Teknoloji Yığını
* **Dil:** Python (Veri analizi ve AI entegrasyonu için en kolay dil).
* **Arayüz (UI):** Streamlit (Sadece Python bilerek, HTML/CSS ile uğraşmadan profesyonel web panelleri oluşturmayı sağlar).
* **Yapay Zeka:** Gemini API (Google AI Studio).
* **Editör:** Cursor AI (Yapay zeka desteğiyle kod yazan, hataları otomatik düzelten editör).
* **Yayına Alma (Deploy):** Streamlit Cloud veya Lovable (Tek tıkla internete açmak için).

## 2. Neden Bu Teknolojileri Seçiyoruz?
* **Hız:** Streamlit sayesinde frontend (görünüm) yazmak haftalar değil, dakikalar sürer.
* **Öğrenme Eğrisi:** Python'ın okunabilirliği yüksektir, başlangıç seviyesi için idealdir.
* **Ücretsiz ve Güçlü:** Google AI Studio ve Gemini API, Buildathon süreci için tamamen ücretsiz ve son derece yeteneklidir.
* **Hata Yönetimi:** Cursor AI, başlangıç seviyesindeki hataları senin yerine analiz eder ve düzeltir.

## 3. Kurulum Adımları (Adım Adım)

### Adım 1: Python Yükle
Eğer yüklü değilse [python.org](https://www.python.org/) adresinden güncel sürümü indir ve yüklerken "Add Python to PATH" kutucuğunu işaretle.

### Adım 2: Cursor AI Kurulumu
[cursor.com](https://cursor.com/) adresinden editörü indir. GitHub hesabını bağla.

### Adım 3: Gerekli Kütüphaneleri Yükle
Cursor terminalini aç (Ctrl+J veya Cmd+J) ve şu komutu yaz:
`pip install streamlit google-generativeai python-dotenv`

### Adım 4: API Anahtarını Güvenliğe Al
Proje klasöründe `.env` isimli bir dosya oluştur ve içine anahtarını yapıştır:
`GEMINI_API_KEY=senin_api_anahtarın_buraya`

### Adım 5: İlk Çalıştırma
Cursor terminalinde proje klasörüne geç ve uygulamayı başlat:
`streamlit run app.py`

Tarayıcıda otomatik açılmazsa şu adrese git:
`http://localhost:8501`
