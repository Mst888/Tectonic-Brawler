# Tectonic Brawler Discord Bot - Kurulum Rehberi

Bu rehber, Discord botunu adım adım kurmak için gereken tüm işlemleri açıklar.

## Gereksinimler

- Python 3.10 veya üzeri
- Discord Bot Token
- YouTube Data API Key
- Groq API Key

---

## Adım 1: Python Kurulumu

1. [Python'un resmi sitesinden](https://www.python.org/downloads/) Python 3.10 veya üzeri sürümü indirin
2. Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin
3. Kurulumu tamamlayın
4. Terminalde `python --version` komutuyla kurulumu doğrulayın

---

## Adım 2: Proje Dosyalarını Hazırlama

1. Proje klasörüne gidin:
```bash
cd "yol\to\Tectonic Brawler"
```

2. Virtual environment oluşturun:
```bash
python -m venv venv
```

3. Virtual environment'ı aktif edin:
```bash
venv\Scripts\activate
```

4. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

---

## Adım 3: Discord Bot Oluşturma

1. [Discord Developer Portal](https://discord.com/developers/applications) adresine gidin
2. "New Application" butonuna tıklayın
3. Bot'a bir isim verin (örn: Tectonic Brawler)
4. Sol menüden "Bot" sekmesine gidin
5. "Reset Token" butonuna tıklayın ve token'ı kopyalayın
   - ⚠️ **ÖNEMLİ**: Bu token'ı güvenli bir yere kaydedin (örn: Not Defteri)
   - Bu token'ı daha sonra `.env` dosyasına yapıştıracaksınız
   - Token'ı kimseyle paylaşmayın!
6. Aşağıdaki ayarları açın:
   - **Privileged Gateway Intents** bölümünden:
     - ✅ Server Members Intent (üye katılma/ayrılma olayları için gerekli)
     - ✅ Message Content Intent (mesajları okumak için gerekli)

### Bot'u Sunucuya Davet Etme

1. Sol menüden "OAuth2" > "URL Generator" sekmesine gidin
2. **Scopes** bölümünden:
   - ✅ bot
   - ✅ applications.commands
3. **Bot Permissions** bölümünden:
   - ✅ Read Messages/View Channels
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Message History
   - ✅ Mention Everyone
   - ✅ Add Reactions
4. Alttaki URL'yi kopyalayın ve tarayıcıda açın
5. Bot'u eklemek istediğiniz sunucuyu seçin

---

## Adım 4: YouTube API Key Alma

1. [Google Cloud Console](https://console.cloud.google.com/) adresine gidin
2. Yeni bir proje oluşturun (örn: "Discord Bot")
3. Sol menüden "APIs & Services" > "Library" sekmesine gidin
4. "YouTube Data API v3" aratın ve etkinleştirin
5. "APIs & Services" > "Credentials" sekmesine gidin
6. "Create Credentials" > "API Key" seçin
7. Oluşturulan API Key'i kopyalayın
   - ⚠️ **ÖNEMLİ**: Bu key'i güvenli bir yere kaydedin
   - Bu key'i daha sonra `.env` dosyasına yapıştıracaksınız

### YouTube Kanal ID'sini Bulma

Bot'un hangi YouTube kanalını izleyeceğini belirlemek için kanal ID'sine ihtiyacınız var.

#### Yöntem 1: Kanal URL'sinden (En Kolay)

1. İzlemek istediğiniz YouTube kanalına gidin
2. Tarayıcınızın adres çubuğundaki URL'ye bakın
3. URL formatlarından birine göre ID'yi bulun:

**Format 1: /channel/ ile başlayan**
```
https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
                                 └─────────┬─────────┘
                                    Bu kısım kanal ID'si
```
- Kanal ID: `UC_x5XG1OV2P6uZZ5FSM9Ttw`

**Format 2: /c/ veya /@kullaniciadi ile başlayan**
```
https://www.youtube.com/@KanalAdi
veya
https://www.youtube.com/c/KanalAdi
```
Bu durumda Yöntem 2'yi kullanın.

#### Yöntem 2: Kanal Hakkında Sayfasından

1. YouTube kanalına gidin
2. "Hakkında" (About) sekmesine tıklayın
3. Sağ tarafta "Paylaş" butonunun altında "Kanal ID'sini kopyala" seçeneği var
4. Veya sayfanın en altında "Kanal ID" yazan kısmı bulun
5. ID'yi kopyalayın (genellikle `UC` ile başlar)

#### Yöntem 3: Sayfa Kaynağından

1. YouTube kanalına gidin
2. Sayfada sağ tıklayın > "Sayfa Kaynağını Görüntüle" (View Page Source)
3. `Ctrl + F` ile `"channelId"` aratın
4. `"channelId":"UC..."` şeklinde bir satır bulacaksınız
5. Tırnak işaretleri arasındaki ID'yi kopyalayın

#### Örnek Kanal ID'leri

- **MrBeast**: `UCX6OQ3DkcsbYNE6H8uQQuVA`
- **PewDiePie**: `UC-lHJZR3Gqxm24_Vd_AJ5Yw`
- **Türkçe bir kanal örneği**: `UCqjWOKOlh7dHRUVXoKk6WoQ`

⚠️ **NOT**: 
- Kanal ID'si genellikle `UC` ile başlar
- 24 karakter uzunluğundadır
- Harf, rakam, tire ve alt çizgi içerebilir

#### Bu ID'yi Ne Zaman Kullanacaksınız?

YouTube Kanal ID'sini **bot çalıştıktan sonra** Discord'da kullanacaksınız:

1. Bot'u çalıştırın (`python main.py`)
2. Discord sunucunuza gidin
3. Şu komutu yazın:
   ```
   !setyoutubeid BURAYA_KANAL_ID_YAPISIRIN
   ```
   **Örnek:**
   ```
   !setyoutubeid UCX6OQ3DkcsbYNE6H8uQQuVA
   ```

4. Bot bu kanalı her 10 dakikada bir kontrol edecek
5. Yeni video yüklendiğinde Discord'da bildirim gönderecek

💡 **Özet:** Şimdilik sadece ID'yi bulun ve bir yere not edin. Bot'u kurduktan sonra Discord'da kullanacaksınız.

---

## Adım 5: Groq API Key Alma

1. [Groq Console](https://console.groq.com) adresine gidin
2. Hesap oluşturun veya giriş yapın (ücretsiz)
3. Sol menüden "API Keys" sekmesine gidin
4. "Create API Key" butonuna tıklayın
5. Key'e bir isim verin (örn: "Discord Bot")
6. Oluşturulan API Key'i kopyalayın
   - ⚠️ **ÖNEMLİ**: Bu key'i güvenli bir yere kaydedin
   - Bu key'i daha sonra `.env` dosyasına yapıştıracaksınız
   - Key bir daha gösterilmeyecek, kaybederseniz yeni oluşturmanız gerekir

---

## Adım 6: .env Dosyası Oluşturma

Bu adımda, topladığınız tüm API key'leri bir dosyaya kaydedeceksiniz.

### Yöntem 1: Not Defteri ile Oluşturma (Önerilen)

1. Not Defteri'ni (Notepad) açın
2. Aşağıdaki içeriği kopyalayıp yapıştırın:

```env
# Discord Bot Token
DISCORD_TOKEN=buraya_discord_bot_tokeninizi_yapisirin

# YouTube Data API Key
YOUTUBE_API_KEY=buraya_youtube_api_keyinizi_yapisirin

# Groq API Key
GROQ_API_KEY=buraya_groq_api_keyinizi_yapisirin

# Groq API Ayarları
GROQ_API_BASE=https://api.groq.com/openai/v1
AI_MODEL=mixtral-8x7b-32768

# Bot Komut Öneki
COMMAND_PREFIX=!
```

3. **Kendi bilgilerinizi girin:**
   - `DISCORD_TOKEN=` yazan yerin sonuna Discord bot token'ınızı yapıştırın
   - `YOUTUBE_API_KEY=` yazan yerin sonuna YouTube API key'inizi yapıştırın
   - `GROQ_API_KEY=` yazan yerin sonuna Groq API key'inizi yapıştırın
   - Diğer satırları değiştirmeyin

4. **Dosyayı kaydedin:**
   - "Dosya" > "Farklı Kaydet" seçin
   - Proje klasörünüze gidin: `yol\to\Tectonic Brawler`
   - **Dosya adı**: `.env` (nokta ile başlamalı!)
   - **Dosya türü**: "Tüm Dosyalar (*.*)" seçin
   - **Kodlama**: UTF-8
   - "Kaydet" butonuna tıklayın

### Yöntem 2: .env.example Dosyasını Kopyalama

1. Proje klasöründeki `.env.example` dosyasını bulun
2. Sağ tıklayın ve "Kopyala" seçin
3. Aynı klasöre "Yapıştır" yapın
4. Yeni dosyayı `.env` olarak yeniden adlandırın
5. Dosyayı Not Defteri ile açın ve kendi API key'lerinizi girin

### Örnek Doldurulmuş .env Dosyası

```env
# Discord Bot Token
DISCORD_TOKEN=MTIzNDU2Nzg5MDEyMzQ1Njc4.GhIjKl.MnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUv

# YouTube Data API Key
YOUTUBE_API_KEY=AIzaSyAbCdEfGhIjKlMnOpQrStUvWxYz1234567

# Groq API Key
GROQ_API_KEY=gsk_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890AbCdEfGhIjKl

# Groq API Ayarları
GROQ_API_BASE=https://api.groq.com/openai/v1
AI_MODEL=mixtral-8x7b-32768

# Bot Komut Öneki
COMMAND_PREFIX=!
```

⚠️ **ÖNEMLİ UYARILAR:**
- `.env` dosyasını kimseyle paylaşmayın!
- Bu dosyayı GitHub'a yüklemeyin!
- Dosya adının başında nokta (`.`) olmalı!
- Eşittir işaretinden sonra boşluk bırakmayın!
- Tırnak işareti kullanmayın!

---

## Adım 7: Bot'u Çalıştırma

1. Virtual environment'ın aktif olduğundan emin olun:
```bash
venv\Scripts\activate
```

2. Bot'u başlatın:
```bash
python main.py
```

3. Terminal'de şu mesajı görmelisiniz:
```
INFO - TectonicBrawler has connected to Discord!
```

---

## Adım 8: Bot'u Yapılandırma

Discord sunucunuzda aşağıdaki komutları kullanarak bot'u yapılandırın:

### 1. Hoş Geldin Kanalını Ayarlama
```
!setwelcome #hosgeldin
```

### 2. Ayrılma Kanalını Ayarlama
```
!setleave #ayrilanlar
```

### 3. YouTube Bildirim Kanalını Ayarlama
```
!setyoutubechannel #youtube-bildirimleri
```

### 4. YouTube Kanal ID'sini Ayarlama
```
!setyoutubeid UC_x5XG1OV2P6uZZ5FSM9Ttw
```

### 5. Yapılandırmayı Kontrol Etme
```
!config
```

---

## Bot Komutları

### Admin Komutları (Sadece Yöneticiler)

| Komut | Açıklama | Kullanım |
|-------|----------|----------|
| `!setwelcome` | Hoş geldin mesajı kanalını ayarlar | `!setwelcome #kanal` |
| `!setleave` | Ayrılma mesajı kanalını ayarlar | `!setleave #kanal` |
| `!setyoutubechannel` | YouTube bildirim kanalını ayarlar | `!setyoutubechannel #kanal` |
| `!setyoutubeid` | İzlenecek YouTube kanal ID'sini ayarlar | `!setyoutubeid KANAL_ID` |
| `!config` | Mevcut yapılandırmayı gösterir | `!config` |

### Kullanıcı Komutları

| Komut | Açıklama | Kullanım |
|-------|----------|----------|
| `!ask` | AI'ya soru sorar | `!ask Python nedir?` |
| `@BotAdı` | Bot'u etiketleyerek soru sorar | `@TectonicBrawler Nasıl kod yazarım?` |

---

## Sorun Giderme

### Bot komutlara yanıt vermiyor
- Discord Developer Portal'da **Message Content Intent** açık olduğundan emin olun
- Bot'un sunucuda mesaj gönderme izni olduğunu kontrol edin
- `.env` dosyasındaki `COMMAND_PREFIX` değerini kontrol edin

### Üye katılma/ayrılma olayları çalışmıyor
- Discord Developer Portal'da **Server Members Intent** açık olduğundan emin olun
- `!setwelcome` ve `!setleave` komutlarıyla kanalları ayarladığınızdan emin olun
- Bot'un o kanallara mesaj gönderme izni olduğunu kontrol edin

### YouTube bildirimleri gelmiyor
- YouTube API Key'inizin geçerli olduğunu kontrol edin
- YouTube kanal ID'sinin doğru olduğunu kontrol edin
- `!setyoutubechannel` komutuyla bildirim kanalını ayarladığınızdan emin olun
- `bot.log` dosyasını kontrol edin

### AI yanıt vermiyor
- Groq API Key'inizin geçerli olduğunu kontrol edin
- Bot'u doğru şekilde etiketlediğinizden emin olun
- Rate limit'e takılmış olabilirsiniz (dakikada 5 istek limiti var)

### Bot kapanıyor veya hata veriyor
- `bot.log` dosyasını kontrol edin
- Tüm API key'lerin geçerli olduğunu doğrulayın
- Python versiyonunun 3.10 veya üzeri olduğunu kontrol edin
- İnternet bağlantınızı kontrol edin

---

## 24/7 Çalıştırma

### Windows'ta Otomatik Başlatma

1. `start_bot.bat` adında bir dosya oluşturun:
```batch
@echo off
cd "BURAYA_PROJE_KLASORU_YOLUNU_YAZIN"
call venv\Scripts\activate
python main.py
pause
```

2. Bu dosyayı çift tıklayarak bot'u başlatabilirsiniz
3. Windows başlangıcında otomatik çalıştırmak için Task Scheduler kullanın

### Bulut Sunucu Seçenekleri

- **Railway**: Ücretsiz hosting, GitHub entegrasyonu
- **Heroku**: Ücretsiz tier mevcut
- **DigitalOcean**: Aylık $5'tan başlayan droplet'ler
- **AWS EC2**: Ücretsiz tier 12 ay boyunca

---

## Destek

Sorun yaşarsanız:
1. Bu rehberdeki sorun giderme bölümünü kontrol edin
2. `bot.log` dosyasını inceleyin
3. Tüm API key'lerin doğru girildiğinden emin olun

---

## Kullanılabilir AI Modelleri

`.env` dosyasındaki `AI_MODEL` değerini değiştirerek farklı modeller kullanabilirsiniz:

- `mixtral-8x7b-32768` (varsayılan) - Hızlı ve dengeli
- `llama2-70b-4096` - Daha büyük bağlam penceresi
- `gemma-7b-it` - Google'ın Gemma modeli

---

## Güvenlik Notları

- ⚠️ `.env` dosyanızı asla kimseyle paylaşmayın
- ⚠️ Discord bot token'ınızı gizli tutun
- ⚠️ API key'lerinizi GitHub'a yüklemeyin
- ⚠️ `.gitignore` dosyasının `.env` dosyasını içerdiğinden emin olun
