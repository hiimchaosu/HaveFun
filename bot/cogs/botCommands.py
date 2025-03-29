import discord
from discord.ext import commands
from discord.ext.commands import Cog
from data import functions
from table2ascii import table2ascii as t2a, PresetStyle
import calendar

class botCommands(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        print(f"{ctx.channel}: {ctx.author}: {ctx.content}")
        if ctx.author == self.bot.user:
            return
        if ctx.channel.id == 746329009691951135 & ctx.author.id == 300652757000519680 & "jutro" in ctx.content:
            await ctx.channel.send('<:PepeClown:768892735499272222> '.format(ctx.author.mention))

    @commands.command(
        name="matura",
        description="Command to remind our friend about her matura exams :)"
    )
    async def matura(self, ctx):
        await ctx.message.channel.send(
            f'Matury zaczynają się 4 Maja 2022, środa o godz. 9.00. Szykuj dupe <@!697518297096257577>, bo zostało ci {functions.daysLeftToMatura()} dni.'
        )

    @commands.command(
        name="essa",
        description="How much of a chill person are You?"
    )
    async def essa(self, ctx):
        OPTION, PERCENTAGE = functions.rngLevel()
        Author = format(ctx.message.author.mention)
        ELevel = [
            f"Twój poziom essy wynosi: {PERCENTAGE}%, wariacie, słabo coś dzisiaj {Author}",
            f"Twój poziom essy wynosi: {PERCENTAGE}%, lecimy nie śpimy, {Author} :call_me:",
            f"Nooo, to jest dopiero chill, {PERCENTAGE}% {Author} tak trzymaj! :call_me:",
            f"Gibon był palony? {Author}, aż potężne {PERCENTAGE}% :call_me:",
            f"Jaki {Author} jest wychillowanyyyyy~ {PERCENTAGE}% :call_me: :call_me: :call_me:",
        ]
        await ctx.send(ELevel[OPTION])

    @commands.command(
        name="rasista",
        description="How much racism is in You?"
    )
    async def rasista(self, ctx):
        OPTION, PERCENTAGE = functions.rngLevel()
        Author = format(ctx.message.author.mention)
        RLevel = [
            f"Racism cancelled {PERCENTAGE}% - try your luck next time {Author} <:brugSad:1012490361257599067>",
            f"Członek {Author} i jego poziom {PERCENTAGE}% wskazuje na lekki <:cmonBrug:1012489207559766146>",
            f"Piękny przykład naszego członka klubu, {Author}, {PERCENTAGE}%! <:cmonBrug:1012489207559766146>",
            f"Rasowy rasista {Author} to jest poziom! {PERCENTAGE}% <:cmonBrug:1012489207559766146>",
            f"NOWY PRZYWÓDCA -> {Author} - {PERCENTAGE}% <:brugHappy:1012490995163729930>",
        ]
        await ctx.send(RLevel[OPTION])

    @commands.command(
        name="tlen",
        description="Check your oxygen reserves!"
    )
    async def tlen(self, ctx):
        OPTION, PERCENTAGE = functions.rngLevel()
        Author = format(ctx.message.author.mention)
        TLevel = [
            f"ALE DUSZNO, TLEN: {PERCENTAGE}% Lepiej łap za butle {Author} <:harambe:1012493211878576259>",
            f"Nie jest źle {Author}, skromne {PERCENTAGE}%. Jest czym oddychać. <:harambe:1012493211878576259>",
            f"Weź się podziel {Author}, aż {PERCENTAGE}%! <:harambe:1012493211878576259>",
            f"Tak to można <:harambe:1012493211878576259> pooddychać. {Author} - {PERCENTAGE}% <:harambe:1012493211878576259>",
            f"Tlen nie jest dla {Author} problemem {PERCENTAGE}%! <:xdd:1012493213703082034>",
        ]
        await ctx.send(TLevel[OPTION])

    @commands.command(
        name="R6",
        description="Want to play a game? R6 - I'll ping people with this rank and give you times!"
    )
    async def R6(self, ctx):
        emote = "<:kitkuPaf:848926844832186388>"
        await ctx.send(
            f"It's time for a game of R6 honey: {emote} <@&754314805438840955> {emote}")
        message_R6 = [
            await ctx.send("19.30-20.00"),
            await ctx.send("20.00-20.30"),
            await ctx.send("20.30-21.00"),
            await ctx.send("Pass aka <@!300652757000519680> mówiący jutro")
        ]
        for i in message_R6:
            await i.add_reaction("<:GHOk:793607140735451156>")

    @commands.command(
        name="calendar",
        description="X"
    )
    async def calendar(self, ctx):
        yy = int(functions.thisYear())
        mm = int(functions.thisMonth())
        cal = calendar.monthcalendar(yy, mm)
        days = ["Pn", "Wt", "Sr", "Czw", "Pt", "Sob", "Ndz"]
        events = functions.calendarEvents()
        for week in cal:
            for i, day in enumerate(week):
                if day in events:
                    week[i] = f"*{day}*"

        output = t2a(
            header=days,
            body=cal,
            style=PresetStyle.double_thin_box,
            first_col_heading=False
        )
        await ctx.send(f"```css\n{output}\n```")
        await ctx.send(events)

    @commands.command(
        name="eventadd",
        description="X"
    )
    async def eventadd(self, ctx, number):
        if number.isnumeric():
            functions.calendarEventsAdd(number)
            await ctx.send(f"```css\nEvent added.\n```")
        else:
            await ctx.send(f"You must type in a number.")

    # For future bug and function testing
    @commands.command(
        name="check",
        description="Mostly a command for checking stuff (WIP)"
    )
    async def checkCommand(self, ctx):
        await ctx.send("Checkmate")

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(botCommands(bot))
    else:
        await bot.add_cog(
            botCommands(bot),
            guild = discord.Object(id=bot.config["test-server-id"])
        )
