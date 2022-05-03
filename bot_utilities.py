import discord
from discord.ext import commands, tasks


#Help Command
@botClient.command()
async def bighelp(ctx):
    await ctx.send(
        ' !ping\n !bigweather <city>\n !music <play>,<stop>\n !quote <symbol>'
    )


#Ping Command posts latency in chat
@botClient.command()
async def ping(ctx):
    await ctx.send(f'latency: {round(botClient.latency*1000)}ms')