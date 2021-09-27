import discord
import os

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('remotely'):
    await message.channel.send('Hello there!')

client.run(BOT_TOKEN)