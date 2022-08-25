import discord
#from discord import app_commands
from discord.ext import commands
import datetime
import random


class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot ready.')
        print('Cog: Commands loaded.')
    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"{message.channel}: {message.author}: {message.content}")
        if message.author == self.bot.user:
            return
        if "@everyone" in message.content:
            await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention))
        if message.channel.id == 746329009691951135 & message.author.id == 300652757000519680 & "jutro" in message.content:
            await message.channel.send('<:PepeClown:768892735499272222> '.format(message.author.mention))

    #@app_commands.command(
    #    name = "help",
    #    description="Basic help function.")

    # Simple help command for now TODO - Maybe make it more... nice looking?
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
    async def essa(self, ctx):
        poziomEssy = random.ranint(0,100)
        await ctx.message.channel.send(f'Poziom essy: {poziomEssy}')

    @commands.command()
    async def R6(self, channel):
        emote = "<:kitkuPaf:848926844832186388>"
        await channel.send(
            f"Its time for a game of R6 honey: {emote} <@&754314805438840955> {emote}")
        message_R6 = [await channel.send("19.30-20.00"),
                      await channel.send("20.00-20.30"),
                      await channel.send("20.30-21.00"),
                      await channel.send("Pass aka <!@300652757000519680 mówiący jutro")]
        for i in message_R6:
            await i.add_reaction("<:GHOk:793607140735451156>")

async def setup(bot):
    await bot.add_cog(botCommands(bot))