
# Coco bot V2

# Import

import discord

from discord.ext import commands

from discord.ext.commands import Bot

import youtube_dl

import random

from os import environ

import asyncio

import time

import random

import datetime

import math

import requests


import random


import datetime

import math

import sys

import base64

import hashlib

import traceback

import string

import inspect

import json

import aiohttp

import websockets

import urllib.request

import logging

from collections import Counter

import os

import colorsys

import socket

from lxml import html
import asyncio
import time
import random
import datetime
import math
import requests
import sys
import base64
import hashlib
import traceback
import string
import inspect
import json

import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket




# Prefix


bot = Bot(description="Coco BOT is best", command_prefix=">")

players = ()

print(f"Connecting your bot to discord!")





# Variables


copyright = "Copyright © 2018 Coco"


OWNER_ID = "351390806101327883"


noperm = "Sorry but you do not have permission to use that command!"


botid = "507241518524923904"



lines = "3.5k+"


if_statements = "Undefined"


else_statements = "Undefined"


total_commands = str(len(bot.commands))


total_embeds = "154"


total_variables = "Undefined"


total_imports = "Undefined"


total_dogs = "872"

DMs = "```I just wrote 📝 you the information, Please check your DMs 💌```"



total_links = "Undefined"



total_dad_jokes = "382"


changelogs = "To view the change log please use the command `>changelog`"


no_work = f"This command is currently not working, Please DM Coco#6429 about the command so he can fix this issue"


user = 'Coco#6429'


key = 'q8Di3LCIL0Qny7IiwN3jxfyBuY37c9nk'



secondnoperm = "You probally have no permission to use this command or i don't have permission to do what you want me to do"


botavatar = "https://cdn.discordapp.com/avatars/507241518524923904/d17a39fdd2440df7a59dd86e3a78fafd.webp?size=1024"









dbl_url = "https://discordbots.org/api/bots/507241518524923904/stats"






#chatbot = ChatBot 'Coco BOT',


 #   storage_adapter='chatterbot.storage.SQLStorageAdapter',


  #  trainer='chatterbot.trainers.ChatterBotCorpusTrainer',


   # #input_adapter='chatterbot.input.TerminalAdapter',


    ##output_adapter='chatterbot.output.TerminalAdapter',


    #logic_adapters=[


     #   'chatterbot.logic.MathematicalEvaluation',


    #    'chatterbot.logic.TimeLogicAdapter',


     #   "chatterbot.logic.BestMatch"


    #],


    #database='./database.sqlite3',


#)





# Remove help


bot.remove_command('help')



async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='>help | Coco#6429', type=2))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='with '+str(len(set(bot.get_all_members())))+' users | >help | Coco#6429'))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='in '+str(len(bot.servers))+' servers | >help | Coco#6429', type=3))
        await asyncio.sleep(5)



# On ready


@bot.event


async def on_ready():





    print(f'Ready')
    print(f"[][][][][][][][][][][][][][][][][][][][][][][][][][]")
    print(f'Coco BOT IS ONLINE')
    print(f'Lets play')

    bot.loop.create_task(status_task())


# Userinfo


@bot.command(pass_context=True)


async def userinfo(ctx, user: discord.Member):


    embed = discord.Embed(title="{}'s information".format(user.name), color=0xD2DCE5)


    embed.add_field(name="👤 __Name__ 👤", value=user.mention, inline=True)


    embed.add_field(name="🎫 __ID__ 🎫", value=user.id, inline=True)


    embed.add_field(name="🔮 __Status__ 🔮", value=user.status, inline=True)


    embed.add_field(name="📉 __Highest Role__ 📉", value=user.top_role)


    embed.add_field(name="📈 __Joined__ 📈", value=user.joined_at.strftime("%d %b %Y %H:%M"))


    embed.add_field(name="⚒ __Created__ ⚒", value=user.created_at.strftime("%d %b %Y %H:%M"))


    embed.add_field(name="💉 __Color__ 💉", value=user.color)


    embed.add_field(name="🤖 __Bot__ 🤖", value=str(user.bot))


    embed.add_field(name="🕹 __Playing__ 🕹", value=user.game)


    embed.add_field(name="🎲 __Discord Tag__ 🎲", value=user.discriminator)


    embed.add_field(name="📋 __Nickname__ 📋", value=user.nick)


    embed.add_field(name="📊 __Server__ 📊", value=user.server)





    try:


            roles = [x.name for x in user.roles if x.name != "@everyone"]





            if roles:


                roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy


                                           if x.name != "@everyone"].index)


                roles = ", ".join(roles)


            else:


                roles = "None"


            embed.add_field(name="📌 __Roles__ 📌", value=roles)


    except:


        pass





    embed.set_thumbnail(url=user.avatar_url)


    await bot.say(embed=embed)





# Botinfo


@bot.command(pass_context=True)


async def botinfo(ctx):

    embed = discord.Embed(title="Coco BOTs information", color=0xD2DCE5)


    embed.add_field(name="__Bot Name__", value="Coco BOT")


    embed.add_field(name="__Bot Tag__", value="9026")


    embed.add_field(name="__Bot ID__", value=botid)


    embed.add_field(name="__Bot Owner__", value="Coco#6429")


    embed.add_field(name="__Bot Prefix__", value=">")

    embed.add_field(name="__Bot Language__", value="Python")


    embed.add_field(name="__Bot Servers__", value=len(bot.servers))


    embed.add_field(name="__Bot Users__", value=(len(set(bot.get_all_members()))))


    embed.add_field(name="__Bot Commands__", value=(str(len(bot.commands))))


    embed.add_field(name="__Bot Invite__", value="[👉 Invite my bot HERE 👈]( https://discordapp.com/api/oauth2/authorize?client_id=507241518524923904&,permissions=8&scope=bot)")

    embed.add_field(name="__Donation Link__", value="[Support our bot by Donating us HERE](https://paypal.me/CocoGT)")

    embed.set_thumbnail(url=botavatar)


    await bot.say(embed=embed)

# Serverinfo


@bot.command(pass_context=True)


async def serverinfo(ctx):

    server = ctx.message.server


    online = len([m.status for m in ctx.message.server.members


                    if m.status == discord.Status.online or


                    m.status == discord.Status.idle])





    embed = discord.Embed(name="{} Server information".format(ctx.message.server.name), color=0xffe5f3)


    embed.add_field(name="__Server name__", value=ctx.message.server.name, inline=True)


    embed.add_field(name="__Owner__", value=ctx.message.server.owner.mention)


    embed.add_field(name="__Server ID__", value=ctx.message.server.id, inline=True)


    embed.add_field(name="__Roles__", value=len(ctx.message.server.roles), inline=True)


    embed.add_field(name="__Members__", value=len(ctx.message.server.members), inline=True)


    embed.add_field(name="Online", value=f"**{online}/{len(ctx.message.server.members)}**")


    embed.add_field(name="__Created at__", value=ctx.message.server.created_at.strftime("%d %b %Y %H:%M"))


    embed.add_field(name="__Emojis__", value=f"{len(ctx.message.server.emojis)}/100")


    embed.add_field(name="__Server Region__", value=str(ctx.message.server.region).title())


    embed.add_field(name="__Total Channels__", value=len(ctx.message.server.channels))


    embed.add_field(name="__AFK Channel__", value=str(ctx.message.server.afk_channel))


    embed.add_field(name="__AFK Timeout__", value=ctx.message.server.afk_timeout)


    embed.add_field(name="__Verification Level__", value=ctx.message.server.verification_level)


    try:


        embed.add_field(name="__Role Names__", value=", ".join([role.name for role in ctx.message.server.roles if role.name != "@everyone"]))


    except:


        pass


    embed.set_thumbnail(url=ctx.message.server.icon_url)


    await bot.say(embed=embed)

# Restart


@bot.command(pass_context=True)


async def bot_restart(ctx):


    if ctx.message.author.id == OWNER_ID:


        embed = discord.Embed(title="Coco BOT is restarting...", color=0x008484)


        msg = await bot.say(embed=embed)


        await asyncio.sleep(2)


        em = discord.Embed(title="Coco BOT we will back!", color=0x008484)


        await bot.edit_message(msg, embed=em)


        quit()


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Servers


@bot.command(pass_context=True)


async def servers(ctx):


    if ctx.message.author.id == OWNER_ID:


        nl = "\n"


        stringy = ""


        for server in bot.servers:


            stringy += f"{server.name} : `{server.id}`{nl}"


        await bot.send_message(ctx.message.author, stringy)


        for server in bot.servers:


            await bot.send_message(ctx.message.author, f"{server.name}  :  `{server.id}`")


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Kick


@bot.command(pass_context=True)


async def kick(ctx, user: discord.Member):


    if ctx.message.author.server_permissions.kick_members:


        embed = discord.Embed(title="Successfully kicked {} from ".format(user.name) + (ctx.message.server.name), color=0x96bef0)


        await bot.kick(user)


        await bot.say(embed=embed)


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Ban


