# 📁 Tectonic Brawler - Proje Yapısı

## Klasör Organizasyonu

```
Tectonic-Brawler/
│
├── 📄 main.py                      # Ana bot dosyası
├── 📄 config.json                  # Bot yapılandırması
├── 📄 requirements.txt             # Python bağımlılıkları
├── 📄 .env                         # API anahtarları (GİZLİ - paylaşma!)
├── 📄 README.md                    # Proje açıklaması
├── 📄 bot.log                      # Bot log dosyası
│
├── 📂 cogs/                        # Bot komutları ve özellikleri
│   ├── ai.py                       # AI sohbet özellikleri
│   ├── events.py                   # Discord event handler'ları
│   ├── youtube.py                  # YouTube bildirimleri
│   └── admin.py                    # Admin komutları
│
├── 📂 utils/                       # Yardımcı araçlar
│   └── config_manager.py           # Yapılandırma yöneticisi
│
├── 📂 docs/                        # Dokümantasyon
│   ├── KURULUM.md                  # Kurulum rehberi
│   ├── NASIL_KULLANILIR.md         # Kullanım kılavuzu
│   ├── BUILD_EXE.md                # Basit EXE oluşturma
│   └── BUILD_ADVANCED_EXE.md       # Gelişmiş EXE oluşturma
│
├── 📂 scripts/                     # Yardımcı scriptler
│   ├── start_bot.bat               # Basit başlatıcı (ÖNERİLEN)
│   ├── launcher.py                 # Basit Python launcher
│   ├── advanced_launcher.py        # Otomatik kurulum launcher
│   └── create_icon.py              # İkon oluşturucu
│
├── 📂 build_tools/                 # Build araçları
│   ├── bot_icon.ico                # Bot ikonu
│   └── TectonicBrawlerLauncher.spec # PyInstaller spec dosyası
│
├── 📂 dist/                        # Derlenmiş EXE dosyaları
│   └── TectonicBrawlerLauncher.exe # Ana launcher EXE
│
├── 📂 build/                       # PyInstaller build dosyaları (geçici)
│
└── 📂 venv/                        # Python virtual environment

```

## 🚀 Hızlı Başlangıç

### Yöntem 1: BAT Dosyası (En Kolay)
```bash
scripts\start_bot.bat
```

### Yöntem 2: EXE Launcher (Otomatik Kurulum)
```bash
dist\TectonicBrawlerLauncher.exe
```

### Yöntem 3: Manuel
```bash
venv\Scripts\activate
python main.py
```

## 📚 Dokümantasyon

- **Kurulum:** `docs/KURULUM.md`
- **Kullanım:** `docs/NASIL_KULLANILIR.md`
- **EXE Oluşturma:** `docs/BUILD_ADVANCED_EXE.md`

## 🔧 Geliştirme

### Yeni Özellik Ekleme
1. `cogs/` klasöründe yeni bir `.py` dosyası oluştur
2. `commands.Cog` sınıfından türet
3. `main.py` içinde cog'u yükle

### Log Kontrol
```bash
type bot.log
```

## 🗂️ Önemli Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `main.py` | Bot'un ana giriş noktası |
| `.env` | API anahtarları (GİZLİ!) |
| `config.json` | Bot ayarları |
| `requirements.txt` | Python bağımlılıkları |
| `cogs/*.py` | Bot özellikleri ve komutları |

## 🔒 Güvenlik

⚠️ **Asla paylaşma:**
- `.env` dosyası
- `bot.log` (token içerebilir)
- `config.json` (hassas bilgiler içerebilir)

## 🧹 Temizlik

Gereksiz dosyaları temizlemek için:
```bash
# Build dosyalarını sil
rmdir /s /q build

# Log dosyasını temizle
del bot.log

# Python cache'i temizle
rmdir /s /q __pycache__
```

## 📦 Yedekleme

Yedeklenmesi gereken dosyalar:
- ✅ `.env`
- ✅ `config.json`
- ✅ `cogs/`
- ✅ `utils/`
- ✅ `main.py`

Yedeklenmemesi gereken:
- ❌ `venv/`
- ❌ `build/`
- ❌ `dist/`
- ❌ `__pycache__/`
- ❌ `bot.log`
