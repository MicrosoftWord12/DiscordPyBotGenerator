import discord
import json
from discord.ext import commands

with open("config.json", 'r') as f:
    config = json.load(f)

bot = discord.Client()
bot = commands.Bot(config["Prefix"], help_command=None)

@bot.event
async def on_ready():
    """
    On Ready Event
    """
    bot.load_extension("TestCommand")
    bot.load_extension("TestEvent")

bot.run(config["Token"])


