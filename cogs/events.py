import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config_manager
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = self.config.get('welcome_channel_id')
        
        if not channel_id:
            return
        
        channel = self.bot.get_channel(channel_id)
        if not channel:
            self.bot.logger.warning(f'Welcome channel {channel_id} not found')
            return
        
        try:
            await channel.send(f"👋 Welcome {member.mention} to the server!")
            self.bot.logger.info(f'Sent welcome message for {member.name}')
        except Exception as e:
            self.bot.logger.error(f'Failed to send welcome message: {e}')
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel_id = self.config.get('leave_channel_id')
        
        if not channel_id:
            return
        
        channel = self.bot.get_channel(channel_id)
        if not channel:
            self.bot.logger.warning(f'Leave channel {channel_id} not found')
            return
        
        try:
            await channel.send(f"😢 {member.name} has left the server.")
            self.bot.logger.info(f'Sent leave message for {member.name}')
        except Exception as e:
            self.bot.logger.error(f'Failed to send leave message: {e}')

async def setup(bot):
    await bot.add_cog(Events(bot))
