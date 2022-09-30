import discord
import os

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
  if message.content.startswith('!hi'):
    await message.channel.send('Hello!')


client.run(os.environ['TOKEN'])