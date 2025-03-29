import discord
from discord.ext import commands

from bot.main import PREFIX

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="help",
        aliases=["h"],
        description="Show all the commands"
    )
    async def help_command(self, ctx):
        embed = discord.Embed(
            title='Commands available: ',
            colour=ctx.author.colour)
        embed.set_author(name="hiimChaosu", icon_url="https://avatars.githubusercontent.com/u/25712415?v=4",
                         url="https://github.com/hiimchaosu")
        for command in self.bot.walk_commands():
            embed.add_field(name=f"{PREFIX}{command}", value=f"", inline=False)
        embed.set_footer(
            text="Future changes in progress - if you have any ideas contact hiimChaosu#1703")
        await ctx.send(embed=embed)

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(help(bot))
    else:
        await bot.add_cog(
            help(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