@bot.command(pass_context=True)


async def ban(ctx, user: discord.Member):


    if ctx.message.author.server_permissions.ban_members:


        embed = discord.Embed(title="Successfully banned {} from ".format(user.name) + (ctx.message.server.name), color=0xff6666)


        await bot.ban(user)


        await bot.say(embed=embed)


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)



# Invite

@bot.command(pass_context=True)


async def invite(ctx):


    embed = discord.Embed(title="Please support Coco BOT", color=0xD2DCE5)


    embed.add_field(name="Bot Invite", value="[👉 Invite my bot HERE 👈]( https://discordapp.com/api/oauth2/authorize?client_id=507241518524923904&,permissions=8&scope=bot)")

    embed.add_field(name="Donation Link", value="[Support our bot by Donating us HERE](https://paypal.me/CocoGT)")

    embed.set_thumbnail(url=botavatar)

    await bot.say(embed=embed)





# Membercount


@bot.command(pass_context=True)


async def membercount(ctx):


    embed = discord.Embed(title="The total amount of members in {}".format(ctx.message.server.name), description=len(ctx.message.server.members), color=0xD2DCE5)


    embed.set_thumbnail(url=ctx.message.server.icon_url)


    await bot.say(embed=embed)





# Servercount


@bot.command(pass_context=True)


async def servercount(ctx):


    embed = discord.Embed(title="Server Counter", description=len(bot.servers), color=0xD2DCE5)


    await bot.say(embed=embed)


# Avatar


@bot.command(pass_context=True)


async def avatar(ctx, user: discord.Member):


    embed = discord.Embed(title="This is the avatar of {}".format(user.name), color=0xfff799)


    embed.set_image(url=user.avatar_url)


    await bot.say(embed=embed)






# Slow Clear


# Slow Purge
@bot.command(pass_context=True)
async def slowvlear(ctx):
    try:
        if ctx.message.author.server_permissions.manage_messages:
            async for msg in bot.logs_from(ctx.message.channel):
                await bot.delete_message(msg)
        else:
            emd = discord.Embed(title=noperm, color=0xD2DCE5)
            await bot.say(embed=emd)
    except Exception as e:
        await bot.say(e)
# Warn



@bot.command(pass_context=True)



async def warn(ctx, member : discord.Member = None, *, message):


    if ctx.message.author.server_permissions.ban_members:


        if member == "@everyone":


            await bot.send_message(member, message)


        else:


            await bot.send_message(member, "Warning From {} Admins : ".format(ctx.message.server.name) + message)


        await bot.send_message(ctx.message.author, "Successfully warned *{}*".format(member.mention))


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Dm


@bot.command(pass_context=True)


async def dm(ctx, member : discord.Member = None, *, message):


    if ctx.message.author.id == OWNER_ID:


        if member == "@everyone":


            await bot.send_message(member, message)


        else:


            await bot.send_message(member, message)


        await bot.send_message(ctx.message.author, "Successfully dmed *{}*".format(member.mention))


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Decide


@bot.command(pass_context=True)


async def decide(ctx):


    if ctx.message.author.server_permissions.kick_members:


        decided = ["Ban him", "Kick him", "Do whatever you wanna do!"]


        embed = discord.Embed(title=random.choice(decided), color=0xff9c9c)


        await bot.say(embed=embed)


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Secret ban


@bot.command(pass_context=True)


async def secretban(ctx, user: discord.Member = None):


    if ctx.message.author.server_permissions.ban_members:


        if user == None:


            await bot.send_message(ctx.message.author, "```Proper usage is\n\n>secretban <mention a user to secretly ban```>")


        else:


            await bot.ban(user)


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





# Secret kick


@bot.command(pass_context=True)


async def secretkick(ctx, user: discord.Member = None):


    try:


        if ctx.message.author.server_permissions.kick_members:


            if user == None:


                await bot.send_message(ctx.message.author, "Proper usage is\n\n>secretkick <mention a user to secretly kick>")


            else:


                await bot.kick(user)


        else:


            emd = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.send_message(ctx.message.author, e)





# Say


@bot.command(pass_context=True)


async def say(ctx, *, what_to_say : str):

    await bot.say(what_to_say)





# Embed


@bot.command(pass_context=True)


async def embed(ctx, *, what_to_say : str):


    colors = [0x7a58d4, 0xff0027, 0x00fff2, 0x00ff09, 0xb5fff8, 0xb5b8ff, 0xffc300, 0xff99b8]


    randomizer = random.choice(colors)


    embed2 = discord.Embed(title=f"{ctx.message.author.name} Said : ", description=what_to_say, color=randomizer)


    await bot.delete_message(ctx.message)


    await bot.say(embed=embed2)





# QR Code


@bot.command(pass_context=True)


async def qr(ctx, *, message: str):


    new_message = message.replace(" ", "+")


    url = f"http://api.qrserver.com/v1/create-qr-code/?data={new_message}"





    embed = discord.Embed(color=0xe73131)


    embed.set_image(url=url)


    await bot.say(embed=embed)





# Google


@bot.command(pass_context=True)


async def google(ctx, *, message):


    new_message = message.replace(" ", "+")


    url = f"https://www.google.com/search?q={new_message}"


    await bot.say(url)





# Youtube


@bot.command(pass_context=True)


async def youtube(ctx, *, message: str):


    new_message = message.replace(" ", "+")


    url = f"https://www.youtube.com/results?search_query={new_message}"





    await bot.say(url)






# 8ball
@bot.command(aliases=['8ball'], pass_context=True)
async def ask(ctx, *, question: str):
    answer = [":8ball: It is certain.", ":8ball: It is decidedly so.", "Without a doubt.", ":8ball:Yes definitely.", ":8ball: You may rely on it.", ":8ball: As I see it, yes.", ":8ball: Most likely.", ":8ball:Outlook good.", ":8ball: Yes.", ":8ball:Signs point to yes.", ":8ball: Reply hazy, try again.", ":8ball: Ask again later.", ":8ball: Better not tell you now.", ":8ball: Cannot predict now.", ":8ball:Concentrate and ask again.", ":8ball: Don't count on it.", ":8ball: My reply is no.", ":8ball: My sources say no.", ":8ball:Outlook not so good.", ":8ball: Very doubtful."]
    randomizer = random.choice(answer)
    embed = discord.Embed(title=question, description=f"{randomizer}", color=0xefff00)
    await bot.say(embed=embed)

#@bot.command(pass_context=True)
#async def 8ball(ctx, *, question: str):

    #answer = [":8ball: It is certain.", ":8ball: It is decidedly so.", "Without a doubt.", ":8ball:Yes definitely.", ":8ball: You may rely on it.", ":8ball: As I see it, yes.", ":8ball: Most likely.", ":8ball:Outlook good.", ":8ball: Yes.", ":8ball:Signs point to yes.", ":8ball: Reply hazy, try again.", ":8ball: Ask again later.", ":8ball: Better not tell you now.", ":8ball: Cannot predict now.", ":8ball:Concentrate and ask again.", ":8ball: Don't count on it.", ":8ball: My reply is no.", ":8ball: My sources say no.", ":8ball:Outlook not so good.", ":8ball: Very doubtful."]

    #randomizer = random.choice(answer)


    #embed = discord.Embed(title=question, description=f"{randomizer}", color=0xefff00)


    #await bot.say(embed=embed)


# Hug


@bot.command(pass_context=True)


async def hug(ctx, user: discord.Member):


    if user.id == ctx.message.author.id:


        await bot.say("{} Wanted to hug his self, good luck on that you will look like an idiot trying to do it".format(user.mention))


    else:


        if user.id == botid:


            await bot.say("You will turn into a metal if you hug me")


        else:


            randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]


            embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color=0xafeeee)


            embed.set_image(url=random.choice(randomurl))


            await bot.say(embed=embed)





# Gender


@bot.command(pass_context=True)


async def gender(ctx, user: discord.Member):


    random.seed(user.id)


    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database xD"]


    randomizer = random.choice(genderized)


    if user == ctx.message.author:


        embed = discord.Embed(title="You should know your own gender", color=0xfff47d)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(color=0xfff47d)


        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")


        await bot.say(embed=embed)





# FBI


@bot.command(pass_context=True)


