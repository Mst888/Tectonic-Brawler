import discord
from discord.ext import commands
import aiohttp
import os
from datetime import datetime, timedelta

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv('GROQ_API_KEY')
        self.api_base = os.getenv('GROQ_API_BASE', 'https://api.groq.com/openai/v1')
        self.model = os.getenv('AI_MODEL', 'mixtral-8x7b-32768')
        self.rate_limit = {}
        self.rate_limit_duration = 60
        self.max_requests_per_minute = 5
        
        if not self.api_key:
            self.bot.logger.warning('Groq API key not found, AI features disabled')
    
    def check_rate_limit(self, user_id):
        now = datetime.utcnow()
        
        if user_id not in self.rate_limit:
            self.rate_limit[user_id] = []
        
        self.rate_limit[user_id] = [
            timestamp for timestamp in self.rate_limit[user_id]
            if now - timestamp < timedelta(seconds=self.rate_limit_duration)
        ]
        
        if len(self.rate_limit[user_id]) >= self.max_requests_per_minute:
            return False
        
        self.rate_limit[user_id].append(now)
        return True
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if not self.api_key:
            return
        
        mentioned = self.bot.user in message.mentions
        
        if not mentioned:
            return
        
        if not self.check_rate_limit(message.author.id):
            await message.reply("⏳ You're sending requests too quickly. Please wait a moment.")
            return
        
        question = message.content.replace(f'<@{self.bot.user.id}>', '').strip()
        
        if not question:
            await message.reply("❓ Please ask me a question!")
            return
        
        async with message.channel.typing():
            response = await self.get_ai_response(question)
            
            if response:
                if len(response) > 2000:
                    chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(response)
            else:
                await message.reply("❌ Sorry, I couldn't process your request. Please try again later.")
    
    @commands.command(name='ask')
    async def ask_command(self, ctx, *, question: str):
        if not self.api_key:
            await ctx.send("❌ AI features are not configured.")
            return
        
        if not self.check_rate_limit(ctx.author.id):
            await ctx.send("⏳ You're sending requests too quickly. Please wait a moment.")
            return
        
        async with ctx.typing():
            response = await self.get_ai_response(question)
            
            if response:
                if len(response) > 2000:
                    chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
                    for chunk in chunks:
                        await ctx.send(chunk)
                else:
                    await ctx.send(response)
            else:
                await ctx.send("❌ Sorry, I couldn't process your request. Please try again later.")
    
    async def get_ai_response(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': self.model,
            'messages': [
                {
                    'role': 'system',
                    'content': 'You are a helpful, concise, and technical assistant. Answer questions about software, hardware, and general knowledge clearly and accurately.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'temperature': 0.7,
            'max_tokens': 1024
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f'{self.api_base}/chat/completions',
                    headers=headers,
                    json=payload
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        self.bot.logger.error(f'Groq API error {response.status}: {error_text}')
                        return None
                    
                    data = await response.json()
                    return data['choices'][0]['message']['content']
        
        except Exception as e:
            self.bot.logger.error(f'Error getting AI response: {e}')
            return None

async def setup(bot):
    await bot.add_cog(AI(bot))
