import discord
from discord.ext import commands, tasks
import asyncio
from data import functions

import json
config = json.loads(open("../data/config.json").read())

class mcserverstatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_status_message = None
        self.status_channel_id = config["mcserverchannelID"]
        self.status_loop.start()

    async def send_update_status(self, ctx):
        server_info = functions.get_mc_server_info(config["mcserverip"],config["mcserverport"])

        if server_info["online"]:
            embed = discord.Embed(
                title="🌍 Hentai Anarchy Server status",
                description="Modpack in use: **Divine Journey 2**! 🎉",
                color=discord.Color.green()
            )
            embed.add_field(name="👥 Players", value=f"{server_info['players_online']}/{server_info['max_players']}",
                            inline=True)
            embed.add_field(name="📜 MOTD", value=f"{server_info['motd']}", inline=True)
            embed.add_field(name="⚡ Latency", value=f"{server_info['latency']:.1f}ms", inline=True)
            # Show player names if players are online
            if server_info["players_online"] > 0:
                embed.add_field(name="👨‍💻 Players Online", value=", ".join(server_info["players"]), inline=False)
            embed.add_field(name="⚡ TPS", value=f"{server_info['tps']}ms", inline=True)

        else:
            embed = discord.Embed(
                title="❌ Minecraft Server Offline",
                description="The server is currently **offline**.",
                color=discord.Color.red()
            )
        if self.last_status_message:
            try:
                await self.last_status_message.edit(embed=embed)
            except discord.NotFound:
                self.last_status_message = await ctx.send(embed=embed)
        else:
            self.last_status_message = await ctx.send(embed=embed)


    @commands.command(
        name="MCStatus",
        help="Is the HENTAI ANARCHY server on?"
    )
    async def mcstatus(self, ctx):
        await self.send_update_status(ctx.channel)

    @tasks.loop(hours=1)
    async def status_loop(self):
        """Runs every hour to update the status message."""
        await self.bot.wait_until_ready()  # Ensure bot is fully ready
        channel = self.bot.get_channel(self.status_channel_id)
        if channel:
            await self.MCStatus(channel)

    @status_loop.before_loop
    async def before_status_loop(self):
        await self.bot.wait_until_ready()  # Wait until the bot is fully ready

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(mcserverstatus(bot))
    else:
        await bot.add_cog(
            mcserverstatus(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )