import discord
from discord.ext import commands
import json
import os

# Veri dosyası yolu
DATA_FILE = "gelengidenkanal.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

class GelenGiden(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gg")
    async def gelen_giden(self, ctx, subcommand=None, channel: discord.TextChannel = "#gelenler-gidenler"):
        data = load_data()
        guild_id = str(ctx.guild.id)

        if subcommand is None:
            await ctx.reply("Gelen Giden Log Kanalını Ayarlamak İçin `!gg ayarla #kanal` yazmalısın.")
            return

        if subcommand == "!ayarla":
            if channel is None:
                await ctx.reply("Ayarlamak istediğin kanalı etiketlemelisin!")
                return

            data[guild_id] = channel.id
            save_data(data)
            embed = discord.Embed(title="Başarılı!", description=f"Başarılı bir şekilde Gelen Giden Log Kanalı {channel.mention} olarak ayarlandı!", color=discord.Color.random())
            await ctx.send(embed=embed)

        elif subcommand == "sıfırla":
            if guild_id not in data:
                await ctx.reply("Sıfırlamam için önce bir kanal ayarlanmış olmalı.")
                return

            del data[guild_id]
            save_data(data)
            embed = discord.Embed(title="Başarılı!", description="Gelen Giden Log Kanalı başarıyla sıfırlandı!", color=discord.Color.random())
            await ctx.send(embed=embed)

        else:
            await ctx.reply("Geçersiz komut! `ayarla` veya `sıfırla` kullanabilirsin.")

def setup(bot):
    bot.add_cog(GelenGiden(bot))