async def fbi(ctx):


    msg = await bot.say("Contacting the FBI")


    await asyncio.sleep(2)


    await bot.edit_message(msg, "```Successfully contacted the FBI```")


    await asyncio.sleep(1)


    msg2 = await bot.say(f"Looking for {ctx.message.author.mention}'s home address")


    await asyncio.sleep(2)


    await bot.edit_message(msg2, "```Successfully found the home address``|")


    msg3 = await bot.say(f"Sending the FBI to {ctx.message.author.mention}'s house")


    await asyncio.sleep(1)


    msg4 = await bot.say(f"According to my calculations it will take about 5 seconds before the FBI gets to {ctx.message.author.mention}'s house")


    await asyncio.sleep(5)


    await bot.edit_message(msg3, "FBI Sent!")


    await bot.edit_message(msg4, "Ok it is now done!")


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "The FBI is here")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "Please put your hands up in the air while we investigate your internet browser")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "Don't f*cking MOVE!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "If you move you are going to die!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "Ok we have successfully investigated your internet browser and we found out you have some p*rn in your history\nplease consider coming with us")





# Joke


@bot.command(pass_context=True)


async def joke(ctx):


    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]


    embed = discord.Embed(color=0x5e72a2)


    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))


    await bot.say(embed=embed)





# Dadjoke


@bot.command(pass_context=True)


async def dadjoke(ctx):


    dadjoke = ["Why did the girl show her boobs to the paper factory?\nTo make flash paper", "My dad literally told me this one last week: 'Did you hear about the guy who invented Lifesavers? They say he made a mint.", "A ham sandwich walks into a bar and orders a beer. Bartender says, 'Sorry we don't serve food here.", "Me: 'Dad, make me a sandwich!' Dad: 'Poof, You’re a sandwich!'", "Why did the Clydesdale give the pony a glass of water?  Because he was a little horse!", "How do you make a Kleenex dance? Put a little boogie in it!", "Two peanuts were walking down the street. One was a salted.", "What time did the man go to the dentist? Tooth hurt-y.", "I'm reading a book about anti-gravity. It's impossible to put down!", "You're American when you go into the bathroom, and you're American when you come out, but do you know what you are while you're in there? European.", "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.", "Want to hear a joke about a piece of paper? Never mind... it's tearable.", "I just watched a documentary about beavers. It was the best dam show I ever saw!", "If you see a robbery at an Apple Store does that make you an iWitness?", "Spring is here! I got so excited I wet my plants!", "A ham sandwich walks into a bar and orders a beer. The bartender says, 'Sorry we dont serverserver food here.", "What’s Forrest Gump’s password? 1forrest1", "Why did the Clydesdale give the pony a glass of water?  Because he was a little horse!", "Did you hear about the guy who invented Lifesavers? They say he made a mint.", "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!", "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans!", "What do you call a factory that sells passable products? A satisfactory.", "How do you make a Kleenex dance? Put a little boogie in it!", "When a dad drives past a graveyard: Did you know that's a popular cemetery? Yep, people are just dying to get in there!", "Two peanuts were walking down the street. One was a salted.", "Why did the invisible man turn down the job offer? He couldn't see himself doing it.", "I used to have a job at a calendar factory but I got the sack because I took a couple of days off.", "How do you make holy water? You boil the hell out of it.", "When you ask a dad if he's alright: 'No, I’m half left.'", "I had a dream that I was a muffler last night. I woke up exhausted!", "Did you hear the news? FedEx and UPS are merging. They’re going to go by the name Fed-Up from now on.", "5/4 of people admit that they’re bad with fractions.", "MOM : How do i look?\nDad : With your eyes.", "What is Beethoven’s favorite fruit? A ba-na-na-na.", "Two guys walk into a bar, the third one ducks.", "What do you call a masturbating cow? Beef Stroganoff.", "Did you hear about the circus fire? It was in tents!", "Don't trust atoms. They make up everything!", "What do you call a cow with two legs? Lean beef. If the cow has no legs, then it’s ground beef.", "What do you get when you cross an elephant with a rhino? Elephino.", "How many tickles does it take to make an octopus laugh? Ten-tickles.", "I’m only familiar with 25 letters in the English language. I don’t know why.", "What's the best part about living in Switzerland? I don't know, but the flag is a big plus."]


    embed = discord.Embed(color=0x20bb2a)


    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(dadjoke))


    await bot.say(embed=embed)


    async with aiohttp.botSession(headers={"Accept": "application/json"}) as cs:


        async with cs.get('https://icanhazdadjoke.com/') as r:


            res = await r.json()


            embed = discord.Embed(description=res['joke'], color=0xf45f5f)


            await bot.say(embed=embed)





# Skincolor


@bot.command(pass_context=True)


async def skincolor(ctx, user: discord.Member):


    random.seed(user.id)


    skins = ["White", "Black", "Blue", "Green", "Rainbow", "Purple", "Brown", "Pink", "Cream", "Orange"]


    if user == ctx.message.author:


        embed2 = discord.Embed(title="You should know your own skin color", color=0xcb287a)


        await bot.say(embed=embed2)


    else:


        embed = discord.Embed(color=0xcb287a)


        embed.add_field(name=f"{user.name}'s skin color", value=random.choice(skins))


        await bot.say(embed=embed)

# Encode


@bot.command(pass_context=True)


async def encode(ctx, *, encode_to: str):


    try:


        encoded = hashlib.md5(encode_to.encode('utf-8')).hexdigest()


        await bot.say(embed=discord.Embed(color=0xD2DCE5, title=f"{encode_to} has been encoded to md5 results are below",


                                        description=f"{encoded}"))


    except Exception as e:


        await bot.say(f"Could not encode.\n`{e}`")


async def clear(ctx, amount = 1000):


    if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == OWNER_ID:


        mgs = [] #Empty list to put all the messages in the log


        number = int(amount) #Converting the amount of messages to delete to an integer


        async for x in bot.logs_from(ctx.message.channel, limit=int(amount) +1):


            mgs.append(x)


        await bot.delete_messages(mgs)
        await bot.say(str(amount) + ' messages got deleted...')

    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)

# sapnupuas


@bot.command(pass_context=True)


async def sapnupuas(ctx):


    embed = discord.Embed(color=0xD2DCE5)


    embed.add_field(name="Meanwhile in Mccdonald's secret area", value=f"{ctx.message.author.name} : hai gerl ples kiss 1 fut penus and show vagen ples\n\nHailey : You wanna see what?\n\n{ctx.message.author.name} : ples bobs vagen insert 1 fut penus big and fell good\n\nHailey : Sorry i cannot understand you, please fix your english\n\n{ctx.message.author.name} : I came from a different planet and i am here to tell you that we are all going to die and there is only one way to survive and you will have to send me a picture of your boobs and vagina so that we won't die please send it right now, i don't want to die")


    await bot.say(embed=embed)



# number


@bot.command(pass_context=True)


async def randomint(ctx):


    embed = discord.Embed(color=0x67f413)


    rand = "{}".format(str(random.randint(0, 100)))


    embed.add_field(name="Here's a random number from 0 to 100", value=rand)


    await bot.say(embed=embed)





# Custom integer


@bot.command(pass_context=True)


async def customint(ctx, first: int, second: int):


    embed = discord.Embed(color=0xcf8fff)


    rand = "{}".format(str(random.randint(first, second)))


    embed.add_field(name=f"Here's a random number from {first} to {second}", value=rand)


    await bot.say(embed=embed)





# Howgay
@bot.command(pass_context=True)
async def howgay(ctx, user: discord.Member = None):
    random.seed(user.id)
    if user.id == OWNER_ID:
        embed = discord.Embed(color=0xbef482)
        embed.add_field(name=f"{user.name}'s Howgay results", value="1% Gay")
        await bot.say(embed=embed)
    else:
        if user.id == "335460741958336512":
            embed = discord.Embed(color=0xbef482)
            embed.add_field(name=f"{user.name}'s Howgay results", value="100000000% Gay")
            await bot.say(embed=embed)
        else:
            if user.id == "327072337432150036":
                embed = discord.Embed(color=0xbef482)
                embed.add_field(name=f"{user.name}'s Howgay results", value="Not Gay At All")
                await bot.say(embed=embed)
            else:
                if user.id == "316181702391365632":
                    embed = discord.Embed(color=0xbef482)
                    embed.add_field(name=f"{user.name}'s Howgay results", value="The howgay results cannot be detected beacause that user has a gender that is out of this world.")
                    await bot.say(embed=embed)
                else:
                    embed = discord.Embed(color=0xbef482)
                    randomizer = "{}% Gay".format(str(random.randint(20, 100)))
                    embed.add_field(name=f"{user.name}'s Howgay results", value=randomizer)
                    await bot.say(embed=embed)






# Embedcode


@bot.command(pass_context=True)


