import discord
from discord.ext import commands
import asyncssh

import json
config_VS = json.loads(open("/app/data/config_VS.json").read())

class VSControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def run_ssh(self, command):
        try:
            async with asyncssh.connect(
                config_VS["HOST"],
                username=config_VS["USER"],
                client_keys=config_VS["KEY_PATH"],
                known_hosts=None
            ) as conn:
                result = await conn.run(command, check=False)
                if result.exit_status == 0:
                    return result.stdout.strip() or "Command executed (on output)."
                else:
                    return (
                        f"? Command failed (exit {result.exit_status})\n"
                        f"STDOUT: {result.stdout.strip()}\n"
                        f"STDERR: {result.stderr.strip()}"
                    )
        except Exception as e:
            return f"SSH connection failed: {e}."

    @commands.command(
        name="startvs",
        help="Turn on the server for VS - Dedicated server (needs role)"
    )
    @commands.has_role("HF")
    async def startvs(self, ctx):
        output = await self.run_ssh(f"{config_VS['VS_COMMAND']} start")
        await ctx.send(f"```\n{output}\n```")

    @commands.command(
        name="stopvs",
        help="Turn off the server for VS - Dedicated server (needs role)"
    )
    @commands.has_role("HF")
    async def stopvs(self, ctx):
        output = await self.run_ssh(f"{config_VS['VS_COMMAND']} stop")
        await ctx.send(f"```\n{output}\n```")

    @startvs.error
    async def startvs_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"You are missing a crucial role for it to work.")

    @stopvs.error
    async def stopvs_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"You are missing a crucial role for it to work.")

async def setup(bot):
    await bot.add_cog(VSControl(bot))