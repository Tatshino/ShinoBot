import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from apikeys import *
from songlist import *

intents = discord.Intents.all()
intents.members = True

music = ListSong().mysongs

queues = {}

def check_queue(ctx, id):
  if queues[id] != []:
    voice = cyx.guild.voice_client
    source = queues[id].pop(0)
    player = voice.play(source)

"client = commands.Bot(command_prefix='sh!')"

client = commands.Bot(command_prefix = 'sh!', intents=intents)

"""client = discord.Client()"""

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
  await ctx.send("Hello there!")

@client.command()
async def info(ctx):
  await ctx.send("Im Shino! I was created by <@391300218269990922>")

@client.command()
async def menu(ctx):
  await ctx.send("<@391300218269990922> is still busy on creating my help menu")

@client.command()
async def users(ctx):
  await ctx.send(discord.User)

@client.command(pass_context = True)
async def joinvc(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio(ListSong().mysongs[0]) #'Audio Files/Local Songs/Hacking to the Gate.mp3'
    player = voice.play(source)
  else:
    await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")

@client.command(pass_context = True)
async def leavevc(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("I left the voice channel")
  else:
    await ctx.send("I am not in a voice channel")

@client.command(pass_context = True)
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    await ctx.send("There isn't anything playing")

@client.command(pass_context = True)
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send("Something is already playing")

@client.command(pass_context = True)
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.stop()

@client.command(pass_context = True)
async def play(ctx, arg):
  voice = ctx.guild.voice_client
  source = FFmpegPCMAudio('Audio Files/Local Songs/' + arg + '.mp3')
  player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

#for testing purposes
@client.command(pass_context = True)
async def testplay(ctx, arg):
  voice = ctx.guild.voice_client
  if arg != "":
    arg2 = music.index(f'{arg}')
  else:
    pass
  source = FFmpegPCMAudio(arg2)
  player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

@client.command(pass_context = True)
async def queue(ctx, arg):
  voice = ctx.guild.voice_client
  source = FFmpegPCMAudio('Audio Files/Local Songs/' + arg + '.mp3')

  guild_id = ctx.message.guild.id

  if guild_id in queues:
    queues[guild_id].append(source)
  else:
    queues[guild_id] = [source]

  await ctx.send("Added to queue")

client.run(botToken)