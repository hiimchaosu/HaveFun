import discord
from discord.ext import commands

class botCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def help(self, ):

def setup(client):
    client.add_cog(botCommands(client))