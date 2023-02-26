import discord
from discord.ext import commands

class Developer(commands.Cog):
    """_summary_

    Args:
        commands (_type_): _description_
    """
    def __init__(self, _bot) -> None:
        """_summary_

        Args:
            _bot (_type_): _description_
        """
        self._bot = _bot
        self.DEVELOPER_ID = self.__set_dev_id()

    def __set_dev_id(self) -> int: 

        developer_id = 0
        with open('developer_id.txt', 'r') as dev_id_file:
            developer_id = int(dev_id_file.read().strip())
        print("dev_id is loaded!")
        return developer_id


    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Developer.py is ready!")

    @commands.command(name="developer")
    async def command_introduce(self, ctx):
        embed=discord.Embed(
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
    async def command_access(self, ctx):
        master_user= self._bot.get_user(self.DEVELOPER_ID)
        await master_user.send("Someone want to conntact!")
        await ctx.send("I send DM to my lord ...")


async def setup(bot):
    await bot.add_cog(Developer(bot))
