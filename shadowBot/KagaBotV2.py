import discord
from discord.ext import commands, tasks
from itertools import cycle

discord_intents = discord.Intents.default()
discord_intents.message_content = True

shadowBot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), 
    intents=discord_intents,
    case_insensitive=True
)

bot_status = cycle(["Status One", "Status Two", "Status Three", "Status Four", "Status Five"])
@tasks.loop(seconds=5)
async def change_status():
    await shadowBot.change_presence(activity=discord.Game(next(bot_status)))

@shadowBot.event
async def on_ready():
    print("shadowBot starts working!")
    change_status.start()

@shadowBot.command()
async def ping(ctx):
    bot_latency = round(shadowBot.latency * 1000)
    await ctx.send(f"pong! {bot_latency} ms.")

TOKEN = ''
with open('token_id.txt', 'r') as token_id:
    TOKEN = token_id.read()
shadowBot.run(TOKEN)
