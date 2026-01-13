import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config_manager
    
    @commands.command(name='setwelcome')
    @commands.has_permissions(administrator=True)
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel):
        self.config.set('welcome_channel_id', channel.id)
        await ctx.send(f"✅ Welcome channel set to {channel.mention}")
        self.bot.logger.info(f'Welcome channel set to {channel.id} by {ctx.author}')
    
    @commands.command(name='setleave')
    @commands.has_permissions(administrator=True)
    async def set_leave_channel(self, ctx, channel: discord.TextChannel):
        self.config.set('leave_channel_id', channel.id)
        await ctx.send(f"✅ Leave channel set to {channel.mention}")
        self.bot.logger.info(f'Leave channel set to {channel.id} by {ctx.author}')
    
    @commands.command(name='setyoutubechannel')
    @commands.has_permissions(administrator=True)
    async def set_youtube_channel(self, ctx, channel: discord.TextChannel):
        self.config.set('youtube_notification_channel_id', channel.id)
        await ctx.send(f"✅ YouTube notification channel set to {channel.mention}")
        self.bot.logger.info(f'YouTube notification channel set to {channel.id} by {ctx.author}')
    
    @commands.command(name='setyoutubeid')
    @commands.has_permissions(administrator=True)
    async def set_youtube_id(self, ctx, *, youtube_channel_id: str):
        self.config.set('youtube_channel_id', youtube_channel_id)
        await ctx.send(f"✅ YouTube channel ID set to `{youtube_channel_id}`")
        self.bot.logger.info(f'YouTube channel ID set to {youtube_channel_id} by {ctx.author}')
    
    @commands.command(name='config')
    @commands.has_permissions(administrator=True)
    async def show_config(self, ctx):
        welcome_ch = self.config.get('welcome_channel_id')
        leave_ch = self.config.get('leave_channel_id')
        youtube_ch = self.config.get('youtube_notification_channel_id')
        youtube_id = self.config.get('youtube_channel_id')
        
        embed = discord.Embed(
            title="⚙️ Bot Configuration",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="Welcome Channel",
            value=f"<#{welcome_ch}>" if welcome_ch else "Not set",
            inline=False
        )
        
        embed.add_field(
            name="Leave Channel",
            value=f"<#{leave_ch}>" if leave_ch else "Not set",
            inline=False
        )
        
        embed.add_field(
            name="YouTube Notification Channel",
            value=f"<#{youtube_ch}>" if youtube_ch else "Not set",
            inline=False
        )
        
        embed.add_field(
            name="YouTube Channel ID",
            value=f"`{youtube_id}`" if youtube_id else "Not set",
            inline=False
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Admin(bot))
