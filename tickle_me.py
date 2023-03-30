
import os
import openai
import discord
from dotenv import load_dotenv
from discord.ext import commands 

load_dotenv()

TOKEN = os.getenv('MY_TOKEN')
SERVER= os.getenv('MY_SERVER')
openai.api_key = os.getenv('OPEN_AI_KEY')
openai.Model.list()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

def generate_response(prompt):
    response= openai.Completion.create(
        model= "text-davinci-003",
        prompt= prompt,
        max_tokens= 200,
        top_p= 1,
        temperature= 0.7,
        frequency_penalty= 0,
    )
    return response.choices[0].text

def generate_image(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
    )
    return response['data'][0]['url']
    
@bot.event 
async def on_ready():
    for guild in bot.guilds:
        if guild.name == SERVER:
            break
    print(f'{bot.user.name} has connected to Discord')
 
@bot.command()
async def draw (ctx, prompt):
    response = generate_image(prompt)
    if response:
        await ctx.send(response)

@bot.command()
async def ask(ctx, *message):
    message = ' '.join(message)
    print(message)
    response = generate_response(message)
    if response:
        await ctx.send(response)
    
bot.run(TOKEN)

