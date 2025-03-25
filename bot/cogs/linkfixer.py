from nextcord.ext import commands

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

def setup(bot):
    bot.add_cog(twitterFixer(bot))