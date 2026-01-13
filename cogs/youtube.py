import discord
from discord.ext import commands, tasks
import aiohttp
import os
from datetime import datetime

class YouTube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config_manager
        self.api_key = os.getenv('YOUTUBE_API_KEY')
        self.check_interval = self.config.get('check_interval_minutes', 10)
        
        if self.api_key:
            self.check_uploads.start()
        else:
            self.bot.logger.warning('YouTube API key not found, upload checking disabled')
    
    def cog_unload(self):
        self.check_uploads.cancel()
    
    @tasks.loop(minutes=10)
    async def check_uploads(self):
        channel_id = self.config.get('youtube_channel_id')
        notification_channel_id = self.config.get('youtube_notification_channel_id')
        
        if not channel_id or not notification_channel_id:
            return
        
        try:
            video_id, video_title, video_url = await self.get_latest_video(channel_id)
            
            if not video_id:
                return
            
            last_video_id = self.config.get('last_video_id')
            
            if video_id != last_video_id:
                await self.send_notification(notification_channel_id, video_title, video_url)
                self.config.set('last_video_id', video_id)
                self.bot.logger.info(f'New video detected: {video_title}')
        
        except Exception as e:
            self.bot.logger.error(f'Error checking YouTube uploads: {e}')
    
    @check_uploads.before_loop
    async def before_check_uploads(self):
        await self.bot.wait_until_ready()
    
    async def get_latest_video(self, channel_id):
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'key': self.api_key,
            'channelId': channel_id,
            'part': 'snippet',
            'order': 'date',
            'maxResults': 1,
            'type': 'video'
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    self.bot.logger.error(f'YouTube API error: {response.status}')
                    return None, None, None
                
                data = await response.json()
                
                if not data.get('items'):
                    return None, None, None
                
                video = data['items'][0]
                video_id = video['id']['videoId']
                video_title = video['snippet']['title']
                video_url = f'https://www.youtube.com/watch?v={video_id}'
                
                return video_id, video_title, video_url
    
    async def send_notification(self, channel_id, title, url):
        channel = self.bot.get_channel(channel_id)
        
        if not channel:
            self.bot.logger.warning(f'YouTube notification channel {channel_id} not found')
            return
        
        embed = discord.Embed(
            title="📢 New YouTube Video Uploaded!",
            description=f"🎬 **{title}**\n🔗 [Watch Now]({url})",
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        
        try:
            await channel.send(embed=embed)
        except Exception as e:
            self.bot.logger.error(f'Failed to send YouTube notification: {e}')

async def setup(bot):
    await bot.add_cog(YouTube(bot))
