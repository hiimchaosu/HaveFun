import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot online.");

client.run('OTEyNjQ1MTQxMjU5NTEzODc2.YZy9BQ.9vIJ0gI9kZHaXfiJLqqn2Zmgb-M');