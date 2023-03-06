from discord.ext import commands,tasks
from itertools import cycle
import discord

class TaskWatcher(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.status = cycle(["command: ping", "command: developer", "command: contact"])

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("TaskWatcher.py is ready!")
        self.change_status.start()

    @tasks.loop(minutes=5)
    async def change_status(self)->None:
        await self.bot.change_presence(activity=discord.Game(next(self.status)))

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TaskWatcher(bot))
