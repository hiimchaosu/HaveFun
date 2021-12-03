# TODO - React with LIKE under tatsu lvl up message
# TODO - Comment tatsu's lvl up message: "Tatsu jak zwykle z rigczem"
# TODO - jakos to kurwa ladnie napisac

import discord
from discord.ext import commands


class tatsuReaction(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
    @commands.Cog.listener()  # Somehow works, tho throws a small error, to fix later.
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.id == 172002275412279296 and "has leveled up!" in message.content:
            await message.channel.send("{0} jak zwykle z rigczem.".format(message.author.mention))
        if "Widzisz mnie?" in message.content:
            with open("brek.jpeg",'rb') as f:
                picture = discord.File(f)
            await message.channel.send("Widze {0}".format(message.author.mention))
            await message.channel.send(file=picture)

def setup(client):
    client.add_cog(tatsuReaction(client))