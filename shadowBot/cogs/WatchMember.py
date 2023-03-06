import discord
from discord.ext import commands, tasks
from typing import Union, Any

class MemberWatcher(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild: Union[discord.Guild, Any, None] = None
        self.members: Union[Any, list[discord.Member]] = []

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("WatchMember.py is ready!")
        self.update_members.start()

    @tasks.loop(hours=1)
    async def update_members(self) -> None:
        if self.guild is None:
            print("Failed to update")
            with open('./IDs/GUILD_ID.txt', 'r') as gID:
                GUILD_ID:int = int(gID.read().strip())
            self.guild = await self.bot.fetch_guild(GUILD_ID)
        self.members = await self.guild.chunk() 
        print("Updated member list")

    @commands.command(name="members")
    async def list_members(self, ctx):
        member_names = "\n".join([member.display_name for member in self.members])
        await ctx.send(f"Members:\n{member_names}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MemberWatcher(bot))
