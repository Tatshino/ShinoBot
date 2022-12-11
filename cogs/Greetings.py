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

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello there!")

    @commands.command()
    async def info(self, ctx):
        await ctx.send("Im Shino! I was created by <@391300218269990922>")

    @commands.command()    
    async def invite(self, ctx):
        await ctx.send("You can invite me using this link!")
        await ctx.send("https://shorturl.at/bsAUW")

    @commands.Cog.listener()
    async def on_member_join(member):
        channel = client.get_channel(2934037839)
        await channel.send("welcome")

async def setup(client):
    client.add_cog(Greetings(client))