async def embedcode(ctx):


    embed = discord.Embed(title="burger king foot lettuce", url="https://example.com", description="yo mam prety", color=0xD2DCE5)


    embed.set_author(name="black guy", url="http://example.com", icon_url="https://i.imgflip.com/1jqcf8.jpg?a422784")


    embed.set_thumbnail(url="https://i.imgflip.com/1jqcf8.jpg?a422784")


    embed.add_field(name="miss me with that pro", value="-elon musk 2025", inline=True)


    embed.set_footer(text="ples no normes allowed")


    await bot.say('```py\nembed=discord.Embed(title="burger king foot lettuce", url="https://example.com", description="yo mam gey", color=0xD2DCE5)\n'


                                                        'embed.set_author(name="black guy", url="http://example.com", icon_url="https://i.imgflip.com/1jqcf8.jpg?a422784")\n'


                                                        'embed.set_thumbnail(url="https://i.imgflip.com/1jqcf8.jpg?a422784")\n'


                                                        'embed.add_field(name="miss me with that pro", value="-elon musk 2025", inline=True)\n'


                                                        'embed.set_footer(text="ples no normes allowed")\n'


                                                        'await bot.say(embed=embed)```')


    await bot.say(embed=embed)





# Codeinfo


@bot.command(pass_context=True)


async def codeinfo(ctx):


    embed = discord.Embed(title="Coco's Code Info!", color=0x7fff0d)


    embed.add_field(name="📃__Lines__", value=lines)


    embed.add_field(name="📋__Total Commands__", value=(str(len(bot.commands))))


    embed.add_field(name="📊__Total Embeds__", value=total_embeds)


    embed.add_field(name="📑__Total Variables__", value=total_variables)


    embed.add_field(name="📥__Total Imports__", value=total_imports)


    embed.add_field(name="📈__Total Links__", value=total_links)

    embed.add_field(name="🚹__Total Dad Jokes__", value=total_dad_jokes)



    await bot.say(embed=embed)



# Hack


@bot.command(pass_context=True)


async def hack(ctx, user: discord.Member):


    discord_password = "qwerty1301MOANA"


    computer_login = "Satursay"


    facebook = "Dooms Day Date"


    msg = await bot.say("Starting LEET Hack tool")


    await asyncio.sleep(1)


    msg2 = await bot.edit_message(msg, "Starting LEET Hack tool [")


    await asyncio.sleep(1)


    msg3 = await bot.edit_message(msg2, "Starting LEET Hack tool [ ]")


    await asyncio.sleep(1)


    msg4 = await bot.edit_message(msg3, "Starting LEET Hack tool [ ][")


    await asyncio.sleep(1)


    msg5 = await bot.edit_message(msg4, "Starting LEET Hack tool [ ][ ]")


    await asyncio.sleep(1)


    msg6 = await bot.edit_message(msg5, "Starting LEET Hack tool [ ][ ][")


    await asyncio.sleep(1)


    msg7 = await bot.edit_message(msg6, "Starting LEET Hack tool [ ][ ][ ]")


    await asyncio.sleep(1)


    msg8 = await bot.edit_message(msg7, "Starting LEET Hack tool [ ][ ][ ][")


    await asyncio.sleep(1)


    msg9 = await bot.edit_message(msg8, "Starting LEET Hack tool [ ][ ][ ][ ]")


    msg10 = await bot.edit_message(msg9, "___Success to run the hack tool___!")


    msg11 = await bot.say(f"Im looking for {user.mention}'s discord password from the discord database")


    await asyncio.sleep(3)


    await bot.edit_message(msg11, f"**Success to found {user.mention}'s discord password from the discord database**")


    msg12 = await bot.say(f"Im looking for {user.mention}'s computer login details")


    await asyncio.sleep(3)


    await bot.edit_message(msg12, f"**Success to found {user.mention}'s computer login details**")


    msg13 = await bot.say(f"Im looking for {user.mention}'s facebook login details from the facebook database, this might take some time")


    await asyncio.sleep(5)


    await bot.edit_message(msg13, f"**Success i found {user.mention}'s facebook login details**")



    await bot.say(f"You won't belive on what i found, I am sending all information i got from {user.mention} to you")

    await asyncio.sleep(3)


    await bot.send_message(ctx.message.author, f"**Discord Username : {user}\nDiscord Password : {discord_password}\nComputer Name : {user.name}-PC\nComputer Password : {computer_login}\nFacebook Username : {user.name} The Gamer\nFacebook Password : {facebook}**")

    await bot.say("Sending...")
    await asyncio.sleep(5)


    await bot.say("I successfully sent the information to you!")


# String generator


@bot.command(pass_context=True)


async def stringgen(ctx, n: int=None):


    if n==None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>stringgen <Give a number>```")


    else:


        if n is 1023:


            await bot.say("*Discord doesn't like that amount, Please consider going lower**")


        else:


            generator_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(n))


            embed = discord.Embed(color=0xc0c5ff)


            embed.add_field(name="__String Generator__", value=generator_string)


            await bot.say(embed=embed)



# Bomb


@bot.command(pass_context=True)


async def bomb(ctx, user: discord.Member = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>bomb <mention a user>```")

    else:


        await bot.say(f":bomb: Planting a bomb to {user.mention}'s account! :bomb:")


        await asyncio.sleep(3)


        await bot.send_message(user, f"{ctx.message.author.name} Have planted a bomb on your account, the bomb will detonate in 5 seconds")


        await bot.say("Bomb has been planted!\n")


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 10 seconds")


        await asyncio.sleep(9)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 3 seconds")


        await asyncio.sleep(3)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 3 seconds")


        await asyncio.sleep(3)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 10 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 9 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 8 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 7 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 6 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 5 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 4 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 3 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 2 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 1 seconds")


        await asyncio.sleep(1)


        await bot.say(":boom: Bomb has exploded :boom:")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")

# G-Ban


@bot.command(pass_context=True)


async def gban(ctx, user: discord.Member, *, reason: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.ban(user)


        embed = discord.Embed(title=f"Successfully banned {user.name} from {ctx.message.server.name}", description=f"Reason : {reason}", color=0x890fe3)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=embed)

# G-Kick


@bot.command(pass_context=True)


async def gkick(ctx, user: discord.Member, *, reason: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.kick(user)


        embed = discord.Embed(title=f"Successfully kicked {user.name} from {ctx.message.server.name}", description=f"Reason : {reason}", color=0x890fe3)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=embed)





# Slap


@bot.command(pass_context=True)


async def slap(ctx, user: discord.Member = None):


    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")


    else:


        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color=0xc7ff00)


        embed.set_image(url=random.choice(gifs))


        await bot.say(embed=embed)

# Report


@bot.command(pass_context=True)


