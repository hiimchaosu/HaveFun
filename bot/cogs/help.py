import discord
from discord.ext import commands

from bot.main import PREFIX

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="help",
        aliases=["h"],
        help="List all the commands"
    )
    async def help_command(self, ctx):
        embed = discord.Embed(
            title='📜 Command List: ',
            colour=ctx.author.colour)
        embed.set_author(name="hiimChaosu", icon_url="https://avatars.githubusercontent.com/u/25712415?v=4",
                         url="https://github.com/hiimchaosu")
        categories = {}
        for command in self.bot.commands:
            category = command.extras.get("category", "Other")  # Get category, default to 'Other'
            if category not in categories:
                categories[category] = []
            categories[category].append(f"**`{command.name}`** - {command.help or 'No description found'}")
        for category, commands_list in categories.items():
            embed.add_field(name=f"🔹 {category}\n────────────────────────────────", value="\n".join(commands_list), inline=False)
        embed.set_footer(
            text="Future changes in progress - if you have any ideas contact hiimChaosu")
        await ctx.send(embed=embed)

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(help(bot))
    else:
        await bot.add_cog(
            help(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
