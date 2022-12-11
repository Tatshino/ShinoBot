import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from songlist import *
import youtube_dl
import os
from nextcord.utils import get
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord import Member

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context = True)
    async def play(self, ctx, url: str):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessor': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")

            source = FFmpegPCMAudio('song.mp3') #'Audio Files/Local Songs/Hacking to the Gate.mp3'
            player = voice.play(source)
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")


    """music = ListSong().mysongs

    queues = {}

    def check_queue(ctx, id):
        if queues[id] != []:
            voice = ctx.guild.voice_client
            source = queues[id].pop(0)
            player = voice.play(source)


    @commands.command(pass_context = True)
    async def joinvc(ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio(ListSong().mysongs[0]) #'Audio Files/Local Songs/Hacking to the Gate.mp3'
            player = voice.play(source)
        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")

    @commands.command(pass_context = True)
    async def leavevc(ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")

    @commands.command(pass_context = True)
    async def pause(ctx):
        voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("There isn't anything playing")

    @commands.command(pass_context = True)
    async def resume(ctx):
        voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Something is already playing")

    @commands.command(pass_context = True)
    async def stop(ctx):
        voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()

    @commands.command(pass_context = True)
    async def play(ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('Audio Files/Local Songs/' + arg + '.mp3')
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

    #for testing purposes
    @commands.command(pass_context = True)
    async def testplay(ctx, arg):
        voice = ctx.guild.voice_client
        if arg != "":
            arg2 = music.index(f'{arg}')
        else:
            pass
        source = FFmpegPCMAudio(arg2)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

    @commands.command(pass_context = True)
    async def queue(ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('Audio Files/Local Songs/' + arg + '.mp3')

        guild_id = ctx.message.guild.id

        if guild_id in queues:
            queues[guild_id].append(source)
        else:
            queues[guild_id] = [source]

        await ctx.send("Added to queue")"""

async def setup(client):
    client.add_cog(Music(client))