import discord
from discord.ext import commands
from config import TOKEN, DATABASE
from logic import *

# Bot için niyetleri (intents) ayarlama
intents = discord.Intents.default()  # Varsayılan ayarların alınması
intents.messages = True              # Botun mesajları işlemesine izin verme
intents.message_content = True       # Botun mesaj içeriğini okumasına izin verme
intents.guilds = True                # Botun sunucularla (loncalar) çalışmasına izin verme
# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

@bot.command
async def film(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def bilim(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def komedi(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def suc(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def tarih(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def tarihi(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def animasyon(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def gerilim(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def romantik(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def savas(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def fantastik(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def belgesel(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def aksiyon(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def korku(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def macera(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def gizem(ctx):
    await ctx.send(get_random_recommendation())

@bot.command
async def dram(ctx):
    await ctx.send(get_random_recommendation())





