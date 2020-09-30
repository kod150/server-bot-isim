from bs4 import BeautifulSoup
import requests
import discord
import pyshorteners
from discord.ext import commands
import datetime
import random


import re

fotolar=["Abi ben nargile tüf tüf","Ben suri ben bilmiyor","Sen istiyor elma  vermek 5 lira "]
bot = commands.Bot(command_prefix='!', description="Herkese Merhaba")
cj=["Ah shit here we go again","i’ll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda.",]
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def topla(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def bilgi(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.add_field(name="Server oluşturma tarihi", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Sahibi", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Bölgesi", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
   

    await ctx.send(embed=embed)



# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Kölelik yapıyor", url="http://www.twitch.tv/accountname"))
    print('Hazır')

@bot.command(pass_context=True)
async def konus(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command(pass_context=True)

async def ayrıl(ctx):
    await ctx.voice_client.disconnect()
@bot.command(pass_context=True)

async def foto(ctx):
    embed = discord.Embed(title=f"Günün Fotoğrafı", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.set_thumbnail(url="https://media.nationalgeographic.org/assets/photos/219/940/a57707f7-9e41-44bd-b60b-1c9d3344a70a.jpg ")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def de(ctx, a: str):
    a.replace("_"," ")
    await ctx.send(a)
@bot.command(pass_context=True)
async def suritaklidi(ctx,):
    a= random.choice(fotolar)

    await ctx.send(a)
@bot.command(pass_context=True)
async def cj_ol(ctx,):
    a=random.choice(cj)

    await ctx.send(a)
@bot.command(pass_context=True)
async def banaparaver(ctx):
    embed = discord.Embed(title=f"Bana Para Ver", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.set_thumbnail(url="https://i.redd.it/hzzcovd6xij31.jpg ")
    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def fiyat(ctx,a: str):
    istek = requests.get(url = a)
    html = istek.text
    veri = BeautifulSoup(html, 'html.parser')
    b=veri.find('span',attrs={'id':'offering-price'}).get_text()
    await ctx.send(b)
@bot.command(pass_context=True)
async def kısalt(ctx,a: str):
    link=a
    kısaltıcı= pyshorteners.Shortener()
    x=kısaltıcı.tinyurl.short(link)
    await ctx.send(x)
@bot.command(pass_context=True)
async def online(ctx):
  online_ppl = ", ".join([str(x) for x in filter(lambda x:x.status == discord.Status.online, ctx.guild.members)])
  await ctx.send(f"online ppl:{online_ppl}")
@bot.command(pass_context=True)
async def amongus(ctx):
  online_ppl = ", ".join([str(x) for x in filter(lambda x:x.status == discord.Status.online, ctx.guild.members)])
  a = random.choice(online_ppl)
  await ctx.send(a)


    

        












bot.run('NzQ4NTI1MjgwMTU0NDg0NzM2.X0esfQ.kihPFmRZNNRHHbmuFclmDuvqNp4')