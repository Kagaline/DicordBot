import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Moderation.py is ready!")

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def command_clear(self, ctx: commands.Context, num_messages: int) -> None:
        await ctx.channel.purge(limit=num_messages+1)   #type: ignore
        await ctx.send(f"{num_messages} message(s) has been deleted.")

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def command_kick(self, ctx: commands.Context, member: discord.Member, mod_reason: str) -> None:
        print("kick called")
        await ctx.guild.kick(member, reason=mod_reason) #type: ignore
        conform_embed = discord.Embed(title="Successfully kicked!", color=0xff0000)
        conform_embed.add_field(
            name="Kicked: ", 
            value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", 
            inline=False
        )
        conform_embed.add_field(
            name="Reason: ",
            value=mod_reason,
            inline=False
        )
        await ctx.send(embed=conform_embed)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def command_ban(self, ctx: commands.Context, member: discord.Member, mod_reason: str) -> None:
        print("ban called")
        await ctx.guild.ban(member, reason=mod_reason)  #type: ignore
        conform_embed = discord.Embed(title="Successfully banned!", color=0xff0000)
        conform_embed.add_field(
            name="Banned: ", 
            value=f"{member.mention} has been banned from the server by {ctx.author.mention}.", 
            inline=False
        )
        conform_embed.add_field(
            name="Reason: ",
            value=mod_reason,
            inline=False
        )
        await ctx.send(embed=conform_embed)

    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def command_unban(self, ctx: commands.Context, userID) -> None:
        print("unban called")
        user = discord.Object(id=userID)
        await ctx.guild.unban(user) #type: ignore
        conform_embed = discord.Embed(title="Successfully unbanned!", color=0xff0000)
        conform_embed.add_field(
            name="Unbanned: ", 
            value=f"<@{userID}> has been unbanned from the server by {ctx.author.mention}.", 
            inline=False
        )
        await ctx.send(embed=conform_embed)



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot))
