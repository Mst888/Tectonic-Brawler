import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv
import asyncio
from utils.config_manager import ConfigManager

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('TectonicBrawler')

class TectonicBrawler(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True
        
        super().__init__(
            command_prefix=os.getenv('COMMAND_PREFIX', '!'),
            intents=intents,
            help_command=None
        )
        
        self.config_manager = ConfigManager()
        self.logger = logger
    
    async def setup_hook(self):
        await self.load_cogs()
    
    async def load_cogs(self):
        cogs = ['events', 'youtube', 'ai', 'admin']
        
        for cog in cogs:
            try:
                await self.load_extension(f'cogs.{cog}')
                self.logger.info(f'Loaded cog: {cog}')
            except Exception as e:
                self.logger.error(f'Failed to load cog {cog}: {e}')
    
    async def on_ready(self):
        self.logger.info(f'{self.user} has connected to Discord!')
        self.logger.info(f'Bot is in {len(self.guilds)} guilds')
        
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="for tectonic shifts"
            )
        )
    
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to use this command.")
            return
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"❌ Missing required argument: {error.param.name}")
            return
        
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"❌ Invalid argument provided.")
            return
        
        self.logger.error(f'Command error: {error}', exc_info=error)
        await ctx.send("❌ An error occurred while processing the command.")

async def main():
    bot = TectonicBrawler()
    
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        logger.error('DISCORD_TOKEN not found in environment variables')
        return
    
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        logger.info('Bot shutdown requested')
    except Exception as e:
        logger.error(f'Bot encountered an error: {e}', exc_info=e)
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.run(main())
