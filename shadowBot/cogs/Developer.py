import discord
from discord.ext import commands
from typing import Union
from dataclasses import dataclass

class Developer(commands.Cog):
    def __init__(self, _bot: commands.Bot) -> None:
        self._bot: commands.Bot = _bot

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
        embed.add_field(name="Do you like it?", value="Yeah!", inline=True)
        embed.set_image(url="https://www.capcom.co.jp/monsterhunter/world-iceborne/topics/e-jang/images/img_rajang08_l.png")
        embed.set_footer(text="summoned in 2023")
        await ctx.send(embed=embed)

    @commands.command(name="contact")
    async def command_contact(self, ctx: commands.Context) -> None:
        with open('./IDs/DEVELOPER_ID.txt', 'r') as devID:
            DEVELOPER_ID: int = int(devID.read().strip())
        master_user: Union[discord.User, None] = self._bot.get_user(DEVELOPER_ID)
        if master_user is None:
            print("Where is my load!")
            return None
        await master_user.send("Someone want to contact!")
        await ctx.send("I send DM to my lord ...")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Developer(bot))
