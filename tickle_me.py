
import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('MY_TOKEN')
SERVER= os.getenv('MY_SERVER')
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event 
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break

    
    print(f'{client.user.name} has connected to Discord')
    for member in guild.members:
        print(f'{member.name}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content == 'hi':
        response = "hi I am tickle"
        await message.channel.send(response)
client.run(TOKEN)

