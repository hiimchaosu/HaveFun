import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def brek(self, message):
        brek_find = message.content
        brek_find.lower().replace(' ', '')
        if 'widziszmnie?' in brek_find:
            await message.channel.send("Widzeee {0}".format(message.author.mention),
                                       file=discord.File('/app/images/brek.jpeg'))
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
