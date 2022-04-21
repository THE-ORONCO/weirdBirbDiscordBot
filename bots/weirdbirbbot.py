from discord.ext.commands import Bot


class WeirdBirbBot(Bot):
    async def on_ready(self):
        print(f"logged in as {self.user.name}")
