# TODO - React with LIKE under tatsu lvl up message
# TODO - Comment tatsu's lvl up message: "Tatsu jak zwykle z rigczem"
# TODO - jakos to kurwa ladnie napisac

import discord
from discord.ext import commands


class tatsuReaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
    @commands.Cog.listener()  # Somehow works, tho throws a small error, to fix later.
    async def on_message(self, message):
        print(f"{message.channel}: {message.author}: {message.content}")
        if message.author == self.bot.user:
            return
        if "test" in message.content:
            print("Testujesz cos?")
        await self.bot.process_commands(message)


def setup(client):
    client.add_cog(tatsuReaction(client))