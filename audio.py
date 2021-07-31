import config
import discord
import asyncio
import youtube_dl
import os

from discord.ext import commands

bot = commands.Bot(command_prefix='!')


def clbot(b):
    return b.author == bot.user


@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send('Yes, it works!')


@bot.command(pass_context=True)
async def yplay(ctx, url):
    mus = os.path.isfile("music.mp3")
    try:
        if mus:
            os.remove("music.mp3")
    except PermissionError:
        await ctx.send("Already")
    return
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    yd_o = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }




