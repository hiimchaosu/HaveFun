import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def brek(self, message):
        message.content = message.content.lower().replace(' ', '')
        if 'widziszmnie?' in message.content:
            await message.channel.send("Widzeee {0}".format(message.author.mention),
                                       file=discord.File('../images/brek.jpeg'))
    async def kazdyJeden(self, message):
        if "@everyone" in message.content:
            await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention))


async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(Events(bot))
    else:
        await bot.add_cog(
            Events(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
