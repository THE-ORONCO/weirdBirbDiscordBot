import discord
from discord.ext import commands


class Greetings(commands.Cog):
    """Cog-class that contains very basic greeting commands for testing purposes"""

    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context, *, member: discord.Member = None):
        """Says hello to someone"""
        member = member or ctx.author
        await ctx.send(f'Hello {member.display_name} by {self.bot.user.name}')


def setup(client):
    client.add_cog(Greetings(client))
