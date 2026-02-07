# 🔧 Sorun Giderme Rehberi

## ❌ Virtual Environment Oluşturulamıyor

### Sorun
EXE çalıştırıldığında "Virtual environment oluşturulamadı" hatası alınıyor.

### Çözüm
Bu sorun düzeltildi! Yeni `TectonicBrawler.exe` versiyonu:
- ✅ Sistem Python'unu otomatik bulur
- ✅ Windows Registry'den Python yolunu okur
- ✅ Fallback olarak PATH'i kontrol eder
- ✅ Detaylı hata mesajları gösterir

### Eğer Hala Sorun Yaşıyorsan:

1. **Python'un kurulu olduğundan emin ol:**
   ```bash
   python --version
   ```
   Python 3.10+ olmalı

2. **Python PATH'e ekli mi kontrol et:**
   - Başlat menüsünde "python" yaz
   - Python açılıyorsa PATH'e ekli

3. **Manuel Python kurulumu:**
   - [python.org](https://www.python.org/downloads/) adresinden indir
   - Kurulumda "Add Python to PATH" seçeneğini işaretle

---

## 📦 Paketler Yüklenemiyor

### Sorun
"Paketler yüklenemedi" veya "pip bulunamadı" hatası.

### Çözüm

1. **İnternet bağlantını kontrol et**
2. **Güvenlik duvarını kontrol et** (pip'in internete erişmesine izin ver)
3. **Antivirüs programını kontrol et** (bazen pip'i engelleyebilir)

---

## 🔐 API Anahtarları Çalışmıyor

### Sorun
Bot başlatılıyor ama Discord'a bağlanmıyor veya AI çalışmıyor.

### Çözüm

1. **Discord Token:**
   - [Discord Developer Portal](https://discord.com/developers/applications) kontrol et
   - Token'ı yeniden oluştur
   - Message Content Intent aktif mi kontrol et

2. **Groq API Key:**
   - [Groq Console](https://console.groq.com) kontrol et
   - API key'in geçerli olduğundan emin ol
   - Kota aşılmış olabilir

3. **Ayarları yeniden gir:**
   - ⚙ Ayarlar butonuna tıkla
   - API anahtarlarını yeniden gir
   - Kaydet

---

## 🚫 EXE Açılmıyor

### Sorun
TectonicBrawler.exe çift tıklandığında hiçbir şey olmuyor.

### Çözüm

1. **Antivirüs kontrolü:**
   - Antivirüs programın EXE'yi engelliyor olabilir
   - EXE'yi güvenilir listesine ekle

2. **Windows Defender SmartScreen:**
   - "Daha fazla bilgi" tıkla
   - "Yine de çalıştır" seç

3. **Yönetici olarak çalıştır:**
   - EXE'ye sağ tıkla
   - "Yönetici olarak çalıştır" seç

---

## 📁 Dosyalar Nerede?

### Sorun
Bot dosyalarını bulamıyorum.

### Cevap
TectonicBrawler.exe çalıştırıldığında dosyalar şuraya kopyalanır:
```
C:\Users\[kullanıcı_adın]\TectonicBrawler\
```

Bu klasörde bulacakların:
- `main.py` - Ana bot dosyası
- `cogs/` - Bot özellikleri
- `utils/` - Yardımcı araçlar
- `.env` - API anahtarları
- `venv/` - Virtual environment
- `bot.log` - Log dosyası

---

## 🔄 Bot Çöküyor

### Sorun
Bot başlıyor ama sonra çöküyor.

### Çözüm

1. **Log dosyasını kontrol et:**
   ```
   C:\Users\[kullanıcı_adın]\TectonicBrawler\bot.log
   ```

2. **Yaygın hatalar:**
   - **"Invalid Token"** → Discord token yanlış
   - **"Missing Intents"** → Discord Developer Portal'da intents aktif değil
   - **"API Error"** → Groq API key geçersiz veya kota aşıldı

3. **Bot'u yeniden başlat:**
   - ⏹ Bot'u Durdur
   - ▶ Bot'u Başlat

---

## 💻 Performans Sorunları

### Sorun
Bot yavaş çalışıyor veya donuyor.

### Çözüm

1. **Sistem gereksinimleri:**
   - En az 4GB RAM
   - İnternet bağlantısı stabil olmalı

2. **Çok fazla log:**
   - Log penceresini temizlemek için bot'u yeniden başlat

3. **Arka planda çok program:**
   - Gereksiz programları kapat

---

## 🆘 Hala Sorun Yaşıyorsan

1. **Log dosyasını kontrol et:**
   ```
   C:\Users\[kullanıcı_adın]\TectonicBrawler\bot.log
   ```

2. **Hata mesajını oku:**
   - GUI'deki log penceresinde renkli hata mesajları var
   - Kırmızı = Hata
   - Turuncu = Uyarı

3. **Temiz kurulum:**
   - `C:\Users\[kullanıcı_adın]\TectonicBrawler\` klasörünü sil
   - EXE'yi yeniden çalıştır
   - Her şey sıfırdan kurulacak

---

## 📞 İletişim

Sorun devam ediyorsa:
- Log dosyasını (`bot.log`) kaydet
- Hata mesajının ekran görüntüsünü al
- Destek için iletişime geç

---

**Son Güncelleme:** 5 Şubat 2026
