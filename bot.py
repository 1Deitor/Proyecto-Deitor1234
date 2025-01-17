import discord
from discord.ext import commands
#from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            fileurl = attachment.url
            await attachment.save(f'./img/{attachment.filename}')
            await ctx.send(f'Imagen guardada {attachment.filename}')
            await ctx.send('listo')
            #await ctx.send(get_class(model_path="./modelo/keras_model.h5", labels_path="./modelo/labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send('Olvidaste subir la imagen :(')


bot.run("MTMyNTIyMDM0MTc4NTY5MDI0NQ.G83EjW.Eby1DYgFXHHuqkMmTZxQawBejuOxyjrAf-WjIc")