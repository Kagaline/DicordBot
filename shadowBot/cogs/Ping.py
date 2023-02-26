import discord
from discord.ext import commands
import random
from typing import Tuple

class Ping(commands.Cog):
    def __init__(self, _bot: commands.Bot) -> None:
        self._bot = _bot
        self.critical_pong: Tuple[str, ...] = (
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
    async def ping(self, ctx: commands.Context) -> None:
        bot_latency: int = round(self._bot.latency * 1000)
        random_critical: str = random.choice(self.critical_pong)
        await ctx.send(f"{random_critical} Pong ... !! ({bot_latency}ms)")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))