async def report(ctx, user: discord.Member = None, *, reason: str = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>report <user to report> <reason of why you are reporting him>```")


    else:


        if reason == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>report <user to report> <reason of why you are reporting him>```")


        else:


            server = bot.get_server("510339939162914826")


            chan = bot.get_channel("520901548575031296")


            embed = discord.Embed(title=f"{ctx.message.author.name}'s Report", color=0xc0c5ff)


            embed.add_field(name="Reported User", value=f"Username : {user}\n"


                                                        f"User ID : {user.id}\n"


                                                        f"User Server : {ctx.message.server.name}\n"


                                                        f"Server ID : {ctx.message.server.id}\n"


                                                        f"Channel Name : {ctx.message.channel.name}\n"


                                                        f"Channel ID : {ctx.message.channel.id}\n"


                                                        f"Server Members : {len(ctx.message.server.members)}")


            embed.add_field(name="User Reporter", value=f"Username : {ctx.message.author}\n"


                                                        f"User ID {ctx.message.author.id}\n"


                                                        f"Channel Name : {ctx.message.channel.name}\n"


                                                        f"Channel ID : {ctx.message.channel.id}")


            embed.add_field(name="Reason", value=reason)


            await bot.send_message(chan, embed=embed)


            await bot.say(f"Successfully reported {user} with the reason of {reason}")





# Whois


@bot.command(pass_context=True)


async def whois(ctx, user: discord.Member = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is \n\n>whois <mention a user>```")


    else:


        lolwho = ["Is a worker at Mcdonalds", "Is the person staring at you right now", "Is behind you", "Is your mom", "Is your dad",
                  "Is the random guy you see in the streets everyday", "Is your past life", "Is me", "Is the person who took your virginity",
                  "Is the guy who get all the bitches", "Is gay", "Is a boy", "Is a girl", "Is about to die", "Is retarded", "Hates you",
                  "Is the guy next to your house", "Is the guy who stole your girl"]

        random.seed(user.id)

        embed = discord.Embed(title=f"{user.name} {random.choice(lolwho)}", color=0xD2DCE5)


        await bot.say(embed=embed)


# RollDice


@bot.command(pass_context=True)


async def rolldice(ctx):


    dice = ["1", "2", "3", "4", "5", "6"]


    embed = discord.Embed(title=f"{ctx.message.author.name} Just rolled the dice and got {random.choice(dice)}", color=0xeed27b)


    await bot.say(embed=embed)





# Dye Hair


@bot.command(pass_context=True)


async def hairdye(ctx, user: discord.Member = None, *, color: str = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>hairdye <mention a user> <color>```")


    else:


        if color == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>hairdye <mention a user> <color>```")


        else:


            if user.id == ctx.message.author.id:


                em = discord.Embed(title=f"{ctx.message.author.name} Just dyed his/her own hair {color}", color=0xD2DCE5)


                await bot.say(embed=em)


            else:


                if user.id == botid:


                    em = discord.Embed(title="You cannot dye a robot's hair", color=0xD2DCE5)


                    await bot.say(embed=em)


                else:


                    em = discord.Embed(title=f"{ctx.message.author.name} Just dyed {user.name}'s hair {color}", color=0xD2DCE5)


                    await bot.say(embed=em)




@bot.command(pass_context=True)


async def start(ctx):


    if ctx.message.author.id == OWNER_ID:

        for repeat in range(2):


            await bot.say(f"Bot Servers : {len(bot.servers)}")

            await bot.say(f"Bot Users : {len(bot.users)}")
    else:


        embed = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=embed)


@bot.command(pass_context=True)


async def height(ctx, user: discord.Member = None):


    try:


        choices = ["6 Foot 10 Inches", "3 Foot 9 Inches", "9 Foot 5 Inches", "He's so short you can't see him", "6 Foot 2 Inches", "4 Foot 2 Inches", "1 Foot 1 Inches", "12 Foot 7 Inches", "37 Foot 62 Inches", "12 Foot 23 Inches", "2 Foot 8 Inches", "69 Foot 21 Inches", "13 Foot 37 Inches"]


        randomizer = random.choice(choices)


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>height <mention a user>```")


        else:


            if user.id == OWNER_ID:


                random.seed(user.id)


                embed = discord.Embed(color=0xfff47d)


                embed.add_field(name=f"{user.name}'s height results", value="1337 Cm")


                await bot.say(embed=embed)


            else:


                if user == ctx.message.author:


                    await bot.say("You're so short your pet is even taller than you")


                else:


                    embed = discord.Embed(color=0xfff47d)


                    embed.add_field(name=f"{user.name}'s height results", value=randomizer)


                    await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

# damn

@bot.command(pass_context=True)
async def damn(ctx):
    embed = discord.Embed(title="DAMNNNNNNNN!!", color=0xf45f5f)
    embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

# burned

@bot.command(pass_context=True)
async def burned(ctx):
    embed = discord.Embed(color=0xD2DCE5)
    embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)



# Talent Check


@bot.command(pass_context=True)
async def talentcheck(ctx, user: discord.Member = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>talentcheck <mention a user>```")


    else:


        if user.id == OWNER_ID:


            try:


                embed = discord.Embed(title=f"Here is the special talent of {user.name}", description="He can't be gay", color=0xD2DCE5)


                await bot.say(embed=embed)


            except Exception as e:


                await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


        else:


            if user == ctx.message.author:


                try:


                    embed = discord.Embed(color=0xD2DCE5)


                    embed.add_field(name=f"Here is your special talent {user.name}", value=f"You must know your talent")


                    await bot.say(embed=embed)


                except Exception as e:


                    await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


            else:


                if user.id == botid:


                    await bot.say("I have no talents at all :(")


                else:


                    try:


                        embed = discord.Embed(color=0xD2DCE5)


                        embed.add_field(name=f"Here is the special talent of {user.name}", value=f"{user.name} Can Read")


                        await bot.say(embed=embed)


                    except Exception as e:


                        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

# shoot

@bot.command(pass_context=True)


async def shoot(ctx, user: discord.Member = None):


    try:


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>shoot <mention a user>```")


        else:


            if user == ctx.message.author:


                images2 = ['https://media.giphy.com/media/GrdvdNF9cuRrO/giphy.gif', 'https://media.giphy.com/media/oW1egQoq8su4M/giphy.gif', 'https://media1.tenor.com/images/abcdc3fdefc7510bab0c8e8a64b37c91/tenor.gif?itemid=4975230', 'https://media1.tenor.com/images/b9ebfbf0e8060ab57071dea8e537b05c/tenor.gif?itemid=5922988']
                embed = discord.Embed(title='{} Just commited suicide'.format(ctx.message.author.name), color=0xeed27b)

                embed.set_image(url=random.choice(images2))
                await bot.say(embed=embed)
            else:
                if user.id == botid:


                    images3 = ['https://media1.tenor.com/images/a0080e72de83e209ea7bb22acc0aab61/tenor.gif?itemid=5437253', 'https://thereadingfangirl.files.wordpress.com/2015/12/grant-catching-bullet.gif', 'https://i.imgur.com/YcX7DND.gif',]


                    embed = discord.Embed(title=f"You can't shoot me, Because im bot", color=0xeed27b)


                    embed.set_image(url=random.choice(images3))


                    await bot.say(embed=embed)


                else:


                    images = ['https://media.giphy.com/media/S4DbvGJggL0pG/giphy-downsized-large.gif', 'https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif', 'http://share.gifyoutube.com/ztj.gif', 'http://78.media.tumblr.com/9da6bcfae89e27e6cbd7f9b660dc5f97/tumblr_nbi8wlLPIr1rarngto3_400.gif', 'http://bestanimations.com/Military/Weapons/gun-with-silencer-shooting-gif.gif', 'https://i.gifer.com/JkKb.gif']


                    embed = discord.Embed(title=f'{user.name} Just got shot by {ctx.message.author.name}', color=0xeed27b)


                    embed.set_image(url=random.choice(images))


                    await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


# lenny


@bot.command(pass_context=True)


async def lenny(ctx):


    try:


        lennyfaces = ['http://i0.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg', 'https://i.imgur.com/EdhFIeB.png', 'https://res.cloudinary.com/teepublic/image/private/s--KmxdS0R1--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1449351547/production/designs/359654_1.jpg', 'https://i.ytimg.com/vi/4Foi6YIaMgc/maxresdefault.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWOOYLu8oxiLNuKCfH3_vnz4dO5nm1ahTZQjiJCMhkl0tXmHLK']


        embed = discord.Embed(color=0xD2DCE5)


        embed.add_field(name="Boi we got da lenny", value="xD")


        embed.set_thumbnail(url=random.choice(lennyfaces))


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def botsearch(ctx, *, sulta: str = None):


    try:


        if sulta == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>botsearch <Name of a bot>```")


        else:


            new_message = sulta.replace(" ", "+")


            urllol = f'https://discordbots.org/search?q={new_message}'


            embed = discord.Embed(title="Is this what you're lookin for?", description=urllol, color=0xfff47d)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")




@bot.command(pass_context=True)


async def topbots(ctx):


    try:


        embed = discord.Embed(title="Here are the Top discord bots", description="1. [Pokécord](https://discordbots.org/bot/365975655608745985?)\n"


                "2. [Dank Memer](https://discordbots.org/bot/270904126974590976?)\n"


                "3. [BoxBot](https://discordbots.org/bot/413728456942288896?)\n"


                "4. [pbot](https://discordbots.org/bot/218921854662868993?)\n"


                "5. [Nadeko](https://discordbots.org/bot/116275390695079945?)\n"


                "6. [Miki](https://discordbots.org/bot/160105994217586689?)\n"


                "7. [OwO](https://discordbots.org/bot/408785106942164992?)\n"


                "8. [Pancake](https://discordbots.org/bot/239631525350604801?)\n"


                "9. [UnbelievaBoat](https://discordbots.org/bot/292953664492929025?)\n"


                "10. [Sinon](https://discordbots.org/bot/277234960807755776?)\n", color=0xD2DCE5)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")




@bot.command(pass_context=True)


async def thicccheck(ctx, user: discord.Member = None):


    try:


        thiccness = ["Very THICC i'd smash", "Not THICC at all", "9999999% THICC", "40% THICC", "100% THICC", "1% THICC"]


        random.seed(user.id)


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>thicccheck <mention a user>```")


        else:


            if user.id == OWNER_ID:


                embed = discord.Embed(title=f"{user.name}'s THICC Check results", description="Ultra THICC", color=0xD2DCE5)


                await bot.say(embed=embed)


            else:


                embed = discord.Embed(title=f"{user.name} THICC Check results", description=random.choice(thiccness), color=0xD2DCE5)


                await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def serverowner(ctx):


    try:


        user = ctx.message.server.owner


        embed = discord.Embed(title="Here are the information about the server owner", color=0xD2DCE5)


        embed.add_field(name="👤 __Name__ 👤", value=user.mention)


        embed.add_field(name="📝 __ID__ 📝", value=user.id, inline=True)


        embed.add_field(name="📊 __Status__ 📊", value=user.status, inline=True)


        embed.add_field(name="📈 __Highest Role__ 📉", value=user.top_role)


        embed.add_field(name="📆 __Joined__ 📆", value=user.joined_at.strftime("%d %b %Y %H:%M"))


        embed.add_field(name="⚒ __Created__ ⚒", value=user.created_at.strftime("%d %b %Y %H:%M"))


        embed.add_field(name="🎆 __Color__ 🎆", value=user.color)


        embed.add_field(name="🎮 __Playing__ 🎮", value=user.game)


        embed.add_field(name="⚛ __Discord Tag__ ⚛", value=user.discriminator)





        try:


                roles = [x.name for x in user.roles if x.name != "@everyone"]





                if roles:


                    roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy


                                               if x.name != "@everyone"].index)


                    roles = ", ".join(roles)


                else:


                    roles = "None"


                embed.add_field(name="__Roles__", value=roles)


        except:


            pass





        embed.set_thumbnail(url=user.avatar_url)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    embed = discord.Embed(
        title = 'Voice channel',
        description = 'commands for the voice channel.',
        colour = discord.Colour.blue()
    )

    embed.add_field(name = '>play', value = '>play (Youtube link to music)', inline = True)
    embed.add_field(name = '>pause', value = 'pauses audio', inline = True)
    embed.add_field(name = '>resume', value = 'resumes audio', inline = True)
    embed.add_field(name = '>leave', value = 'leave voice channel', inline = True)

    await bot.say(embed=embed)
    await bot.join_voice_channel(channel)


