import discord
from discord.ext import commands

class tatsuReaction(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.id == 172002275412279296 and "has leveled up!" in message.content:
            await message.channel.send("{0} jak zwykle z rigczem.".format(message.author.mention))
            await message.add_reaction('<:LIKE:915547952381055036>')
        message.content = message.content.lower().replace(' ','')
        if "widziszmnie?" in message.content:
            with open("brek.jpeg",'rb') as f:
                picture = discord.File(f)
            await message.channel.send("Widzeee {nickname}".format(nickname = message.author.mention), file = picture)

def setup(client):
    client.add_cog(tatsuReaction(client))