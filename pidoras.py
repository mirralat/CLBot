import discordhttps://github.com/Mirralat/CLBot/blob/main/pidoras
import config
from discord import Member

def clbot(b):
    return b.author == bot.user

async def discord.on_guild_join(guild):
    members = guild.members
    for member in members:
        await ctx.send("Пидорас зашел на сервер")

async def discord.on_guild_remove(guild):
    members = guild.members
    await ctx.send("Пидорас вышел с сервера")

bot.run(config.TOKEN)
