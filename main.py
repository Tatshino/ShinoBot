import asyncio
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
import youtube_dl
import os

from apikeys import *

intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = 'sh!', intents=intents)

@client.event
async def on_ready():
  #await client.change_presence(status=discord.Status.idle)
  await client.change_presence(activity=nextcord.Game('Minecraft'))
  print('We have logged in as {0.user}'.format(client))

@client.slash_command(name = "help", description = "description of all available commands", guild_ids=[1010962644934590486])
async def help(interaction: Interaction):
  await interaction.response.send_message("This is help")

initial_extensions = []

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
             client.load_extension(f"cogs.{filename[:-3]}")



"""print(initial_extensions)

if __name__ == '__main__':
  for extension in initial_extensions:
    client.load_extension(extension)

print(extension)

client.run(botToken)"""

async def main():
  await load_extensions()
  await client.start(botToken)

asyncio.run(main())