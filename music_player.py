import discord
from discord.ext import commands, tasks
import glob
import ffmpeg
import asyncio


#Command to play mp3 from file
@botClient.command()
async def music(ctx,*, push):
    channel=botClient.get_channel(771592178706415616)
    if push=="play":
        vchan= await channel.connect()
        songs = glob.glob('music\*.mp3')
        for song in songs:
            vchan.play(discord.FFmpegPCMAudio(f'{song}'))
            while vchan.is_playing():
                await asyncio.sleep(1)
    if push=="stop":
        for x in botClient.voice_clients:
            await x.disconnect()
