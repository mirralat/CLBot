import discord
from discord.ext import commands
import requests
import config
import aiohttp
import asyncio
import json
import random
from bs4 import BeautifulSoup
from random import choice

bot = commands.Bot(command_prefix='!')


def clbot(b):
    return b.author == bot.user


@bot.command(pass_context=True)
async def test(ctx):
    await ctx.send('Yes, it works!')


class FuCo(commands.Cog):
    @bot.command(pass_context=True)
    async def rnum(ctx):
        rc = random.randint(0, 1000000)
        await ctx.send(f"Your random count is:{rc}")

    @bot.command(pass_context=True)
    async def rantag(ctx, member: discord.Member):
        guild = bot.get_guild()
        memberList = guild.members
        member = random.choice(memberList)
        await ctx.send(f"{member.mention} mom is gay!!!")

    @bot.command(pass_context=True)
    async def rpic(ctx):
        channel = ctx.message.channel
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.pexels.com/v1/search') as r:
                embed = discord.Embed(title=f"Your random pic:", color=ctx.guild.me.top_role.color, timestamp=ctx.message.created_at)
                embed.set_image(url=session.get)


class Weat(commands.Cog):
    @bot.command(pass_context=True)
    async def weather(ctx, *, city: str):
            api_key = "8d0c5d014b7587a8840240ff79c6e233"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = city
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            channel = ctx.message.channel
            if x["cod"] != "404":
                async with channel.typing():
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_temperature_celsiuis = str(round(current_temperature - 273.15))
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    weather_description = z[0]["description"]
                    embed = discord.Embed(title=f"Weather in {city_name}", color=ctx.guild.me.top_role.color,
                                  timestamp=ctx.message.created_at)
                    embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
                    embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                    embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                    embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                    embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}")
                    await channel.send(embed=embed)
            else:
                await channel.send("City not found")


class WALLET(commands.Cog):

    @bot.command(pass_context=True)
    async def btc(ctx):
            channel = ctx.channel
            base_url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            async with channel.typing():
                async with aiohttp.ClientSession() as session:
                    resp = await session.get(base_url)
                    response = await resp.text()
                    response = json.loads(response)
                    embed = discord.Embed(
                                    title="Bitcoin price is:",
                                    description=f" ${response['bpi']['USD']['rate']}",
                                    color=ctx.guild.me.top_role.color)
                    await channel.send(embed=embed)

    @bot.command(pass_context=True)
    async def rub(ctx):
            channel = ctx.channel
            async with channel.typing():
                DR = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/80.0.3987.149 Safari/537.36'}
                full_page = requests.get(DR, headers=headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
                embed = discord.Embed(
                            title="USD price is:",
                            description=f" {convert[0].text} ₽ ",
                            color=ctx.guild.me.top_role.color)
                await channel.send(embed=embed)


bot.run(config.TOKEN)


