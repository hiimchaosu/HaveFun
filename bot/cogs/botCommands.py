import discord
from discord.ext import commands
import datetime
import random

class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def rngLevel(self):
        RNGCreate = random.randint(0,100)
        RNGOption = [0,1,2,3,4]
        print(RNGOption[0])
        if RNGCreate <= 20:
            return RNGOption[0], RNGCreate
        elif 20 < RNGCreate < 60:
            return RNGOption[1], RNGCreate
        elif 60 <= RNGCreate <= 95:
            return RNGOption[2], RNGCreate
        elif 96 <= RNGCreate <= 99:
            return RNGOption[3], RNGCreate
        else:
            return RNGOption[4], RNGCreate

    @commands.Cog.listener()
    async def on_message(self, ctx):
        print(f"{ctx.channel}: {ctx.author}: {ctx.content}")
        if ctx.author == self.bot.user:
            return
        if ctx.channel.id == 746329009691951135 & ctx.author.id == 300652757000519680 & "jutro" in ctx.content:
            await ctx.channel.send('<:PepeClown:768892735499272222> '.format(ctx.author.mention))

    # Rewritten command without a function for matura command
    @commands.command(name="matura")
    async def matura(self, ctx):
        current_date = datetime.date.today()
        target_date = datetime.date(2022, 5, 4)
        days_left = target_date - current_date
        await ctx.message.channel.send(
            f'Matury zaczynają się 4 Maja 2022, środa o godz. 9.00. Szykuj dupe <@!697518297096257577>, bo zostało ci {days_left.days} dni.')

    @commands.command(name="essa")
    async def essa(self, ctx):
        OPTION, PERCENTAGE = self.rngLevel()
        Author = format(ctx.message.author.mention)
        ELevel = [
            f"Twój poziom essy wynosi: {PERCENTAGE}%, wariacie, słabo coś dzisiaj {Author}",
            f"Twój poziom essy wynosi: {PERCENTAGE}%, lecimy nie śpimy, {Author} :call_me:",
            f"Nooo, to jest dopiero chill, {PERCENTAGE}% {Author} tak trzymaj! :call_me:",
            f"Gibon był palony? {Author}, aż potężne {PERCENTAGE}% :call_me:",
            f"Jaki {Author} jest wychillowanyyyyy~ {PERCENTAGE}% :call_me: :call_me: :call_me:",
        ]
        await ctx.send(ELevel[OPTION])

    @commands.command(name="rasista")
    async def rasista(self, ctx):
        OPTION, PERCENTAGE = self.rngLevel()
        Author = format(ctx.message.author.mention)
        RLevel = [
            f"Racism cancelled {PERCENTAGE}% - try your luck next time {Author} <:brugSad:1012490361257599067>",
            f"Członek {Author} i jego poziom {PERCENTAGE}% wskazuje na lekki <:cmonBrug:1012489207559766146>",
            f"Piękny przykład naszego członka klubu, {Author}, {PERCENTAGE}%! <:cmonBrug:1012489207559766146>",
            f"Rasowy rasista {Author} to jest poziom! {PERCENTAGE}% <:cmonBrug:1012489207559766146>",
            f"NOWY PRZYWÓDCA -> {Author} - {PERCENTAGE}% <:brugHappy:1012490995163729930>",
        ]
        await ctx.send(RLevel[OPTION])

    @commands.command(name="tlen")
    async def tlen(self, ctx):
        OPTION, PERCENTAGE = self.rngLevel()
        Author = format(ctx.message.author.mention)
        TLevel = [
            f"ALE DUSZNO, TLEN: {PERCENTAGE}% Lepiej łap za butle {Author} <:harambe:1012493211878576259>",
            f"Nie jest źle {Author}, skromne {PERCENTAGE}%. Jest czym oddychać. <:harambe:1012493211878576259>",
            f"Weź się podziel {Author}, aż {PERCENTAGE}%! <:harambe:1012493211878576259>",
            f"Tak to można <:harambe:1012493211878576259> pooddychać. {Author} - {PERCENTAGE}% <:harambe:1012493211878576259>",
            f"Tlen nie jest dla {Author} problemem {PERCENTAGE}%! <:xdd:1012493213703082034>",
        ]
        await ctx.send(TLevel[OPTION])

    @commands.command(name="R6")
    async def R6(self, ctx):
        emote = "<:kitkuPaf:848926844832186388>"
        await ctx.send(
            f"It's time for a game of R6 honey: {emote} <@&754314805438840955> {emote}")
        message_R6 = [await ctx.send("19.30-20.00"),
                      await ctx.send("20.00-20.30"),
                      await ctx.send("20.30-21.00"),
                      await ctx.send("Pass aka <@!300652757000519680> mówiący jutro")]
        for i in message_R6:
            await i.add_reaction("<:GHOk:793607140735451156>")

    # For future bug and function testing
    @commands.command(name="check")
    async def checkCommand(self, ctx):
        pass


def setup(bot):
    bot.add_cog(botCommands(bot))
