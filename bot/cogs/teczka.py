import discord
import random

from discord.ext import commands
from pathlib import Path

class teczka(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teczka")
    async def teczkaCommand(self, ctx):
        dowody = [p.stem for p in Path(".").glob("./images/teczka/*")]
        choice = random.randint(0, len(dowody)-1)

        file = discord.File(f"./images/teczka/{dowody[choice]}.jpg", filename=f"{dowody[choice]}.jpg")
        embed = discord.Embed()
        embed.set_author(name=f"Akta HF - {dowody[choice]}")
        embed.set_image(url=f"attachment://{dowody[choice]}.jpg")
        await ctx.send(file=file, embed=embed)

    #TODO - Podmienic teczke jako akta60-siony - kiedy ktos wpisze "potwierdzam" to wrzucic emotke police i pingnac lolusia

def setup(bot):
    bot.add_cog(teczka(bot))