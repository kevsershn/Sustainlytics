# Sustainlytics MVP Kapsami ve Basari Kriterleri

## 1) Amac ve Problem Tanimi

Sustainlytics'in MVP hedefi:
- KOBI ve startup'larin belirli bir butce siniri icinde daha dusuk karbon etkili tedarikcileri hizli bulmasini saglamak.
- Tuketici tarafinda bir sirketin surdurulebilirlik guvenilirligini tek ekranda gostermek.

MVP'in basari tanimi:
- Karar surelerini kisaltmak (hizli sonuc).
- Maliyet-cevre dengesinde olculebilir iyilesme saglamak.
- Greenwashing riskini algilanabilir bir guven skoruna cevirmek.

## 2) MVP Persona ve Ana Senaryolar

### Persona A: Satin Alma Sorumlusu
- Ihtiyac: "Belli butceyi asmadan en yesil secenegi bul."
- Basari ciktilari:
  - En uygun 3 tedarikciyi karsilastirmali gormek.
  - Karbon, fiyat, lojistik ve sertifika puanlarini tek tabloda incelemek.

### Persona B: Bilincli Tuketici
- Ihtiyac: "Bu sirketin surdurulebilirlik beyanina guvenebilir miyim?"
- Basari ciktilari:
  - Sirket ismiyle hizli sorgu.
  - 1-100 Guven Skoru + kisa aciklama.

## 3) MVP'e Dahil Olan Ozellikler (IN)

1. Dashboard girdi akisi
   - Butce araligi girisi.
   - "Maliyet <-> Surdurulebilirlik" slider dengesi.
   - Kategori/tedarik turu secimi (minimum 1 kategori).

2. AI destekli tedarikci skorlama ve optimizasyon
   - Girdiler: birim fiyat, tahmini karbon emisyonu, lojistik mesafe/rota, sertifika varligi.
   - Cikti: "En Uygun 3 Tedarikci" listesi.
   - Aciklanabilirlik: Her aday icin skor bilesenlerinin dagilimi.

3. Sonuc paneli
   - 3 tedarikcinin yan yana karsilastirmasi.
   - "Neden bu secim?" ozet kutusu.

4. Tuketici sorgu ekrani
   - Sirket adiyla arama.
   - Guven Skoru (1-100) + risk bayraklari (ornek: tutarsiz beyan, eksik kanit).

5. Dokuman tabanli veri alim (MVP seviyesinde)
   - PDF yukleme.
   - OCR ile metin cikarma.
   - Temel alan cikarimi (sertifika adi, rapor yili, emisyon ifadeleri).

## 4) MVP Disinda Kalanlar (OUT)

- Gercek zamanli IoT/saha verisi entegrasyonlari.
- Gelismis tedarik sozlesmesi yonetimi.
- Ulke bazli tum regülasyonlarin otomatik hukuki yorumu.
- Cok dilli gelismis raporlama (MVP'de tek dil yeterli).
- Mobil native uygulama (once web tabanli MVP).

## 5) Neden Bu Kapsam?

- En yuksek degeri en kisa surede ureten cekirdek akis korunur:
  1) Butce + tercih gir,
  2) optimize edilmis tedarikci onerisi al,
  3) guven skorunu dogrula.
- Uretime cikis riskini azaltmak icin veri kalitesi ve aciklanabilirlik MVP'nin merkezine alinir.

## 6) Teknik Basari Metrikleri (MVP KPI)

1. Hiz KPI
   - Kurumsal sorgu: p95 <= 60 saniye.
   - Tuketici sorgusu: p95 <= 30 saniye.

2. Kalite KPI
   - Top 3 oneri icinde butce ihlali orani <= %3.
   - Eksik/hatali veri nedeniyle sonucsuz kalan istek orani <= %5.

3. Etki KPI
   - Referans secime gore tahmini karbon azalimi >= %15.
   - Maliyet artis limiti <= %5 (ortalama senaryoda).

4. Guven KPI
   - Guven Skoru hesaplamasinda aciklama uretme orani = %100.
   - Sorgularda "kaynak gosterimi mevcut" orani >= %95.

## 7) Kabul Kriterleri (Definition of Done - MVP)

Bir MVP surumunun "hazir" sayilmasi icin:

1. Fonksiyonel
   - Dashboard, Sonuc Paneli, Tuketici Sorgu akislari kesintisiz calisir.
   - En az 1 veri setinde 3 tedarikci karsilastirmasi basariyla uretilir.

2. AI/Analitik
   - Skorlama formulu dokumante edilmis ve parametreleri versiyonlanmistir.
   - Greenwashing denetimi en az 3 risk bayragi turunu ayirt eder.

3. Performans
   - KPI hedefleri test ortaminda dogrulanmistir (p95 bazli).

4. Guvenlik ve Izlenebilirlik
   - Her sorgu icin audit log olusur.
   - Hata durumlarinda kullaniciya anlasilir geri bildirim verilir.

## 8) MVP Release Gate'leri

Release oncesi zorunlu kapilar:

1. Veri kapisi
   - En az 1 pilot sektorde yeterli tedarikci verisi.

2. Model kapisi
   - Skor dagilimlari manuel kontrolle tutarlidir.
   - Asiri sapma/sasirtici sonuc oranlari kabul limitinde.

3. Urun kapisi
   - Kritik akislarda engelleyici bug sayisi = 0.

4. Is kapisi
   - Pilot musteri demo senaryolari kesintisiz tamamlanir.

## 9) Sonraki Gorev Baglantisi

Bir sonraki adim `docs/02_DOMAIN_GLOSSARY.md`:
- Terim birligi,
- Veri sozlesmesi,
- Skorlama degiskenlerinin net tanimi.