@bot.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    await voice_bot.disconnect()


@bot.command(pass_context = True)
async def play(ctx, url):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    player = await voice_bot.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@bot.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@bot.command(pass_context = True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()


@bot.command(pass_context=True)


async def statcheck(ctx, user: discord.Member = None):


    try:


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>statcheck <mention a user>```")


        else:


            embed = discord.Embed(title=f"{user.name}'s current status", description=f"{user.status}", color=0xD2DCE5)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def gamecheck(ctx, user: discord.Member = None):


    try:


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>gamecheck <mention a user>```")


        else:


            embed = discord.Embed(title=f"{user.name}'s current game", description=f"{user.game}", color=0xf6c63d)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def vote(ctx):


    try:


        embed = discord.Embed(color=0x7a58d4)


        embed.add_field(name="Wanna vote for Coco BOT? Here's the link for that", value="https://discordbots.org/bot/507241518524923904/vote")


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")




@bot.command(pass_context=True)


async def channelinfo(ctx):


    try:


        embed = discord.Embed(title=f"Information about {ctx.message.channel.name}", color=0xcb287a)


        embed.add_field(name="🕺 __Name__ 👤", value=ctx.message.channel.name)


        embed.add_field(name="💠 __Server__ 💠", value=ctx.message.channel.server)


        embed.add_field(name="🎫 __ID__ 🎫", value=ctx.message.channel.id)


        embed.add_field(name="📋 __Position__ 📋", value=ctx.message.channel.position)


        embed.add_field(name="📆 __Created__ 📆", value=ctx.message.channel.created_at.strftime("%d %b %Y %H:%M"))


        embed.set_thumbnail(url=ctx.message.server.icon_url)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def membernames(ctx):


    try:


        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)


        await bot.send_message(ctx.message.author, embed=embed)


    except:


        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color=0xD2DCE5)


        await bot.say(embed=embed)





@bot.command(pass_context=True)


async def docs(ctx):


    await bot.say("http://discordpy.readthedocs.io/en/latest/api.html#version-related-info")





@bot.command(pass_context=True)


async def nick(ctx, user: discord.Member = None, *, changed: str = None):


    try:


        if ctx.message.author.server_permissions.manage_nicknames:


            if user == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n >nick <mention a user> <new nickname>```")





            if changed == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n >nick <mention a user> <new nickname>```")





            else:


                embed = discord.Embed(description=f"Successfully changed {user.mention}'s nickname from {user.name} to {changed}", color=0x96bef0)


                await bot.say(embed=embed)


                await bot.change_nickname(user, changed)


        else:


            emd = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")








@bot.command(pass_context=True)


async def logout(ctx):


    if ctx.message.author.id == OWNER_ID:


        embed = discord.Embed(title="Successfully logged out of discord", color=0xD2DCE5)


        await bot.say(embed=embed)


        await bot.logout()


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





@bot.command(pass_context=True)


async def slowmode(ctx, val: str = None):


    try:


        if ctx.message.author.server_permissions.manage_messages:


            if val == None:


                embed = discord.Embed(description="To start the slow mode simply type in `>slowmode on`.\nTo stop the slow mode simply type in `>slowmode off`", color=0xD2DCE5)


                await bot.say(embed=embed)


            else:


                if val == "on":


                    embed = discord.Embed(title="Successfully started slow mode", desciprtion=f"{ctx.message.channel.mention} Is now in slow mode, To stop please simply type `>slowmode off`", color=0x20bb2a)


                    await bot.say(embed=embed)


                    for x in range(999999999999999999999):


                        mag = await bot.wait_for_message(author=None, channel=ctx.message.channel, content=None)


                        if ctx.message.author.id == botid:


                            return


                        else:


                            await asyncio.sleep(0.60)


                            await bot.delete_message(mag)


                        if mag.content == ">slowmode off":


                            if mag.author.server_permissions.manage_messages:


                                break


                        else:


                            continue


                else:


                    await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel, content=">slowmode on")


                    if val == "off":


                        embed = discord.Embed(title="Successfully stopped slow mode", color=0xD2DCE5)


                        await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=emd)





    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def textchannel(ctx, *, name: str = None):


    try:


        if ctx.message.author.server_permissions.manage_channels or ctx.message.author.id == OWNER_ID:


            if name == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>textchannel <channel name>```")


            else:


                the_channel = await bot.create_channel(ctx.message.server, name=name)


                embed = discord.Embed(description=f"Successfully created the channel {the_channel.mention}", color=0x00fff2)


                await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=emd)





    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(aliase=['config_slowmode'], pass_context=True)


async def cslowmode(ctx, stopat: int = None, timeout: int = None, chan: discord.Channel = None, *, custommsg: str = None):


    if ctx.message.author.server_permissions.manage_messages:


        if stopat == None:


            await bot.say(f"{ctx.message.author.mention} ```Please read the proper usage of this command\n\nmessages read: Stops the slow mode when it reads a specific amount of messages\ncustom message: Sends a message every time a message is detected and deleted (You can leave it empty)\ntimeout: Stops when the bot doesn't detect a message in x seconds\nchannel: Enables the slow mode for the mentioned channel \n\n>config_slowmode <messages read> <timeout> <channel> <custom message>```")


        if custommsg == None:


            embed = discord.Embed(description=f"Successfully enabled the custom slow mode with the given settings\nStops at {stopat} messages deleted\nCustom message given : None\nGiven Timeout : {timeout}\nStarted at {chan.mention}\n\nTo stop simply type in `>config_slowmode off` in the given slow mode channel", color=0xb39e0d)


            await bot.say(embed=embed)


            for x in range(stopat):


                msg = await bot.wait_for_message(timeout=timeout, author=None, channel=chan, content=None)


                if ctx.message.author.id == OWNER_ID:


                    return


                else:


                    await asyncio.sleep(0.60)


                    await bot.delete_message(msg)


                if msg.content == ">config_slowmode off":


                    if msg.author.server_permissions.manage_messages:


                        embed = discord.Embed(title="Successfully stopped the slow mode", color=0x7a58d4)


                        await bot.say(embed=embed)


                        break


                else:


                    continue


        if timeout == None:


            await bot.say(f"{ctx.message.author.mention} ```Please read the proper usage of this command\n\nmessages read: Stops the slow mode when it reads a specific amount of messages\ncustom message: Sends a message every time a message is detected and deleted (You can leave it empty)\ntimeout: Stops when the bot doesn't detect a message in x seconds\nchannel: Enables the slow mode for the mentioned channel \n\n>config_slowmode <messages read> <timeout> <channel> <custom message>```")


        if chan == None:


            await bot.say(f"{ctx.message.author.mention} ```Please read the proper usage of this command\n\nmessages read: Stops the slow mode when it reads a specific amount of messages\ncustom message: Sends a message every time a message is detected and deleted (You can leave it empty)\ntimeout: Stops when the bot doesn't detect a message in x seconds\nchannel: Enables the slow mode for the mentioned channel \n\n>config_slowmode <messages read> <timeout> <channel> <custom message>```")
        else:
            embed = discord.Embed(description=f"Successfully enabled the custom slow mode with the given settings\nStops at {stopat} messages deleted\nCustom message given : {custommsg}\nGiven Timeout : {timeout}\nStarted at {chan.mention}\n\nTo stop simply type in `>config_slowmode off` in the given slow mode channel", color=0xb39e0d)
            await bot.say(embed=embed)
            for x in range(stopat):
                msg = await bot.wait_for_message(timeout=timeout, author=None, channel=chan, content=None)
                await bot.send_message(chan, custommsg)
                if ctx.message.author.id == botid:
                    return
                else:
                    await asyncio.sleep(0.60)
                    await bot.delete_message(msg)
                if msg.content == ">config_slowmode off":
                    if msg.author.server_permissions.manage_messages:


                        embed = discord.Embed(title="Successfully stopped the slow mode", color=0x7a58d4)


                        await bot.say(embed=embed)


                        break


                else:


                    continue


    else:


        emd = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=emd)





