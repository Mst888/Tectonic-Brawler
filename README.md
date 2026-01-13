# Tectonic Brawler Discord Bot

A production-ready Discord bot built with Python featuring member event announcements, YouTube upload notifications, AI-powered question answering using Groq, and comprehensive admin controls.

## Features

### 1. Member Join/Leave Announcements
- Welcomes new members with customizable messages
- Announces when members leave the server
- Configurable announcement channels

### 2. YouTube Upload Notifications
- Monitors YouTube channels for new video uploads
- Sends automatic notifications to designated Discord channels
- Prevents duplicate notifications
- Checks for new videos every 10 minutes

### 3. AI Question Answering (Groq-Powered)
- Responds when mentioned (@BotName)
- Supports `!ask` command for direct questions
- Uses Groq API (OpenAI-compatible) for fast AI responses
- Built-in rate limiting (5 requests per minute per user)
- Handles long responses with automatic message chunking

### 4. Admin Commands
- Configure all bot settings via Discord commands
- Administrator-only access with permission checks
- Persistent configuration storage

## Requirements

- Python 3.10 or higher
- Discord Bot Token
- YouTube Data API Key
- Groq API Key

## Installation

### 1. Clone or Download the Repository

```bash
cd "Tectonic Brawler"
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Discord Bot Token (from Discord Developer Portal)
DISCORD_TOKEN=your_discord_bot_token_here

# YouTube Data API Key (from Google Cloud Console)
YOUTUBE_API_KEY=your_youtube_api_key_here

# Groq API Key (from https://console.groq.com)
GROQ_API_KEY=your_groq_api_key_here

# Groq API Configuration
GROQ_API_BASE=https://api.groq.com/openai/v1
AI_MODEL=mixtral-8x7b-32768

# Bot Command Prefix
COMMAND_PREFIX=!
```

### 5. Run the Bot

```bash
python main.py
```

## Getting API Keys

### Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Click "Reset Token" and copy your token
5. Enable these Privileged Gateway Intents:
   - **Server Members Intent**
   - **Message Content Intent**
6. Invite the bot to your server with appropriate permissions

### YouTube Data API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable "YouTube Data API v3"
4. Create credentials (API Key)
5. Copy your API key

### Groq API Key
1. Go to [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy your API key

## Bot Commands

### Admin Commands (Administrator Only)

| Command | Description | Usage |
|---------|-------------|-------|
| `!setwelcome` | Set the channel for welcome messages | `!setwelcome #welcome` |
| `!setleave` | Set the channel for leave messages | `!setleave #goodbye` |
| `!setyoutubechannel` | Set the channel for YouTube notifications | `!setyoutubechannel #videos` |
| `!setyoutubeid` | Set the YouTube channel ID to monitor | `!setyoutubeid UC_x5XG1OV2P6uZZ5FSM9Ttw` |
| `!config` | View current bot configuration | `!config` |

### User Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `!ask` | Ask the AI a question | `!ask What is Python?` |
| `@BotName` | Mention the bot to ask a question | `@TectonicBrawler How do I code?` |

## Configuration

The bot stores its configuration in `config.json`. This file is automatically created and updated when you use admin commands.

```json
{
  "welcome_channel_id": null,
  "leave_channel_id": null,
  "youtube_notification_channel_id": null,
  "youtube_channel_id": null,
  "last_video_id": null,
  "check_interval_minutes": 10
}
```

## Project Structure

```
Tectonic Brawler/
├── main.py                 # Bot entry point
├── config.json             # Persistent configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── .env.example            # Environment variables template
├── cogs/
│   ├── __init__.py
│   ├── events.py          # Member join/leave events
│   ├── youtube.py         # YouTube monitoring
│   ├── ai.py              # AI question answering
│   └── admin.py           # Admin commands
└── utils/
    ├── __init__.py
    └── config_manager.py  # Configuration management
```

## Running 24/7

### Windows (using Task Scheduler)
1. Create a batch file `start_bot.bat`:
```batch
@echo off
cd "C:\Users\mesud\Documents\Kodland\Tectonic Brawler"
call venv\Scripts\activate
python main.py
```
2. Use Task Scheduler to run this batch file at startup

### Linux (using systemd)
1. Create a service file `/etc/systemd/system/tectonic-bot.service`:
```ini
[Unit]
Description=Tectonic Brawler Discord Bot
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/Tectonic Brawler
ExecStart=/path/to/Tectonic Brawler/venv/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
```
2. Enable and start the service:
```bash
sudo systemctl enable tectonic-bot
sudo systemctl start tectonic-bot
```

### Cloud Hosting Options
- **Heroku**: Use a `Procfile` with `worker: python main.py`
- **Railway**: Connect your GitHub repo and deploy
- **DigitalOcean**: Use a droplet with systemd service
- **AWS EC2**: Run on a free-tier instance with systemd

## Troubleshooting

### Bot doesn't respond to commands
- Check that the bot has the correct permissions in your Discord server
- Verify that **Message Content Intent** is enabled in Discord Developer Portal
- Check that the command prefix matches your `.env` file

### Member join/leave events not working
- Ensure **Server Members Intent** is enabled in Discord Developer Portal
- Verify channels are set using `!setwelcome` and `!setleave`
- Check bot has permission to send messages in those channels

### YouTube notifications not working
- Verify your YouTube API key is valid
- Check the YouTube channel ID is correct (use `!setyoutubeid`)
- Ensure notification channel is set with `!setyoutubechannel`
- Check bot logs for API errors

### AI not responding
- Verify your Groq API key is valid and has credits
- Check that you're mentioning the bot correctly or using `!ask`
- Review rate limiting (max 5 requests per minute per user)

### Bot crashes or disconnects
- Check `bot.log` file for error messages
- Verify all API keys are valid
- Ensure stable internet connection
- Check Python version is 3.10 or higher

## Logs

The bot creates a `bot.log` file with detailed logging information. Check this file for debugging issues.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the `bot.log` file for errors
3. Verify all API keys are valid and have proper permissions

## Available Groq Models

- `mixtral-8x7b-32768` (default) - Fast and balanced
- `llama2-70b-4096` - Larger context window
- `gemma-7b-it` - Google's Gemma model

Change the model in your `.env` file by updating the `AI_MODEL` variable.

## License

This project is provided as-is for educational and personal use.
