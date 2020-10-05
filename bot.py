import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
    print("Bot is ready.")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked: {user.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)   
    await ctx.send(f'Banned: {user.mention}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)    

client.run('BOT_TOKEN')    
