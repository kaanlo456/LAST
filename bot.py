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
    await ctx.send(get_random_recommendation(media_type="film"))

@bot.command
async def fbilim(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="bilim kurgu"))

@bot.command
async def fkomedi(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="komedi"))

@bot.command
async def fsuc(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="suç"))

@bot.command
async def ftarih(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="tarih"))

@bot.command
async def ftarihi(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="tarihi"))

@bot.command
async def fanimasyon(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="animasyon"))

@bot.command
async def fgerilim(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="gerilim"))

@bot.command
async def fromantik(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="romantik"))

@bot.command
async def fsavas(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="savaş"))

@bot.command
async def ffantastik(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="fantastik"))

@bot.command
async def fbelgesel(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="belgesel"))

@bot.command
async def faksiyon(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="aksiyon"))

@bot.command
async def fkorku(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="korku"))

@bot.command
async def fmacera(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="macera"))

@bot.command
async def fgizem(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="gizem"))

@bot.command
async def fdram(ctx):
    await ctx.send(get_random_recommendation(media_type="film", category="dram"))


@bot.command
async def dizi(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi"))

@bot.command
async def dbilim(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="bilim"))

@bot.command
async def dkomedi(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="komedi"))

@bot.command
async def dsuc(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="suç"))

@bot.command
async def dtarih(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="tarih"))

@bot.command
async def dtarihi(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="tarihi"))

@bot.command
async def danimasyon(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="animasyon"))

@bot.command
async def dgerilim(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="gerilim"))

@bot.command
async def dromantik(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="romantik"))

@bot.command
async def dsavas(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="savaş"))

@bot.command
async def dfantastik(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="fantastik"))

@bot.command
async def dbelgesel(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="belgesel"))

@bot.command
async def daksiyon(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="aksiyon"))

@bot.command
async def dkorku(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="korku"))

@bot.command
async def dmacera(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="macera"))

@bot.command
async def dgizem(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="gizem"))

@bot.command
async def ddram(ctx):
    await ctx.send(get_random_recommendation(media_type="dizi", category="dram"))

@bot.command
async def devs(ctx):
    await ctx.send("kaanlo456 - https://github.com/kaanlo456 \n YusufTGNS - https://github.com/YusufTGNS")

@bot.command
async def info(ctx):
    await ctx.send('''Thank you for running this bot.\n
                   Bu botu çalıştırdığınız için teşekkürler.\n
                   !devs - List of developers.\n
                   Yapımcılar listesi.\n
                   !film - This command gives you a random reccomandations based on films.\n
                   Bu komut rastgele filmler önerir.\n
                   !(type)(category) - This command gives you recommendations about (category)(type)\n
                   Bu komut (category=kategori)(type=tip) hakkında öneri verir.\n
                   categorys-kategoriler\n
                   !(type)bilim/sci-fi/bilim kurgu\n
                   !(type)komedi/comedy/komedi\n
                   !(type)suc/crime/suç\n
                   !(type)tarih/history/tarih
                   !(type)animasyon/animation/animasyon\n
                   !(type)gerilim/thriller/gerilim\n
                   !(type)romantik/romantic/romantik\n
                   !(type)savas/war/savaş\n
                   !(type)fantastik/fantastic/fantastik\n
                   !(type)belgesel/documentary/belgesel\n
                   !(type)aksiyon/action/aksiyon\n
                   !(type)korku/scary/korku\n
                   !(type)macera/adventure/macera\n
                   !(type)gizem/mistery/gizem\n
                   !(type)dram/drama/dram\n
                   Types - Tipler:\n
                   f = films - filmler\n
                   d = series - diziler
                   ''')

if __name__ == "__main__":
    bot.run(TOKEN)





