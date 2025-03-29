import discord
from discord.ext import commands

#TODO - make it a little bit less hardcoded, ok?

TWITTER = "https://twitter.com"

class twitterFixer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, ctx):
        if TWITTER in ctx.content and ctx.author != self.bot.user:
            await ctx.channel.send(ctx.content[:8] + "fx" + ctx.content[8:])
            await ctx.delete()

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(twitterFixer(bot))
    else:
        await bot.add_cog(
            twitterFixer(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
