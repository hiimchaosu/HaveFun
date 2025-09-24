import discord
import random

from discord.ext import commands
from pathlib import Path

SIXTY = "potwierdzam"

class aktaHF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def manIsSixty(self, ctx):
        if SIXTY in ctx.content.lower().replace(' ', ''):
            await ctx.add_reaction("<a:POLICE:927849013628268545>")
            await ctx.channel.send("Co robisz?<:gun:668879124554579988>")

    @commands.command(
        name="teczka",
        description="Check the archives of HF"
    )
    async def teczkaCommand(self, ctx):
        try:
            dowody = [p.stem for p in Path(".").glob("app/images/teczka/*")]
            choice = random.randint(0, len(dowody)-1)

            file = discord.File(f"app/images/teczka/{dowody[choice]}.jpg", filename=f"{dowody[choice]}.jpg")
            embed = discord.Embed()
            embed.set_author(name=f"Akta HF - {dowody[choice]}")
            embed.set_image(url=f"attachment://{dowody[choice]}.jpg")
            await ctx.send(file=file, embed=embed)
        except Exception:
            embed = discord.Embed()
            embed.set_author(name=f"Akta HF - Empty")
            await ctx.send(embed=embed)

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(aktaHF(bot))
    else:
        await bot.add_cog(
            aktaHF(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
