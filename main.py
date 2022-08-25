import discord
import asyncio
import os
import json
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents, help_command=None)

with open("HaveFunToken.json") as f:
    data = json.load(f)
HFToken = data["TOKEN"]


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load()
    async with bot:
        await bot.start(HFToken)

    # TODO - write code for reminder about whatever event ex. ($reminder 2000 today Przypomnij o filmie)
    # TODO - calendar with server events
    # TODO(?) - storage for some links(?) make a database for storing stuff


asyncio.run(main())
