import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
    print("Bot is ready.")
    
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed()

    embed.set_author(name='Help')
    embed.add_field(name='!ban', value='Bans the mentioned user from the server', inline=False)
    embed.add_field(name='!clear', value='Purges the amount of messages you desire', inline=False)
    embed.add_field(name='!kick', value='Kicks the mentioned user from the server', inline=False)
    embed.add_field(name='!mute', value='Mutes the mentioned user, must have the role **muted**', inline=False)
    embed.add_field(name='!unmute', value='Unmutes the mentioned user', inline=False)

    await author.send(embed=embed)
    

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