@bot.command(pass_context=True)


async def voicechannel(ctx, *, name: str = None):


    try:


        if ctx.message.author.server_permissions.manage_channels:


            if name == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>voicechannel <name of the channel you wanna make>```")


            else:


                await bot.create_channel(ctx.message.server, name, type=discord.ChannelType.voice)


                embed = discord.Embed(description="Successfully created the voice channel {}".format(name), color=0xcb287a)


                await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


@bot.command(pass_context=True)


async def amplify(ctx, *, message: str):


    try:


        if ctx.message.author.id == OWNER_ID:


            i = ctx.message.server.members


            await bot.say("Are you sure you wanna continue? Type `yes` if yes")


            await bot.wait_for_message(timeout=0.01, author=ctx.message.author, content="yes")


            for x in range(1000000000000000000000000000):




                await bot.say(message)





            for member in i:


                try:


                    print(f"Successfully named {member.name} to {message}")


                    await bot.change_nickname(member, message)


                except:


                    pass


        else:


            embed = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def renamerole(ctx, *, roled: discord.Role = None):


    try:


        if ctx.message.author.server_permissions.manage_roles:


            if roled == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renamerole <mention a role>\n\nMake sure capitalization and everything else is correct```")


            else:


                embed = discord.Embed(description=f"Please type in the new name for the role {roled.mention}\nExample : `gay role`", color=0x00ff8c)


                await bot.say(embed=embed)


                msg = await bot.wait_for_message(author=ctx.message.author, content=None)


                embed = discord.Embed(title=f"Successfully renamed the role from {roled.name} to {msg.content}", color=0x6000ff)


                await bot.say(embed=embed)


                await bot.edit_role(ctx.message.server, role=roled, name=msg.content)


        else:


            embed = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=embed)


    except:


        await bot.say("**I probally do not have the `Manage Roles` permission or the role that you're trying to rename is higher than my current role.**")





@bot.command(pass_context=True)


async def emojis(ctx):


    try:


        lol = ctx.message.server


        embed = discord.Embed(title=f"Emojis for {ctx.message.server.name}. Total emojis : {len(lol.emojis)}", description="\n".join([str(xd) for xd in lol.emojis]), color=0x17e170)


        await bot.send_message(ctx.message.author, embed=embed)


        await bot.say("Successfully sent you the emojis, Check your dms")


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def renameserver(ctx, *, nigga: str = None):


    try:


        if ctx.message.author.server_permissions.manage_server:


            if nigga == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renameserver <new name for the server>```")


            else:


                await bot.edit_server(ctx.message.server, name=nigga)


                embed = discord.Embed(title=f"Successfully renamed this server to {nigga}", color=0x49daff)


                await bot.say(embed=embed)


        else:


            embed = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


@bot.command(pass_context=True)


async def renamechannel(ctx, channeled: discord.Channel = None, *, newname: str = None):


    try:


        if ctx.message.author.server_permissions.manage_channels:


            if channeled == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renamechannel <mention a channel> <new name for the channel>```")


            else:


                if newname == None:


                    await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renamechannel <mention a channel> <new name for the channel>```")


                else:


                    await bot.edit_channel(channel=channeled, name=newname)


                    embed = discord.Embed(description=f"Successfully renamed the channel to {channeled.mention}", color=0x890fe3)


                    await bot.say(embed=embed)


        else:


            embed = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

@bot.command(pass_context=True)


async def autistcheck(ctx, user: discord.Member = None):


    try:


        results = ['Autistic AF', '100% Autistic', '50% Autistic', '28% Autistic', 'Not Autistic', 'Too Autistic For Me', 'Dont even ask, its just too Autistic', 'More Autistic Than You', '69% Autistic', '36% Autistic', '73% Autistic', '99% Autistic', '64% Autistic', 'Autistic Points : 100', '52% Autistic', 'Dont ask me, ask him/her', '420% Autistic']


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>autistcheck <mention a user>```")


        else:


            random.seed(user.id)


            if user.name.upper().startswith('AUTIS'):


                embed = discord.Embed(title=f"{user.name}'s Autistic check results", description="Obviously Autistic, Look At The Name", color=0xD2DCE5)


                await bot.say(embed=embed)


            else:


                if user.id == bot.user.id:


                    embed = discord.Embed(title=f"{user.name}'s Autistic check results", description="Why are you trying to check", color=0xD2DCE5)


                    await bot.say(embed=embed)


                else:


                    if user.id == OWNER_ID:


                        embed = discord.Embed(title=f"{user.name}'s Autistic check results", description="Autism Level : 1337", color=0xD2DCE5)


                        await bot.say(embed=embed)


                    else:


                        embed = discord.Embed(title=f"{user.name}'s Autistic check results", description=random.choice(results), color=0xD2DCE5)


                        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def kickme(ctx, *, reason: str = None):


    try:


        if reason == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>kickme <reason>```")


            return


        if ctx.message.server.id == OWNER_ID:


            return





        await bot.say(f"Are you sure you wanna kick yourself from this server? This is not a joke, once you type 'kick me' it will kick you out of {ctx.message.server.name}")


        mag = await bot.wait_for_message(author=ctx.message.author, content="kick me")

        if ctx.message.author == ctx.message.server.owner or ctx.message.author.id == OWNER_ID:


            await bot.say("Are you drunk? You cannot kick yourself...")


        else:


            await bot.kick(ctx.message.author)


            embed = discord.Embed(description=f"{ctx.message.author.name} Have been successfully kicked from {ctx.message.server.name}\nReason : {reason}")


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")



@bot.command(pass_context=True)


async def editprofile(ctx, *, lol: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.edit_profile(username=lol)


        embed = discord.Embed(description=f"Successfully renamed myself to {lol}", color=0xff0027)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(title=noperm, color=0xD2DCE5)


        await bot.say(embed=embed)





@bot.command(aliases=['userip'], pass_context=True)


async def ipcheck(ctx, *, user: str = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>userip <name a user (do not mention)>``")


        return





    try:


        up = user.upper().startswith


        if user.upper().startswith('NADO'):


            embed = discord.Embed(description="Nadohack's IP : 5.197.89.204", color=0xD2DCE5) #god : 213.226.141.226


            await bot.say(embed=embed)


        elif user.upper().startswith('HAXRIN') or user.upper().startswith('DARKNO') or up('IHEK'):


            embed = discord.Embed(description="Haxrin's IP : 84.42.161.126\nHaxrin is also known as DarkNoobz and iHek", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('ZTZ'):


            embed = discord.Embed(description="ZTzTopia's IP : 139.228.105.1", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('NANO') or up('UNNAMED'):


            embed = discord.Embed(description="Nanoteurz's IP : 41.232.137.189\nNanoteurz is also known as Unnamed GT", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('FINE') or up('REKTY') or up('STRIX') or up('RELUNG') or up('NABDOUCE') or up('RELUNG') or up('THEHUMAN'):


            embed = discord.Embed(description="FineHax's IP : 36.75.114.251\nFineHax is also known as RelungGamer, NabDouce, StrixAgario, TheHumanGT and RektyGT", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('AYOVO'):


            embed = discord.Embed(description="AYOVO's IP : 68.43.158.246", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('NOOB'):


            embed = discord.Embed(description="NoobzGT's IP : 84.25.89.169\nNoobitaz's IP : 85.76.54.34\nNoobitaz is also known as Noobitas and noobhackz", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('HEX'):


            embed = discord.Embed(description="Hexto Gaming's IP : 79.118.37.29", color=0xD2DCE5)


            await bot.say(embed=embed)


        elif up('MRSHAK'):


            embed = discord.Embed(description="MrShakoz's IP : 216.56.81.226", color=0xD2DCE5)


            await bot.say(embed=embed)


        else:


            embed = discord.Embed(description="Cannot find the name in the database\nMaybe check your spelling or do not mention the user you wanna check but instead type their name out", color=0xD2DCE5)


            await bot.say(embed=embed)


    except:


        await bot.say("Do not mention a user, Put in their name instead")





@bot.command(aliases=['yudodis', 'yudothis'], pass_context=True)


async def whyudothis(ctx):


    await bot.delete_message(ctx.message)


    images = ['http://media.tumblr.com/tumblr_m0t255pKb91r5cfgh.gif', 'https://media1.tenor.com/images/5b0eacf23dc1b33e5e4c68c48bee3a69/tenor.gif?itemid=4830853', 'https://thumbs.gfycat.com/EnormousDimpledBadger-max-1mb.gif', 'https://memecrunch.com/meme/8PJWZ/y-u-do-dis/image.gif']


    embed = discord.Embed(color=0xD2DCE5)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





#@bot.command(pass_context=True)


async def approved(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://i.gifer.com/8tuB.gif', 'https://media.tenor.com/images/1490de9f5356d342903ca6a912ffaa07/tenor.gif', 'https://media1.tenor.com/images/13e95668baac397b5e21f20705ef7513/tenor.gif?itemid=7266308', 'https://media1.giphy.com/media/SmoCFhZCi1kzu/giphy.gif']


    embed = discord.Embed(color=0xD2DCE5)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





@bot.command(aliases=['hmmm', 'hmmmm', 'hmmmmm'], pass_context=True)


async def hmm(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://m.popkey.co/6c22a7/X1jdg_f-maxage-0.gif', 'https://media1.tenor.com/images/0e42110c65d57aa0029a291585e200f5/tenor.gif?itemid=5236565', 'https://media.giphy.com/media/kTJnl5gA6cjIc/giphy.gif']


    embed = discord.Embed(color=0xfff47d)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)


@bot.command(pass_context=True)


async def illegalize(ctx, *, legal:str = None):


    if legal == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>illegalize <text>```")


    else:


        """Make Stuff Illegal!"""


        xd = await bot.say(f"Making {legal} Illegal, Just hold on")


        legal = legal.upper()


        url = "https://storage.googleapis.com/is-now-illegal.appspot.com/gifs/" + legal +".gif"


        em = discord.Embed(title="{} Successfully illegalized by president Donald Trump".format(legal), color=0xD2DCE5)


        em.set_footer(text="No image? API Might be broken then")


        em.set_image(url=url)


        await bot.say(embed=em)


        await bot.delete_message(xd)


