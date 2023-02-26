import discord
from discord.ext import commands
from typing import Union

class Developer(commands.Cog):
    def __init__(self, _bot: commands.Bot) -> None:
        self._bot: commands.Bot= _bot
        self.DEVELOPER_ID: int = self.__set_dev_id()

    def __set_dev_id(self) -> int: 
        with open('developer_id.txt', 'r') as dev_id_file:
            developer_id: int = int(dev_id_file.read().strip())
        print("dev_id is loaded!")
        return developer_id

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Developer.py is ready!")

    @commands.command(name="developer")
    async def command_introduce(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title="MY LORD", 
            description="Who create me in a world of violence and strife ...", 
            color=0x001eff
        )
        embed.set_author(
            name="Kagaline", 
            url="https://github.com/Kagaline", 
            icon_url="https://avatars.githubusercontent.com/u/80609274?v=4"
        )
        embed.set_thumbnail(url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        embed.add_field(name="s", value="ss", inline=True)
        embed.set_footer(text="summoned in 2023")
        await ctx.send(embed=embed)

    @commands.command(name="contact")
    async def command_access(self, ctx: commands.Context) -> None:
        master_user: Union[discord.User, None] = self._bot.get_user(self.DEVELOPER_ID)
        if master_user is None:
            print("Where is my load!")
            return None
        await master_user.send("Someone want to contact!")
        await ctx.send("I send DM to my lord ...")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Developer(bot))
