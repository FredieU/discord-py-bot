# Discord Bot Template

A template repo to set up a Discord bot with [Discord.py](https://discordpy.readthedocs.io/en/stable/index.html).

## Set up

Create a [Python virtual environment](https://docs.python.org/3/library/venv.html) and install the dependencies

```
pip install -r requirements.txt
```

[Create a Discord application](https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro) on Discord's Developer Portal along with a Bot user to obtain a token to authenticate the Discord.py client

Set this token as an environment variable (`DISCORD_BOT_TOKEN`) on your machine (or as any other name but amending bot.py accordingly)

```
DISCORD_BOT_TOKEN=<token>
```

Run the bot

```
python bot.py
```