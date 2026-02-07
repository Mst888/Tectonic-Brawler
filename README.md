<div align="center">

# 🤖 Tectonic Brawler Discord Bot

### *Modern, Akıllı ve Güçlü Discord Botu*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.4+-blue.svg)](https://github.com/Rapptz/discord.py)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

**AI Destekli Sohbet** • **YouTube Bildirimleri** • **Otomatik Karşılama** • **Admin Araçları**

[🚀 Hızlı Başlangıç](#-hızlı-başlangıç) • [✨ Özellikler](#-özellikler) • [📖 Dokümantasyon](#-dokümantasyon) • [🎮 Komutlar](#-bot-komutları)

---

</div>

## 🌟 Neden Tectonic Brawler?

Tectonic Brawler, Discord sunucunuz için **yapay zeka destekli**, **tam otomatik** ve **kullanımı kolay** bir bot çözümüdür. Groq AI teknolojisi ile anlık cevaplar, YouTube entegrasyonu ile otomatik bildirimler ve kapsamlı yönetim araçları sunar.

## 🚀 Hızlı Başlangıç

### ⚡ En Kolay Yol: Tek EXE Dosyası!

```bash
# 1. TectonicBrawler.exe (ÖNERİLEN) ⭐
dist\TectonicBrawler.exe
# ✅ Tek dosya - Taşınabilir
# ✅ Görsel arayüz
# ✅ Otomatik kurulum
# ✅ Tüm özellikler dahil
```

### 🎯 Alternatif Yöntemler

```bash
# 2. Python ile GUI Launcher
python scripts\gui_launcher.py

# 3. Basit BAT Dosyası
scripts\start_bot.bat

# 4. Manuel Başlatma
venv\Scripts\activate
python main.py
```

> 💡 **İlk kez mi kullanıyorsun?** → [`docs/KURULUM.md`](docs/KURULUM.md) dosyasına göz at!
> 
> 🎨 **GUI Launcher Rehberi** → [`docs/GUI_LAUNCHER.md`](docs/GUI_LAUNCHER.md)

---

## ✨ Özellikler

<table>
<tr>
<td width="50%">

### 🤖 AI Destekli Sohbet

- **Groq AI** ile hızlı ve akıllı cevaplar
- Mention ile veya `!ask` komutuyla kullanım
- Otomatik rate limiting (dakikada 5 istek)
- Uzun cevaplar için otomatik bölme
- Türkçe ve İngilizce destek

</td>
<td width="50%">

### 📺 YouTube Entegrasyonu

- Yeni video yüklemelerini otomatik takip
- Anlık Discord bildirimleri
- Çift bildirim önleme sistemi
- 10 dakikada bir kontrol
- Özelleştirilebilir bildirim kanalı

</td>
</tr>
<tr>
<td width="50%">

### 👋 Üye Karşılama Sistemi

- Yeni üyelere otomatik hoş geldin mesajı
- Ayrılan üyeler için veda mesajı
- Özelleştirilebilir mesaj formatları
- Kanal bazlı yapılandırma

</td>
<td width="50%">

### ⚙️ Güçlü Admin Araçları

- Discord üzerinden tam kontrol
- Sadece yöneticilere özel komutlar
- Kalıcı yapılandırma depolama
- Kolay kurulum ve yönetim

</td>
</tr>
</table>

---

## 🎮 Bot Komutları

### 👑 Admin Komutları

| Komut | Açıklama | Örnek |
|-------|----------|-------|
| `!setwelcome` | Hoş geldin kanalını ayarla | `!setwelcome #hoşgeldin` |
| `!setleave` | Veda kanalını ayarla | `!setleave #görüşürüz` |
| `!setyoutubechannel` | YouTube bildirim kanalı | `!setyoutubechannel #videolar` |
| `!setyoutubeid` | İzlenecek YouTube kanalı | `!setyoutubeid UC_x5XG1OV2P6uZZ5FSM9Ttw` |
| `!config` | Mevcut ayarları görüntüle | `!config` |

### 💬 Kullanıcı Komutları

| Komut | Açıklama | Örnek |
|-------|----------|-------|
| `!ask` | AI'ya soru sor | `!ask Python nedir?` |
| `@BotName` | Mention ile soru sor | `@TectonicBrawler Nasıl kod yazarım?` |

---

## 📋 Gereksinimler

- ✅ Python 3.10+
- ✅ Discord Bot Token
- ✅ YouTube Data API Key
- ✅ Groq API Key

## 📖 Dokümantasyon

| Dosya | İçerik |
|-------|--------|
| 📘 [`docs/KURULUM.md`](docs/KURULUM.md) | Detaylı kurulum rehberi |
| 🚀 [`HIZLI_BASLANGIÇ.md`](HIZLI_BASLANGIÇ.md) | 3 adımda başlangıç |
| 🎨 [`docs/GUI_LAUNCHER.md`](docs/GUI_LAUNCHER.md) | Görsel arayüz kullanımı |
| 📖 [`docs/NASIL_KULLANILIR.md`](docs/NASIL_KULLANILIR.md) | Kullanım kılavuzu |
| 🏗️ [`PROJE_YAPISI.md`](PROJE_YAPISI.md) | Proje yapısı ve organizasyon |
| 🔧 [`docs/BUILD_ADVANCED_EXE.md`](docs/BUILD_ADVANCED_EXE.md) | EXE oluşturma rehberi |

---

## 🔑 API Anahtarları Nasıl Alınır?

<details>
<summary><b>🔵 Discord Bot Token</b></summary>

1. [Discord Developer Portal](https://discord.com/developers/applications) adresine git
2. "New Application" butonuna tıkla
3. "Bot" sekmesine geç
4. "Reset Token" ile token'ı kopyala
5. **Privileged Gateway Intents** aktif et:
   - ✅ Server Members Intent
   - ✅ Message Content Intent
6. Bot'u sunucuna davet et (OAuth2 > URL Generator)

</details>

<details>
<summary><b>🔴 YouTube Data API Key</b></summary>

1. [Google Cloud Console](https://console.cloud.google.com/) aç
2. Yeni proje oluştur
3. "YouTube Data API v3" etkinleştir
4. "Credentials" > "Create Credentials" > "API Key"
5. API Key'i kopyala

</details>

<details>
<summary><b>🟢 Groq API Key</b></summary>

1. [Groq Console](https://console.groq.com) aç
2. Kayıt ol veya giriş yap
3. "API Keys" bölümüne git
4. "Create API Key" tıkla
5. API Key'i kopyala

</details>

---

## 📁 Proje Yapısı

```
Tectonic-Brawler/
├── 📄 main.py                  # Ana bot dosyası
├── 📄 .env                     # API anahtarları
├── 📄 config.json              # Bot yapılandırması
├── 📂 cogs/                    # Bot özellikleri
│   ├── ai.py                   # AI sohbet
│   ├── events.py               # Üye olayları
│   ├── youtube.py              # YouTube takip
│   └── admin.py                # Admin komutları
├── 📂 scripts/                 # Başlatıcılar
│   ├── start_bot.bat           # ← Bunu kullan!
│   └── advanced_launcher.py
├── 📂 dist/                    # EXE dosyaları
│   └── TectonicBrawlerLauncher.exe
└── 📂 docs/                    # Dokümantasyon
```

## 🔧 Sorun Giderme

<details>
<summary><b>Bot komutlara cevap vermiyor</b></summary>

- Discord Developer Portal'da **Message Content Intent** aktif mi kontrol et
- Bot'un sunucuda gerekli izinlere sahip olduğundan emin ol
- Komut prefix'inin `.env` dosyasıyla eşleştiğini kontrol et

</details>

<details>
<summary><b>AI özellikleri çalışmıyor</b></summary>

- Groq API anahtarının geçerli olduğunu kontrol et
- İnternet bağlantını test et
- `bot.log` dosyasını incele
- Rate limit aşılmış olabilir (dakikada 5 istek)

</details>

<details>
<summary><b>YouTube bildirimleri gelmiyor</b></summary>

- YouTube API anahtarının geçerli olduğunu doğrula
- YouTube kanal ID'sinin doğru olduğunu kontrol et
- Bildirim kanalının ayarlandığından emin ol
- Bot'un kanala mesaj gönderme izni var mı kontrol et

</details>

<details>
<summary><b>Bot çöküyor veya bağlantı kesiliyor</b></summary>

- `bot.log` dosyasını kontrol et
- Tüm API anahtarlarının geçerli olduğunu doğrula
- İnternet bağlantısının stabil olduğundan emin ol
- Python versiyonunun 3.10+ olduğunu kontrol et

</details>

## 🌐 7/24 Çalıştırma

### ☁️ Cloud Hosting Seçenekleri

| Platform | Zorluk | Ücretsiz Plan | Önerilen |
|----------|--------|---------------|----------|
| **Railway** | ⭐ Kolay | ✅ Var | ✅ Evet |
| **Heroku** | ⭐⭐ Orta | ⚠️ Sınırlı | ⚠️ Kısmen |
| **DigitalOcean** | ⭐⭐⭐ Zor | ❌ Yok | ✅ Evet |
| **AWS EC2** | ⭐⭐⭐ Zor | ✅ Var (1 yıl) | ⚠️ Kısmen |

### 💻 Windows Task Scheduler

1. `scripts\start_bot.bat` dosyasını kullan
2. Task Scheduler'ı aç
3. "Create Basic Task" seç
4. Başlangıçta çalışacak şekilde ayarla

### 🐧 Linux systemd

Detaylı talimatlar için [`docs/KURULUM.md`](docs/KURULUM.md) dosyasına bakın.

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

---

## 📊 İstatistikler

- 🤖 **AI Model:** Groq (llama-3.3-70b-versatile)
- ⚡ **Yanıt Süresi:** ~1-2 saniye
- 📺 **YouTube Kontrol:** Her 10 dakika
- 🔒 **Rate Limit:** Kullanıcı başına dakikada 5 istek
- 🐍 **Python:** 3.10+
- 📦 **Bağımlılıklar:** discord.py, aiohttp, python-dotenv

---

## 💡 İpuçları

- 🔐 `.env` dosyanızı **asla** paylaşmayın
- 📝 `bot.log` dosyasını düzenli kontrol edin
- 🔄 Bot'u güncel tutun
- 💾 Düzenli yedekleme yapın
- 🌐 Stabil internet bağlantısı kullanın

---

## 📜 Lisans

Bu proje eğitim ve kişisel kullanım için sağlanmıştır.

---

<div align="center">

### 🌟 Projeyi Beğendin mi?

⭐ **Star** vermeyi unutma!

**Yapımcı:** [Kodland](https://kodland.com) | **Bot:** Tectonic Brawler

*Discord sunucunuzu bir üst seviyeye taşıyın!* 🚀

</div>
