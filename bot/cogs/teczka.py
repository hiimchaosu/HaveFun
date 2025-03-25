import nextcord
import random

from nextcord.ext import commands
from pathlib import Path

SIXTY = "potwierdzam"

class aktaHF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teczka", description="Check the archives of HF")
    async def teczkaCommand(self, ctx):
        dowody = [p.stem for p in Path(".").glob("./images/teczka/*")]
        choice = random.randint(0, len(dowody)-1)

        file = nextcord.File(f"./images/teczka/{dowody[choice]}.jpg", filename=f"{dowody[choice]}.jpg")
        embed = nextcord.Embed()
        embed.set_author(name=f"Akta HF - {dowody[choice]}")
        embed.set_image(url=f"attachment://{dowody[choice]}.jpg")
        await ctx.send(file=file, embed=embed)

    @commands.Cog.listener("on_message")
    async def manIsSixty(self, ctx):
        ctx.content = ctx.content.lower().replace(' ', '')
        if SIXTY in ctx.content:
            await ctx.add_reaction("<a:POLICE:927849013628268545>")
            await ctx.channel.send("Co robisz?<:gun:668879124554579988>")


def setup(bot):
    bot.add_cog(aktaHF(bot))