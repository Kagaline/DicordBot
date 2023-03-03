import discord
from discord.ext import commands, tasks
import os
import asyncio
from typing import Union
from itertools import cycle


# intentの作成(全て許可)
discord_intents = discord.Intents.all()

shadowBot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), 
    intents=discord_intents,
    case_insensitive=True
)


# 実験用サーバのサーバID(Guild ID)を取得⇒ギルド情報を取得
with open('guild_id.txt', 'r') as guild_id_file:
    GUILD_ID: int = int(guild_id_file.read().strip())
guild: Union[discord.Guild, None] = shadowBot.get_guild(GUILD_ID)

# メンバー情報を30分ごとに更新
@tasks.loop(minutes = 30)
async def update_member_cache() -> None:
    global guild
    guild = shadowBot.get_guild(GUILD_ID)
    if guild is None:
        print("cannot get guild info.")
        return 
    for member in guild.members:
        print(member.name)
    await guild.chunk()



status = cycle(["command: ping", "command: developer", "command: contact"])
@tasks.loop(seconds=5)
async def change_status()->None:
    await shadowBot.change_presence(activity=discord.Game(next(status)))

# ボットが起動したときの処理
@shadowBot.event
async def on_ready() -> None:
    print("shadowBot starts working!")
    update_member_cache.start()
    change_status.start()

# Cogをロードする
async def load() -> None:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await shadowBot.load_extension(f"cogs.{filename[:-3]}")

# メインの処理
async def main() -> None:
    async with shadowBot:
        await load()
        with open('token_id.txt', 'r') as token_id:
            TOKEN_ID: str = token_id.read()
        await shadowBot.start(TOKEN_ID)


if __name__ == '__main__':
    asyncio.run(main())
