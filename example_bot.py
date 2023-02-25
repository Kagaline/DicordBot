import discord
import os
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


async def reply(message):
    # reply message
    reply = f'({message.author.mention} called me?)'
    
    # send reply
    await message.channel.send(reply) 

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

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if client.user in message.mentions:
        await reply(message)

TOKEN = ''
with open('token_id.txt', 'r') as token:
    TOKEN = token.read()
client.run(TOKEN)
