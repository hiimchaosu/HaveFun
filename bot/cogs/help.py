import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["h"])
    async def help_command(self, ctx):
        # First embed for 'music commands'
        embed = discord.Embed(
            title='List of music commands:',
            colour=ctx.author.colour)
        embed.set_author(name="hiimChaosu", icon_url="https://avatars.githubusercontent.com/u/25712415?v=4",
                         url="https://github.com/hiimchaosu")
        embed.add_field(name="connect", value="[$connect (channel_name)] - connect to a channel", inline=False)
        embed.add_field(name="play/p",
                        value="[$play/$p (SONG_URL / SONG_NAME)] - play a song of your choice, or use to resume playback",
                        inline=False)
        embed.add_field(name="disconnect", value="[$disconnect] - disconnect from a channel", inline=False)
        embed.add_field(name="queue/q", value="[$queue/$q] - shows the queue for the next tracks if present",
                        inline=False)
        embed.add_field(name="pause", value="[$pause] - pauses the playback - to resume use $play", inline=False)
        embed.add_field(name="stop", value="[$stop] - stops the playback", inline=False)
        embed.add_field(name="next/skip", value="[$next/$skip] - goes to the next song", inline=False)
        embed.add_field(name="previous", value="[$previous] - goes back to the previously played song", inline=False)
        embed.set_footer(
            text="Future changes in progress - if you have any ideas contact hiimChaosu#1703 or Kakari#3103")
        await ctx.send(embed=embed)

        # Second Embed for 'other commands'
        embed = discord.Embed(
            title='List of other commands:',
            colour=ctx.author.colour)
        embed.add_field(name="R6",
                        value="Want to play a game? R6 - I'll ping people with this rank and give you times!",
                        inline=False)
        embed.add_field(name="matura", value="Command to remind our friend about her matura exams :)", inline=False)
        embed.add_field(name="essa", value="How much of a chill person are You?", inline=False)
        embed.add_field(name="rasista", value="How much racism is in You? Check it with this command!", inline=False)
        embed.add_field(name="tlen", value="Check your oxygen reserves", inline=False)
        embed.set_footer(
            text="Future changes in progress - if you have any ideas contact hiimChaosu#1703 or Kakari#3103")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
