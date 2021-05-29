import discord
from discord.ext import commands, tasks
import pyowm
import glob
import ffmpeg
import asyncio


#Initializes bot with command prefix.
botClient= commands.Bot(command_prefix='!')

#OpenWeatherMap key
owm = pyowm.OWM('384117676beab9667270502d1e668946')

#Writes Status to console
@botClient.event
async def on_ready():
    print('The Discord bot is ready')

#Help Command
@botClient.command()
async def bighelp(ctx):
    await ctx.send(
        ' !ping\n'
        )


#Ping Command posts latency in chat
@botClient.command()
async def ping(ctx):
    await ctx.send(f'latency: {round(botClient.latency*1000)}ms')
    
    
    
#Weather Command returns weather based on location argument
@botClient.command()
async def bigweather(ctx, *, place):
    weathermgr = owm.weather_manager()
    observation = weathermgr.weather_at_place(f'{place},us')
    weather = observation.weather
    await ctx.send(f'status: {weather.status}\nTemp: {weather.temp}\nHumidity: {weather.humidity}\n')
    
    
    
botClient.run('ODQ4MjMxMjUzNzc3MzE3OTA4.YLJm6g.92A0MZxnB-lHiZR6yZeb5YePX-k')