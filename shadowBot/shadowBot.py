import discord
from discord.ext import commands, tasks
import os
import asyncio
from pprint import pprint


# intentの作成(全て許可)
discord_intents = discord.Intents.all()

shadowBot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), 
    intents=discord_intents,
    case_insensitive=True
)

# 実験用サーバのサーバID(Guild ID)を取得⇒ギルド情報を取得
with open('guild_id.txt', 'r') as guild_id_file:
    GUILD_ID = int(guild_id_file.read().strip())
guild = shadowBot.get_guild(GUILD_ID)


@tasks.loop(minutes=30)
async def update_member_cache():
    
    global guild
    guild = shadowBot.get_guild(GUILD_ID)
    if guild is None:
        print("cannot get guild info.")
        return 
    for member in guild.members:
        print(member.name)
    await guild.chunk()

@shadowBot.event
async def on_ready():
    print("shadowBot starts working!")
    update_member_cache.start()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await shadowBot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    
    async with shadowBot:
        await load()
        with open('token_id.txt', 'r') as token_id:
            TOKEN = token_id.read()
        await shadowBot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
