import discord
import json
from discord.ext import commands

#TODO - make it a little bit less hardcoded, ok?
config = json.loads(open("../data/config.json").read())
class twitterFixer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, ctx):
        if config["twitter_link"] in ctx.content and ctx.author != self.bot.user:
            await ctx.channel.send(config["twitter_link_fixed"] + ctx.content[13:] + " by " + str(ctx.author))
            await ctx.delete()

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(twitterFixer(bot))
    else:
        await bot.add_cog(
            twitterFixer(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
