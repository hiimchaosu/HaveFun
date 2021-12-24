import discord
from discord.ext import commands
import datetime

class botCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    # Simple help command for now TODO - REWRITE THIS SHIT XD
    @commands.command()
    async def help(self, ctx):
        await ctx.send("As for now the commands are as follows: ")
        embed = discord.Embed(title='List of commands:', color=0x00ff00)
        embed.set_author(name="hiimChaosu",icon_url="https://avatars.githubusercontent.com/u/25712415?v=4",url="https://github.com/hiimchaosu")
        embed.add_field(name="R6", value="A command made by KaKari for (insert desc here)",inline=False)
        embed.add_field(name="play [yt-url]", value="Command for simple music bot",inline=False)
        embed.add_field(name="join", value="If you are feeling lonely, I can come join you :)",inline=False)
        embed.add_field(name="disconnect", value="Well, I am currently unable to leave channel by my own, please help me if you feel like your VC is crowded",inline=False)
        embed.add_field(name="pause", value="When I am annoying you, you can pause my song or whatever I am doing on VC",inline=False)
        embed.add_field(name="resume", value="If you want me to continue, use this command",inline=False)
        embed.add_field(name="matura", value="Command to remind our friend about her matura exams :)",inline=False)
        embed.set_footer(text="Future changes in progress - if you have any ideas contact my owner hiimChaosu#1703 or Kakari#3103")
        await ctx.send(embed=embed)

    # Rewritten command without a function for matura command
    @commands.command()
    async def matura(self, ctx):
        current_date = datetime.date.today()
        target_date = datetime.date(2022, 5, 4)
        days_left = target_date - current_date
        await ctx.message.channel.send(f'Matury zaczynają się 4 Maja 2022, środa o godz. 9.00. Szykuj dupe <@!697518297096257577>, bo zostało ci {days_left.days} dni.')

    @commands.command()
    async def R6(self, channel):
        emote = "<:kitkuPaf:848926844832186388>"
        await channel.send(
            f"Its time for a game of R6 honey: <@!404579956874674176> {emote} <@!230697738784735232> {emote} <@!532665219927769099> {emote} <@!697518297096257577> {emote} <@!300652757000519680> {emote} <@!378627693606076444>")
        message_R6 = [await channel.send("17.30-18.30"),
                      await channel.send("18.30-19.30"),
                      await channel.send("19.30-20.30")]
        # embed = discord.Embed(title='Testy', color=0x00ff00) - This lil guy makes a fancy little box. Saved to play with later
        for i in message_R6:
            await i.add_reaction("<:GHOk:793607140735451156>")

def setup(client):
    client.add_cog(botCommands(client))