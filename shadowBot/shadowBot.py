import discord
from discord.ext import commands
import os
import asyncio

# intentの作成(全て許可)
discord_intents = discord.Intents.all()

# ボットを作成
shadowBot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), 
    intents=discord_intents,
    case_insensitive=True
)

# ボットが起動したときの処理
@shadowBot.event
async def on_ready() -> None:
    print("shadowBot starts working!")

# Cogをロードする
async def load() -> None:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await shadowBot.load_extension(f"cogs.{filename[:-3]}")

# メインの処理
async def main() -> None:
    async with shadowBot:
        await load()
        # tokenのIDを読み込む
        with open('./IDs/TOKEN_ID.txt', 'r') as tID:
            TOKEN_ID: str = tID.read().strip()
        await shadowBot.start(TOKEN_ID)

if __name__ == '__main__':
    asyncio.run(main())
