# Sustainlytics - Gelistirme Gorev Listesi

Bu gorev listesi, PRD'deki hedefleri adim adim hayata gecirmek icin MVP odakli bir yol haritasi sunar.

## 0) Proje Kurulumu ve Temel Altyapi
- [ ] Repo yapisini netlestir (`frontend`, `backend`, `ai`, `data`, `infra`).
- [ ] Ortak kod standartlarini tanimla (lint, format, commit kurali, klasor konvansiyonu).
- [ ] Ortam degiskenlerini ve `.env.example` dosyasini olustur.
- [ ] Temel CI is akisini kur (test + lint + build).
- [ ] Ilk teknik dokumantasyonu olustur (`README`, kurulum adimlari, calistirma komutlari).

## 1) Veri Modeli ve Kaynak Entegrasyonlari
- [ ] Tedarikci veri modeli tasarla:
  - fiyat, karbon emisyonu, lojistik rota, sertifikalar, guven skoru alanlari.
- [ ] Sirket raporu ve urun bilgisi icin veri giris formatlarini tanimla (JSON/PDF/OCR sonucu).
- [ ] OCR/PDF parser modulunu sec ve entegrasyon prototipini yap.
- [ ] Veri dogrulama katmani ekle (eksik/veri tipi hatasi kontrolleri).
- [ ] Ornek seed veri seti olustur (en az 20 tedarikci, farkli maliyet/karbon profilleri).

## 2) AI Modulu - Akilli Tedarikci Analizi
- [ ] AI girdi sozlesmesini tanimla (hangi metrikler, hangi agirliklarla islenecek).
- [ ] Karbon + maliyet + lojistik + sertifika puanlama algoritmasi gelistir.
- [ ] "En Ekonomik", "En Yesil", "Dengeli" olmak uzere 3 onerme modu uret.
- [ ] Sonuc aciklanabilirligi ekle (neden bu 3 tedarikci secildi?).
- [ ] Ilk benchmark testlerini yaz (dogruluk, sure, tutarlilik).

## 3) AI Modulu - Greenwashing Denetimi
- [ ] Rapor tarama pipeline'i olustur (metin cikarma + iddia tespiti).
- [ ] Supheli soylem/sahte iddia siniflandirma mantigini kur.
- [ ] 1-100 arasi "Guven Skoru" hesaplama modelini tanimla.
- [ ] Skor aciklamasini ureten katman ekle (kritik bulgular, riskli ifadeler).
- [ ] Dogrulama seti ile modelin yanlis pozitif/negatif oranini olc.

## 4) Backend API Gelistirme
- [ ] Kimlik dogrulama ve yetkilendirme (isletme vs tuketici rolleri) ekle.
- [ ] Dashboard icin optimizasyon endpoint'i yaz:
  - girdi: butce araligi + maliyet/surdurulebilirlik slider degeri
  - cikti: en uygun 3 tedarikci ve metrikleri
- [ ] Tuketici sorgu endpoint'i yaz:
  - girdi: sirket adi
  - cikti: surdurulebilirlik karnesi + guven skoru
- [ ] PDF/OCR dosya yukleme endpoint'i ve asenkron isleme kuyrugu ekle.
- [ ] API performans limitleri, hata yonetimi ve loglama altyapisini tamamla.

## 5) Frontend UI Gelistirme
- [ ] **Ana Dashboard** ekranini olustur:
  - butce min/max girdi alanlari
  - "Maliyet mi/Surdurulebilirlik mi?" slideri
  - optimizasyonu baslat butonu
- [ ] **Sonuc Paneli** ekranini olustur:
  - AI tarafindan secilen 3 tedarikciyi yanyana karsilastirma
  - karbon, maliyet, sertifika, guven skoru gorselleri
- [ ] **Tuketici Sorgu** ekranini olustur:
  - sirket adi arama
  - hizli karne ve guven skoru gosterimi
- [ ] Yukleniyor, bos durum, hata durumlari ve geri bildirim mesajlarini tasarla.
- [ ] Mobil uyumluluk ve temel erisilebilirlik gereksinimlerini uygula.

## 6) Performans ve Basari Metrikleri
- [ ] Sirket sorgularinda sonuc suresini `< 60 sn` hedefiyle olc.
- [ ] Tuketici sorgularinda sonuc suresini `< 30 sn` hedefiyle olc.
- [ ] Toplu test senaryolariyla sistem darbohazlarini belirle.
- [ ] Cache ve asenkron isleme ile gecikme iyilestirmeleri yap.
- [ ] KPI paneli ekle:
  - karbon azalimi yuzdesi
  - maliyet degisimi yuzdesi
  - kullanici bazli ortalama sorgu suresi

## 7) Denge Hedefi Dogrulama (Is Degeri)
- [ ] "Karbon ayak izi %15 azalirken maliyet artisi %5'i gecmesin" kuralini hesaplayan rapor katmani yaz.
- [ ] Farkli sektorler icin simule test senaryolari olustur.
- [ ] KPI hedefleri tutmayan durumlar icin AI agirlik ayarini optimize et.
- [ ] Sonuclari is birimi tarafinda anlasilir bir formatta sun (yonetici ozeti).

## 8) Guvenlik, Uyumluluk ve Kalite
- [ ] Hassas veri maskeleme ve erisim loglarini etkinlestir.
- [ ] Dosya yukleme guvenlik kontrolleri ekle (dosya tipi, boyut, malware taramasi).
- [ ] Unit, integration ve E2E test kapsamlarini tamamla.
- [ ] Temel guvenlik taramalari (dependency, SAST) CI'a bagla.
- [ ] Uretim ortami icin izleme/uyari mekanizmalarini aktif et.

## 9) Yayina Alma ve MVP Cikis
- [ ] Staging ortamini canliya benzer sekilde hazirla.
- [ ] Pilot musteri grubu ile UAT (kabul testi) yap.
- [ ] Kritik geri bildirimleri onceliklendirip MVP duzeltmelerini tamamla.
- [ ] V1 release notlarini ve kullanici kilavuzunu yayinla.
- [ ] Post-launch izleme plani ve sonraki sprint backlog'unu olustur.

## 10) Ilk Sprint Onerisi (Hizli Baslangic)
- [ ] **Sprint 1:** Altyapi + veri modeli + temel dashboard iskeleti
- [ ] **Sprint 2:** Optimizasyon AI v1 + sonuc paneli
- [ ] **Sprint 3:** Greenwashing skoru + tuketici sorgu ekrani
- [ ] **Sprint 4:** Performans hedefleri + test + MVP hardening
