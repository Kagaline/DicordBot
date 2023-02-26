import discord
from discord.ext import commands
import random

class Ping(commands.Cog):
    def __init__(self, _bot) -> None:
        self._bot = _bot
        self.critical_pong = (
            "Shadow",
            "Dark Abyss",
            "Phantom",
            "Nightfall",
            "Demon",
            "Death Blow",
            "Blackout",
            "Nightmare",
            "Hellfire",
            "Necro",
        )

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Ping.py is ready!")

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self._bot.latency * 1000)
        random_critical = random.choice(self.critical_pong)
        await ctx.send(f"{random_critical} Pong ... !! ({bot_latency}ms)")


async def setup(bot):
    await bot.add_cog(Ping(bot))
