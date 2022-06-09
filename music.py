import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(" No estas en canal de voz!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
            await ctx.send("Fierro q le damos")  
        else:
            await ctx.voice_client.move_to(voice_channel)
               
    @commands.command()
    async def connect(self,ctx):
        await ctx.voice_client.connect()
        
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}     
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source =  await discord.FFmpegOpusAudio.from_probe(url2, method='fallback',**FFMPEG_OPTS)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        ctx.voice_client.pause()
        await ctx.send("Pausado perro")  
    
    @commands.command()
    async def stop(self,ctx):
        ctx.voice_client.stop()
        await ctx.send("Parado primo")  

    @commands.command()
    async def resume(self,ctx):
        ctx.voice_client.resume()
        await ctx.send("Reanudado pariente")


def setup(client):
  client.add_cog(music(client))

#API DISCORD
#https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=commands#bot