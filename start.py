import discord
import asyncio
import aiohttp
import json
import random
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from pprint import pprint

TOKEN = 'NDk4NTE2NzgyNDM3MzY3ODA4.DqFGVg.hue467MO0Y_1_4wDpgzQeV0edSE'

description = '''Bot de qualitay'''
bot = commands.Bot(command_prefix='#',description=description)


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='vec mon frein'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='QuiEstTonMaitre',
                aliases=['quiesttonmaitre', 'whosurmaster', 'tonmaitre', 'QuiEstLePlusBeau', 'quiestleplusbeau'])
async def QuiEstTonMaitre():
    """Le soumis"""
    await bot.say("Vous, Maitre")

@bot.command(name='Bowsette',
                aliases=['bowsette', 'bgette', 'Bgette', 'Désirée', 'désirée', 'desiree', 'Desiree'])
async def Bowsette():
    """Bowsette la bgette"""
    await bot.say("https://media.giphy.com/media/5n7rMuIpPJk4wvrzUv/giphy.gif")

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
        'Probable/20',
        'Définitivement',
        'AYAAA non',
        'Demande à Anto',
        'POST OU CANCER :smiling_imp:',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command(name='bitcoin',
                aliases=['btc'],)
            
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
    
@bot.command(name='Dé',
                description="Lance un dé à 6 faces.",
                brief="Lance un dé.",
                aliases=['LeDé', 'dé'],
                pass_context=True)
async def Dé(context):
    possible_responses = [
        "1",
        '2',
        '3',
        '4',
        '5',
        '6',
        'Le dé est tombé par terre',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
@bot.command()
async def fois(left : float, right : float):
    """Multiplie deux nombres ensembles."""
    await bot.say(left * right)
    
    
@bot.command(name='IlaCru',
                aliases=['pd', 'aya', 'mytho', 'salemerde', 'noublipas', 'tacrumdr'])
async def IlaCru():
    """Noublipas"""
    await bot.say("https://media.discordapp.net/attachments/493077049251069972/500038544673472518/IMG_20180929_073327.jpg")
    
def user_is_me(ctx):
    return ctx.message.author.id == "268526642530353153" 

@bot.command(pass_context = True)
@commands.check(user_is_me)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

def user_is_issuisse(ctx):
    return ctx.message.author.id == "385318295068213258" 

@bot.command(pass_context = True)
@commands.check(user_is_issuisse)
async def aya():
    mesg = 'http://image.noelshack.com/fichiers/2016/42/1477217760-epicjesus.gif '
    return await bot.say(mesg)

                 
bot.run(TOKEN)        
