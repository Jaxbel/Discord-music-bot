import discord
from discord.ext import commands
import music 

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('-GerardoElBotardo ha llegado- ')

music.setup(bot)

#TOKEN
bot.run("OTAwMTI3NTgwNTAwMzkzOTk0.YW8zIg.tJejlALTJtvg1JYO8xyzxV8poPQ")