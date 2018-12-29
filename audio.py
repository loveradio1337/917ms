import discord
import asyncio
import platform
import colorsys
import youtube_dl
import os
import time
import datetime
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find
from discord import Game, Embed, Color, Status, ChannelType

cc = 0xC72323
bot = commands.Bot(command_prefix='>')
bot.remove_command('help')
from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
opts = {
    'default_search': 'auto',
    'quiet': True,
}  # youtube_dl options



load_opus_lib()
in_voice=[]
servers_songs={}
player_status={}
now_playing={}
song_names={}
paused={}

async def set_player_status():
    for i in bot.servers:
        player_status[i.id]=False
        servers_songs[i.id]=None
        paused[i.id]=False
        song_names[i.id]=[]
    print("lets go boy.")



async def bg():
    bot.loop.create_task(set_player_status())


@bot.event
async def on_ready():
    bot.loop.create_task(bg())
    print(bot.user.name)


@bot.event
async def on_reaction_add(react,user):
    pass


async def check_voice(con):
    pass


async def queue_songs(con,clear):
    if clear == True:
        song_names[con.message.server.id].clear()
        await bot.voice_client_in(con.message.server).disconnect()
        player_status[con.message.server.id] = False

    if clear == False:

        if len(song_names[con.message.server.id])==0:
            servers_songs[con.message.server.id]=None

        if len(song_names[con.message.server.id]) !=0:
            song=await bot.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: bot.loop.create_task(after_song(con, False)))
            servers_songs[con.message.server.id]=song
            servers_songs[con.message.server.id].start()
            await bot.delete_message(now_playing[con.message.server.id])
            embed=discord.Embed(color=cc)
            embed.description="Playing the :notes: ``{}`` - Now.".format(servers_songs[con.message.server.id].title)
            msg=await bot.send_message(con.message.channel,embed=embed)
            now_playing[con.message.server.id]=msg

            if len(song_names[con.message.server.id]) >= 1:
                song_names[con.message.server.id].pop(0)


        if len(song_names[con.message.server.id]) ==0 and servers_songs[con.message.server.id] == None:
            player_status[con.message.server.id]=False
        

async def after_song(con,clear):
    bot.loop.create_task(queue_songs(con,clear))
    bot.loop.create_task(check_voice(con))


@bot.command(pass_context=True)
async def queue(con):
    embed=discord.Embed(color=cc)
    embed.set_author(name="Queue")
    embed.description="There are {} audios in queue".format(len(song_names))
    await bot.say(embed=embed)

@bot.command(aliases=["p"],pass_context=True)
async def play(con,*,url):
    await bot.say(f":mag_right: **Searching** for `{url}`")

        if bot.is_voice_connected(con.message.server) == False:
            await bot.join_voice_channel(con.message.author.voice.voice_channel)
        if bot.is_voice_connected(con.message.server) == True:
            if player_status[con.message.server.id]==True:
                song_names[con.message.server.id].append(url)
                await bot.send_message(con.message.channel, "☑ | The audio ``{}`` is queued".format(url.title))
            if player_status[con.message.server.id]==False:
                player_status[con.message.server.id]=True
                song_names[con.message.server.id].append(url)
                song=await bot.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: bot.loop.create_task(after_song(con,False)))
                servers_songs[con.message.server.id]=song
                servers_songs[con.message.server.id].start()
                embed=discord.Embed(color=cc)
                embed.description="Playing :notes: `{}` - Now".format(now_playing[con.message.server.id].title)
                msg = await bot.send_message(con.message.channel, embed=embed)
                now_playing[con.message.server.id]=msg
                song_names[con.message.server.id].pop(0)




@bot.command(aliases=["s"],pass_context=True)
async def skip(con):

    if servers_songs[con.message.server.id]== None or len(song_names[con.message.server.id])==0 or player_status[con.message.server.id]==False:
        await bot.send_message(con.message.channel,"**❎ | There no songs left on the queue due to last song to skip**")
    if servers_songs[con.message.server.id] !=None:
        servers_songs[con.message.server.id].pause()
        bot.loop.create_task(queue_songs(con,False))



@bot.command(pass_context=True)
async def join(con,channel=None):

    voice_status = bot.is_voice_connected(con.message.server)

    if voice_status == False:
        await bot.join_voice_channel(con.message.author.voice.voice_channel)
        embed=discord.Embed(color=cc)
        embed.description="☑ | I just joined in the voice channel."
        await bot.say(embed=embed)
    if voice_status == True:
        await bot.send_message(con.message.channel, "**☑ | The bot is already connected to a voice channel.**")



@bot.command(pass_context=True)
async def leave(con):
        
    if bot.is_voice_connected(con.message.server) == False:
        await bot.send_message(con.message.channel,"**❎ | The bot is not connected to a voice channel**")

    if bot.is_voice_connected(con.message.server) == True:
        embed=discord.Embed(color=cc)
        embed.description="☑ | I left on the voice channel."
        await bot.say(embed=embed)
        bot.loop.create_task(queue_songs(con,True))

@bot.command(pass_context=True)
async def pause(con):

    if servers_songs[con.message.server.id]!=None:
        if paused[con.message.server.id] == True:
            await bot.send_message(con.message.channel,"**☑ | The audio already paused.**")
        if paused[con.message.server.id]==False:
            embed=discord.Embed(color=cc)
            embed.description="**☑ | The audio is paused.**"
            await bot.say(embed=embed)
            servers_songs[con.message.server.id].pause()
            paused[con.message.server.id]=True

@bot.command(pass_context=True)
async def resume(con):

    if servers_songs[con.message.server.id] != None:
        if paused[con.message.server.id] == False:
            await bot.send_message(con.message.channel,"**☑ | The audio already playing**")
        if paused[con.message.server.id] ==True:
            embed=discord.Embed(color=cc)
            embed.description="**☑ | The audio is resumed.**"
            await bot.say(embed=embed)
            servers_songs[con.message.server.id].resume()
            paused[con.message.server.id]=False

@bot.command(aliases=["vol"],pass_context=True)
async def volume(con, vol:float):
    volu = float(vol)
    servers_songs[con.message.server.id].volume=volu
    embed=discord.Embed(color=cc)
    embed.description=f"The audio volume is set to **{vol}**"
    await bot.say(embed=embed)

bot.run(os.environ['BOT_TOKEN'])