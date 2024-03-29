import discord
import asyncio
import os
from threading import Thread
from time import sleep
from keep_alive import keep_alive


def endless_job():
  while True:
    print("p")
    sleep(3000)


job = Thread(target=endless_job)
job.start()

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
  if msg[:3] == 'ok ' or msg == 'ok' or msg == 'ok?':
    await asyncio.sleep(5)
    await message.channel.send('OOOOOOKKKKKKKK!!!!!!!')


keep_alive()
client.run(os.environ['TOKEN'])
