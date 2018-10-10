import discord
import asyncio
import aiohttp
import random
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from pprint import pprint

TOKEN = ''

description = '''Bot de merde'''
bot = commands.Bot(command_prefix='#',description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def QuiEstTonMaitre():
    """Le soumis"""
    await bot.say("Vous, Maitre")

@bot.command()
async def add(left : float, right : float):
    """Ajoute deux nombres ensemble."""
    await bot.say(left + right)

@bot.command(name='LeSac',
                description="Réponds à une question par des choses ( ͡° ͜ʖ ͡° ).",
                brief="Répond à tes questions.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def LeSac(context):
    possible_responses = [
        "C'est un non retentissant",
        'Cela semble peu probable',
        'Difficile à dire',
        'Probable',
        'Définitivement',
        'AYAAA',
        'Demande à Anto',
        "Youhou Lama t'es là ? *rip max*",
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await bot.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
        
@bot.command()
async def Maxssio():
    """*Hommage à Maxssio partit trop tot*"""
    await bot.say("YOUHOU MAX, c'est TOI ?! *dit Polo*. "
                  " Tout le monde eut entendu et Max se fit arreter."
                  " Il finira sa vie en prison, pour avoir espionné des cailloux."
                  " La Légende raconte que Max se mit à parler latin en prison, il était devenu 'tou édgi 4 u'")
    
@bot.command()
async def ぴんがす():
    """A jamais malade"""
    await bot.say("Ah, bah il est pas là ¯\_(ツ)_/¯ ")
                 
bot.run(TOKEN)        

