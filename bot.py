import discord
from discord.ext import commands, tasks

botClient= commands.Bot(command_prefix='.')

@botClient.event
async def on_ready():
    print('The Discord bot is ready')

botClient.run('ODQ4MjMxMjUzNzc3MzE3OTA4.YLJm6g.92A0MZxnB-lHiZR6yZeb5YePX-k')