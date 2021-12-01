import logging
from discord.ext import commands

class botLogger(commands.Cog):
    def __init__(self, client):
        self.client = client
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

def setup(client):
    client.add_cog(botLogger(client))