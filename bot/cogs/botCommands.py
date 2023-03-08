import discord
from discord.ext import commands
import datetime
import random


class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"{message.channel}: {message.author}: {message.content}")
        if message.author == self.bot.user:
            return
        if message.channel.id == 746329009691951135 & message.author.id == 300652757000519680 & "jutro" in message.content:
            await message.channel.send('<:PepeClown:768892735499272222> '.format(message.author.mention))

    # @app_commands.command(
    #    name = "help",
    #    description="Basic help function.")

    # Simple help command for now TODO - Maybe make it more... nice looking?

    @commands.command(name="help", aliases=["h"])
    async def help(self, ctx):
        embed = discord.Embed(
            title='List of music commands:',
            colour=ctx.author.colour)
        embed.set_author(name="hiimChaosu", icon_url="https://avatars.githubusercontent.com/u/25712415?v=4",
                         url="https://github.com/hiimchaosu")
        # embed.add_field(name="", value="", inline=False)
        embed.add_field(name="connect", value="[$connect (channel_name)] - connect to a channel", inline=False)
        embed.add_field(name="play/p",
                        value="[$play/$p (SONG_URL / SONG_NAME)] - play a song of your choice, or use to resume playback",
                        inline=False)
        embed.add_field(name="disconnect", value="[$disconnect] - disconnect from a channel", inline=False)
        # embed.add_field(name="", value="", inline=False)
        embed.add_field(name="queue/q", value="[$queue/$q] - shows the queue for the next tracks if present",
                        inline=False)
        embed.add_field(name="pause", value="[$pause] - pauses the playback - to resume use $play", inline=False)
        embed.add_field(name="stop", value="[$stop] - stops the playback", inline=False)
        # embed.add_field(name="", value="", inline=False)
        embed.add_field(name="next/skip", value="[$next/$skip] - goes to the next song", inline=False)
        embed.add_field(name="previous", value="[$previous] - goes back to the previously played song", inline=False)
        # embed.add_field(name="", value="", inline=False)
        embed.set_footer(
            text="Future changes in progress - if you have any ideas contact hiimChaosu#1703 or Kakari#3103")
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title='List of other commands:',
            colour=ctx.author.colour)
        # embed.add_field(name="", value="", inline=False)
        embed.add_field(name="R6",
                        value="Want to play a game? R6 - I'll ping people with this rank and give you times!",
                        inline=False)
        embed.add_field(name="matura", value="Command to remind our friend about her matura exams :)", inline=False)
        # embed.add_field(name="", value="", inline=False)
        embed.add_field(name="essa", value="How much of a chill person are You?", inline=False)
        embed.add_field(name="rasista", value="How much racism is in You? Check it with this command!", inline=False)
        embed.add_field(name="tlen", value="Check your oxygen reserves", inline=False)
        embed.set_footer(
            text="Future changes in progress - if you have any ideas contact hiimChaosu#1703 or Kakari#3103")
        await ctx.send(embed=embed)

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
        poziom_essy = random.randint(0, 100)
        wariat = format(ctx.message.author.mention)
        if poziom_essy <= 20:
            await ctx.message.channel.send(
                f'Twój poziom essy wynosi: {poziom_essy}%, wariacie, słabo coś dzisiaj {wariat}')
        elif poziom_essy > 20 and poziom_essy < 60:
            await ctx.message.channel.send(
                f'Twój poziom essy wynosi: {poziom_essy}%, lecimy nie śpimy, {wariat} :call_me:')
        elif poziom_essy >= 60 and poziom_essy <= 95:
            await ctx.message.channel.send(
                f'Nooo, to jest dopiero chill, {poziom_essy}% {wariat} tak trzymaj! :call_me:')
        elif poziom_essy >= 96 and poziom_essy <= 99:
            await ctx.message.channel.send(
                f'Gibon był palony? {wariat}, aż potężne {poziom_essy}% :call_me:')
        elif poziom_essy == 100:
            await ctx.message.channel.send(
                f'Jaki {wariat} jest wychillowanyyyyy~ {poziom_essy}% :call_me: :call_me: :call_me:')

    @commands.command(name="rasista")
    async def rasista(self, ctx):
        poziom_rasisty = random.randint(0, 100)
        rasista = format(ctx.message.author.mention)
        if poziom_rasisty <= 20:
            await ctx.message.channel.send(
                f'Racism cancelled {poziom_rasisty}% - try your luck next time {rasista} <:brugSad:1012490361257599067>')
        elif poziom_rasisty > 20 and poziom_rasisty < 60:
            await ctx.message.channel.send(
                f'Członek {rasista} i jego poziom {poziom_rasisty}% wskazuje na lekki <:cmonBrug:1012489207559766146>')
        elif poziom_rasisty >= 60 and poziom_rasisty <= 95:
            await ctx.message.channel.send(
                f'Piękny przykład naszego członka klubu, {rasista}, {poziom_rasisty}%! <:cmonBrug:1012489207559766146>')
        elif poziom_rasisty >= 96 and poziom_rasisty <= 99:
            await ctx.message.channel.send(
                f'Rasowy rasista {rasista} to jest poziom! {poziom_rasisty}% <:cmonBrug:1012489207559766146>')
        elif poziom_rasisty == 100:
            await ctx.message.channel.send(
                f'NOWY PRZYWÓDCA, NASZ {rasista} - {poziom_rasisty}% <:brugHappy:1012490995163729930>')

    @commands.command(name="tlen")
    async def tlen(self, ctx):
        poziom_tlenu = random.randint(0, 100)
        oddychacz = format(ctx.message.author.mention)
        if poziom_tlenu <= 30:
            await ctx.message.channel.send(
                f'ALE DUSZNO, TLEN: {poziom_tlenu}% Lepiej łap za butle {oddychacz} <:harambe:1012493211878576259>')
        elif poziom_tlenu > 30 and poziom_tlenu < 60:
            await ctx.message.channel.send(
                f'Nie jest źle {oddychacz}, skromne {poziom_tlenu}%. Jest czym oddychać. <:harambe:1012493211878576259>')
        elif poziom_tlenu >= 60 and poziom_tlenu <= 95:
            await ctx.message.channel.send(
                f'Weź się podziel {oddychacz}, aż {poziom_tlenu}%! <:harambe:1012493211878576259>')
        elif poziom_tlenu >= 96 and poziom_tlenu <= 99:
            await ctx.message.channel.send(
                f'Tak to można <:harambe:1012493211878576259> pooddychać. {oddychacz} - {poziom_tlenu}% <:harambe:1012493211878576259>')
        elif poziom_tlenu == 100:
            await ctx.message.channel.send(
                f'Tlen nie jest dla {oddychacz} problemem {poziom_tlenu}%! <:xdd:1012493213703082034>')

    @commands.command(name="R6")
    async def R6(self, channel):
        emote = "<:kitkuPaf:848926844832186388>"
        await channel.send(
            f"It's time for a game of R6 honey: {emote} <@&754314805438840955> {emote}")
        message_R6 = [await channel.send("19.30-20.00"),
                      await channel.send("20.00-20.30"),
                      await channel.send("20.30-21.00"),
                      await channel.send("Pass aka <@!300652757000519680> mówiący jutro")]
        for i in message_R6:
            await i.add_reaction("<:GHOk:793607140735451156>")


def setup(bot):
    bot.add_cog(botCommands(bot))
