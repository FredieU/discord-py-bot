import discord
import os

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
BOT_TRIGGER_KEYWORD = 'remotely'

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(BOT_TRIGGER_KEYWORD):
    await message.channel.send('Hello there!')

client.run(BOT_TOKEN)