import discord
from discord.ext import commands
import os
import asyncio

discord_intents = discord.Intents.all()

shadowBot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), 
    intents=discord_intents,
    case_insensitive=True
)

@shadowBot.event
async def on_ready():
    print("shadowBot starts working!")

    

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await shadowBot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with shadowBot:
        await load()
        TOKEN = ''
        with open('token_id.txt', 'r') as token_id:
            TOKEN = token_id.read()
        await shadowBot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
