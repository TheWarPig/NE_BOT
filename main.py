import discord
import asyncio
import os
from replit import db
from keep_alive import keep_alive

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)


@client.event
async def on_ready():
  print('We Have logged in as: {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = str(message.content).lower()
  if message.content.startswith('!hi'):
    author = str(message.author)
    await message.channel.send('Hello ' + author.split("#")[0] + '!')
  if msg[:3] == 'ne ' or msg == 'ne' or msg == 'ne?':
    await asyncio.sleep(5)
    await message.channel.send('NENENENENENENENENENENENE')
  if msg[:4] == 'any ' or msg == 'any' or msg == 'any?':
    await asyncio.sleep(5)
    await message.channel.send('ANYANYANYANYANYANYANYANYANY')


keep_alive()
client.run(os.environ['TOKEN'])
