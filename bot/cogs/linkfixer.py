import discord
import json
import re
from discord.ext import commands

config = json.loads(open("/app/data/config.json").read())
class twitterFixer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        replacements = {
            config["instagram_link"]: config["instagram_link_fixed"],
            config["twitter_link"]: config["twitter_link_fixed"],
            config["x_link"]: config["x_link_fixed"]
        }
        new_content = message.content
        replaced = False

        for old, new in replacements.items():
            if old in new_content:
                new_content = new_content.replace(old, new)
                replaced = True

        # remove junk before question mark
        new_content = re.sub(r"(https?://www\.kkinstagram\.com/\S+?)\?.*", r"\1", new_content)

        if replaced or new_content != message.content:
            await message.delete()
            await message.channel.send(f"{new_content} (by {message.author})")

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(twitterFixer(bot))
    else:
        await bot.add_cog(
            twitterFixer(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
