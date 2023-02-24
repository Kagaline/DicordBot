import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

"""event handler when bot activated"""
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

"""event handler when bot got message"""
@client.event
async def on_message(message):

    # if bot messaged something then ignore it
    # focus on human message only 
    if message.author == client.user:
        return 

    # useful command
    if message.content == '/cleanup':
        if message.author.guild_permissions:
            await message.channel.purge()
            await message.channel.send('Delete everything!')
        else:
            await message.channel.send('How do you want to do?')

    # sample reactions
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('\\neko'):
        await message.channel.send('myao!')

    if client.user in message.mentions:
        await reply(message)

async def reply(message):
    # reply message
    reply = f'({message.author.mention} called me?)'
    
    # send reply
    await message.channel.send(reply) 

TOKEN = ''
with open('token_id.txt', 'r') as token:
    TOKEN = token.read()
client.run(TOKEN)
