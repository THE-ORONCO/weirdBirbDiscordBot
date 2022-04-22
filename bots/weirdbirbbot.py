from discord.ext.commands import Bot


class WeirdBirbBot(Bot):
    """class representing a weird birb that pretends to be a discord bot"""

    async def on_ready(self):
        """notify user as which user the bot logged in"""
        print(f"logged in as {self.user.name}")
