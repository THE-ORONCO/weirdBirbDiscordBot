import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context, *, member: discord.Member = None):
        """Says hello to someone"""
        member = member or ctx.author
        await ctx.send(f'Hello {member.display_name}')


def setup(client):
    client.add_cog(Greetings(client))
