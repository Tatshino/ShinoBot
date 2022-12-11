import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from nextcord.utils import get
from apikeys import *
from songlist import *
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord import Member
import requests
import json
import os

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions,):
            await ctx.send("You're not worthy of this power!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Odin has struck {member}')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are not worthy of Odins power!")

    #new command
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def addRole(self, ctx, user : nextcord.Member, *, role : nextcord.Role):

        if role in user.roles:
            await ctx.send(f"{user.mention} already has the role, {role}")
        else:
            await user.add_roles(role)
            await ctx.send(f"Added {role} to {user.mention}")
    
    @addRole.error
    async def role_error(self, ctx, error):
        if inistance(error, commands.MissingPersmissions):
            await ctx.send("You do not have permission to use this command")

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def removeRole(self, ctx, user : nextcord.Member, *, role : nextcord.Role):

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"Removed {role} from {user.mention}")
        else:
            
            await ctx.send(f"{user.mention} does not have the role {role}")

    @removeRole.error
    async def removeRole_error(self, ctx, error):
        if inistance(error, commands.MissingPersmissions):
            await ctx.send("You do not have permission to use this command")

async def setup(client):
    client.add_cog(Admin(client))