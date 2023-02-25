import discord
from discord.ext import commands
import requests
import json
from cogs import testcog

discord_intents = discord.Intents.default()
discord_intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('$'), 
    intents=discord_intents,
    case_insensitive=True
)

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def check_answer(answer: str):
    lower_answer = answer.lower()
    if lower_answer in ('yes', 'y', 'true', 't', '1', 'enable', 'on'):
        return True
    elif lower_answer in ('no', 'n', 'false', 'f', '0', 'disable', 'off'):
        return False

"""event handler when bot activated"""
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

"""event handler when bot got message"""
@bot.event
async def on_message(message):

    # if bot messaged something then ignore it
    # focus on human message only 
    if message.author == bot.user:
        return 

    # useful command
    """
    if message.content == '/cleanup':
        if message.author.guild_permissions:
            await message.channel.purge()
            await message.channel.send('')
        else:
            await message.channel.send('How do you want to do?')
    """
    
    await bot.process_commands(message)

@bot.command(name="cleanup")
async def command_cleanup(ctx):
    if ctx.author.guild_permissions:
        print(f"Guild: {ctx.guild}\nChannel: {ctx.channel}\nAuthor: {ctx.author}")
        
        await ctx.reply("Delete everything!")
    else:
        await ctx.reply("How do you want to do?")

@bot.command(name="maxim")
async def command_maxim(ctx):
    quote = get_quote()
    await ctx.reply(quote)

@bot.command(name="ping")
async def command_ping(ctx):
    await ctx.reply("Pong!")

@bot.command(name="greet")
async def command_greet(ctx, *name):
    if len(name) == 0:
        await ctx.reply("Hello, everyone.")
    else:
        names = ', '.join(name)
        await ctx.reply(f"Hello, {names}.")

@bot.command(name="neko")
async def command_neko(ctx):
    await ctx.reply("myao!")



TOKEN = ''
with open('token_id.txt', 'r') as token:
    TOKEN = token.read()
bot.run(TOKEN)
