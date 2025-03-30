import json
from pathlib import Path

import discord
from discord.ext import commands

VERSION = "0.4.2dev"
PREFIX = "*"

class HaveFun(commands.Bot):
    def __init__(self, config):
        super().__init__(
            command_prefix=self.prefix,
            case_insensitive=True,
            help_command=None,
            intents=discord.Intents.all()
        )
        self.config = config

    async def setup_hook(self):
        print("### SETTING UP COGS ###")
        for file in Path("cogs").glob("*.py"):
            cog_name = file.name.split(".")[0]
            await self.load_extension(f"cogs.{cog_name}")
            print("Loaded extension:", file.name)

        if self.config["test-server-id"] == "":
            await self.tree.sync()
        else:
            await self.tree.sync(guild=discord.Object(id=self.config["test-server-id"]))
        print("### COGS SET UP COMPLETE ###")

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or(f"{PREFIX}")(bot, msg)

    async def on_ready(self):
        self.client_id = (await self.application_info()).id
        print("Bot ready.")
        await self.change_presence(activity=discord.CustomActivity(name=f"v{VERSION} | {PREFIX}help"))

if __name__ == "__main__":
    config = json.loads(open("../data/config.json").read())
    bot = HaveFun(config)
    bot.run(config["token"])