@bot.command(pass_context=True)


async def emojirename(ctx, emoj: discord.Emoji = None, *, lol: str = None):


    try:


        if ctx.message.author.server_permissions.manage_emojis or ctx.message.author.id == OWNER_ID:


            if lol == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>emojirename <Emoji Name> <New Name>```")


            elif emoj == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>emojirename <Emoji Name> <New Name>```")


            else:


                await bot.edit_custom_emoji(emoji=emoj, name=lol)


                embed = discord.Embed(title="Successfully updated the emoji", color=0xD2DCE5)


                await bot.say(embed=embed)


        else:


            embed = discord.Embed(title=noperm, color=0xD2DCE5)


            await bot.say(embed=embed)


    except:


        await bot.say("An error has occured while updating the emoji.")

@bot.command(pass_context=True)


async def announce(ctx, *, xdd: str = None):


    if ctx.message.author.server_permissions.manage_server or ctx.message.author.id == OWNER_ID:


        await bot.delete_message(ctx.message)


        if xdd == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>announce <Message to announce>```")


        else:


            await bot.send_message(ctx.message.author, f"Currently announcing to {len(ctx.message.server.members)} members\nThis might take some time")


            for member in ctx.message.server.members:


                try:


                    await bot.send_message(member, xdd)


                    print('Successfully sent a message to {}'.format(member.name))


                except:


                    pass


            await bot.send_message(ctx.message.author, "Successfully sent the announcement")


    else:


        embed = discord.Embed(title=noperm, color=0xD2DCE5)


# On-Messages


@bot.event


async def on_message(message):





    if message.content.startswith(">"):


        print(f"{message.author.name} : {message.content}  (Server Name : {message.server.name} : {message.server.id}  {message.channel.id})")





    if message.content.startswith(">secretban"):


        await bot.delete_message(message)


    if message.content.startswith(">say"):


        await bot.delete_message(message)




    if message.content.startswith(">warn"):


        await bot.delete_message(message)





    if message.content.startswith(">dm"):


        await bot.delete_message(message)





    if message.content == ">kick":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>kick <mention a user>```".format(message.author.mention))
    if message.content == ">ban":
        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>ban <mention a user>```".format(message.author.mention))
    if message.content == ">warn":
        await bot.send_message(message.channel, "{} ```Proper usage is\n>warn <mention a user>```".format(message.author.mention))
    if message.content == ">avatar":
        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>avatar <mention a user>```".format(message.author.mention))
    if message.content == ">userinfo":
        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>userinfo <mention a user>```".format(message.author.mention))
    if message.content == ">8ball":
        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>8ball <question>```".format(message.author.mention))
    if message.content == ">magik":
        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>magik <mention a user>```".format(message.author.mention))




    if message.content == ">say":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>say <message>```".format(message.author.mention))





    if message.content == ">embed":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>embed <message>```".format(message.author.mention))





    if message.content == ">qr":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>qr <message>```".format(message.author.mention))

    if message.content == ">encode":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>encode <message>```".format(message.author.mention))





    if message.content == ">google":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>google <what do you wanna search on google>```".format(message.author.mention))





    if message.content == ">youtube":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>youtube <what do you wanna search on youtube>```".format(message.author.mention))





    if message.content == ">kiss":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>kiss <mention a user>```".format(message.author.mention))





    if message.content == ">hug":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>hug <mention a user>```".format(message.author.mention))





    if message.content == ">gender":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>gender <mention a user>```".format(message.author.mention))

    if message.content == ">skincolor":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>skincolor <mention a user>```".format(message.author.mention))





    if message.content == ">clear":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>clear <pick amount of message 1-1000>```".format(message.author.mention))





    if message.content == ">startdox":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>startdox <mention a user>```".format(message.author.mention))





    if message.content == ">customint":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>customint <first number> <second number>```".format(message.author.mention))





    if message.content == ">howgay":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>howgay <mention a user>```".format(message.author.mention))


    if message.content == ">ship":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>ship <mention a user> <mention a second user>```".format(message.author.mention))


    if message.content == ">hack":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>hack <mention a user>```".format(message.author.mention))

    if message.content == ">poll":


        await bot.send_message(message.channel, '{} ```Proper usage is\n\n>poll "Add title" "Option 1" "Option 2" "up to 10 Options only"```'.format(message.author.mention))



    await bot.process_commands(message)


@bot.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await bot.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await bot.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = [ '1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await bot.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await bot.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await bot.edit_message(react_message, embed=embed)


@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '🎊welcome🎊':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'🎉Welcome {member.name} to {member.server.name}🎉', description='Please 🙏 do not forget to read the rules and dont try to break any one of them👼', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**I hope you will be active here.😉**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining here', value=member.joined_at)
            await bot.send_message(channel, embed=embed) 

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '🎊welcome🎊':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Good bye 👋! We will gonna miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**We hope you will be back soon 🙋.**', inline=True)
            embed.add_field(name='**Your join position was**', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await bot.send_message(channel, embed=embed)

@bot.command(pass_context = True)
async def ping(ctx):


    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    embed = discord.Embed(title="Ping!\nPong!", description= "{}ms 🏓".format(round((t2-t1)*1000)), color=0xD2DCE5)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def trumptweet(ctx, *, tet:str = None):
    if tet == None:
        await bot.say(f"{ctx.message.author} ```Proper usage is\n\n>trumptweet <text>```")
    else:
        url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={tet}"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                embed = discord.Embed(color=0xDEADBF)
                embed.set_image(url=res['message'])
                embed.title = "trumptweet.png"
                await bot.say(embed=embed)

@bot.command(pass_context=True)
async def magik(ctx, user: discord.Member = None):
    ssas = user.avatar_url

    url = f"https://nekobot.xyz/api/imagegen?type=magik&image={ssas}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            embed = discord.Embed(color=0xD2DCE5)
            embed.set_image(url=res['message'])
            embed.title = "magik.png"
            await bot.say(embed=embed)

@bot.command(pass_context=True)
async def awooify(ctx, user: discord.Member):
    ssas = user.avatar_url

    url = f"https://nekobot.xyz/api/imagegen?type=awooify&url={ssas}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            embed = discord.Embed(color=0xDEADBF)
            embed.set_image(url=res['message'])
            embed.title = f"{user.name} awooify LOL"
            await bot.say(embed=embed)

@bot.command(aliases=['help_fun', 'help_moderation'], pass_context = True)
async def help_general(ctx):
      await bot.say(DMs)

@bot.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):

    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"

    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            embed = discord.Embed(color=0xDEADBF)
            embed.set_image(url=res['message'])
            embed.title = f"{usernamename} **tweets about** {txt}"
            await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ship(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    ss1 = user.name
    ss2 = user2.name
    usss2 = user.avatar_url
    usss = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={usss2}&user2={usss}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            embed = discord.Embed(title=f"{ss1} ❤ {ss2} Love each others", description=f"Love %\n`{counter_}` **{score}% **\n{finalName}", color=0xDEADBF)
            embed.set_image(url=res['message'])
            await bot.say(embed=embed)


bot.run(os.environ['Token1'])