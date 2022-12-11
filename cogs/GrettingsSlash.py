import nextcord
from nextcord.ext import commands
from nextcord import Client, FFmpegPCMAudio
from nextcord.utils import get
from apikeys import *
from songlist import *
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord import Member
from nextcord import Interaction
import requests
import json
import os

class GreetingsSlash(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name = "hello", description = "hello", guild_ids=[1010962644934590486])
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message("Hello there!")

    @nextcord.slash_command(name = "info", description = "info about Shino", guild_ids=[1010962644934590486])
    async def info(self, ctx):
        await ctx.send("Im Shino! I was created by <@391300218269990922>")

    @nextcord.slash_command(name = "invite", description = "Shino will give you the link to invite her", guild_ids=[1010962644934590486])   
    async def invite(self, ctx):
        await ctx.send("You can invite me using this link!")
        await ctx.send("https://shorturl.at/bsAUW")


async def setup(client):
    client.add_cog(GreetingsSlash(client))