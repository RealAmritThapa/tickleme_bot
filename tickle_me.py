
import os
import openai
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('MY_TOKEN')
SERVER= os.getenv('MY_SERVER')
openai.api_key = os.getenv('OPEN_AI_KEY')
openai.Model.list()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

def generate_response(prompt):
    response= openai.Completion.create(
        model= "text-davinci-003",
        prompt= prompt,
        max_tokens= 200,
        top_p= 1,
        temperature= 0.3,
        frequency_penalty= 0,
    )
    return response.choices[0].text

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
    
    user_message = message.content.lower()
    if "tickleme gpt" in user_message:
        user_message = user_message.strip("tickleme gpt")
        response = str(generate_response(user_message))
        if response:
            await message.channel.send(response)
        else:
            await message.channel.send("fuck")
    if "tickleme yell" in user_message:
        user_message = user_message.replace("tickleme yell", '')
        print(user_message)
        if "me" in user_message:
            user_message = "eat a lumpy dick " + str(message.author.display_name)
            if user_message:
                await message.channel.send(user_message)
        else:

            user_message = "fuck you " + str(user_message)
            print(user_message)
            if user_message:
                await message.channel.send(user_message)
    

client.run(TOKEN)

