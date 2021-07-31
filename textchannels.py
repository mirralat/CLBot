import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


def clbot(b):
    return b.author == bot.user


class Helper(commands.Cog):
    @bot.command(pass_context=True)
    async def helpme(self, ctx):
        channel = ctx.message.channel
        async with channel.typing():
            embed = discord.Embed(title=f"Hi! \nThis is the list of commands:", value=f"****",
                                  color=ctx.guild.me.top_role.color,
                                  timestamp=ctx.message.created_at, )
            embed.add_field(name="!test", value=f"**u can test bot with this command**",  inline=False)
            embed.add_field(name="!clearall", value=f"**removal messages of ALL users, including bot**", inline=False)
            embed.add_field(name="!clearbot", value=f"**remove bot's messages**", inline=False)
            embed.add_field(name="!ban", value=f"**ban member**", inline=False)
            embed.add_field(name="!weather + <city>",  value=f"**show weather in the city**", inline=False)
            embed.add_field(name="!random", value=f"**random count**", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)


class Comandi(commands.Cog):
    @bot.command(pass_context=True)
    async def test(ctx):
        channel = ctx.channel
        async with channel.typing():
            await ctx.send('Все работает')

    @bot.command(pass_context=True)
    async def clearbot(ctx):
        channel = ctx.channel
        delete = await channel.purge(limit=10000, check=clbot)

    @bot.command(pass_context=True)
    async def clearall(ctx):
        channel = ctx.channel
        remove = await channel.purge(limit=100000)
        channel = ctx.channel
        async with channel.typing():
            await ctx.send('Deleted {} messages'.format(len(remove)))

    @bot.command(pass_context=True)
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        channel = ctx.channel
        async with channel.typing():
            await ctx.send('User banned')


class Inf:
    @bot.command(pass_context=True)
    async def my_top_role(ctx):
        roles = ctx.author.roles
        roles.reverse()
        top_role = roles[0]
        channel = ctx.channel
        async with channel.typing():
            await ctx.send(top_role)

    @bot.command(pass_context=True)
    async def top_role(ctx, member: discord.Member):
        roles = member.roles
        roles.reverse()
        top_role = roles[0]
        channel = ctx.channel
        async with channel.typing():
            await ctx.send(top_role)

    '''
    @bot.command(pass_context=True)
    async def info(ctx, member: discord.Member):
        channel = ctx.channel
        roles = member.roles
        low_role = roles[0]
        roles.reverse()
        top_role = roles[0]
        ava = member.avatar_url
        async with channel.typing():
            embed = discord.Embed(title=f"Member information", value=f"****",
                                            color=ctx.guild.me.top_role.color,
                                            timestamp=ctx.message.created_at, )
            embed.add_field(name="Nickname", value=f"**{member}", inline=False)
            embed.add_field(name="Role(s)", value=f"**The top role is: {top_role},"
                            f" the lowest role is: {low_role}**", inline=False)
            embed.set_thumbnail(url=ava)
'''


class Eve:
    @bot.event
    async def on_member_remove(ctx,  member: discord.Member, reason=None):
        await member.ban(reason=reason)
        await ctx.send("This user has already left the guild and now banned")

    @bot.event
    async def on_member_join(member):
        if welcome_channel := member.guild.get_channel(754741279918410952):
            await welcome_channel.send(f"Hi {member.mention}!")




