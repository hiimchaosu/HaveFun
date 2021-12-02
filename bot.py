import discord
import datetime
from discord.ext import commands
from HaveFunToken import HFToken
import music
import discordLogging
import tatsuReaction

bot = commands.Bot(command_prefix='$', intents = discord.Intents.all())

cogs = [music, discordLogging, tatsuReaction]
for i in range(len(cogs)):
    cogs[i].setup(bot)


def maturka_time():  # Counting days inbetween two dates.
    current_date = datetime.date.today()
    target_date = datetime.date(2022, 5, 4)
    days_left = target_date - current_date
    return days_left.days


@bot.event  # wait for bot's responsiveness and set it's status
async def on_ready():
    print('{0.user} online and operating.'.format(bot))
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="his incompetent coder"))


@bot.event  # whatever is down here, its mine - KaKari
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.content}")
    if message.author == bot.user:
        return
    if "matura" in message.content:
        await message.channel.send(
            f'Matury zaczynają się 4 Maja 2022, środa o godz. 9.00. Szykuj dupe <@!697518297096257577>, bo zostało ci {maturka_time()} dni. ')
    if "@everyone" in message.content:
        await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention))
    await bot.process_commands(message)


# Commands for BM side of the server as for now I guess - KaKari - TODO tidy up R6 role, then change to ping the role

@bot.command()
async def R6(channel):
    emote = "<:kitkuPaf:848926844832186388>"
    await channel.send(f"Its time for a game of R6 honey: <@!404579956874674176> {emote} <@!230697738784735232> {emote} <@!532665219927769099> {emote} <@!697518297096257577> {emote} <@!300652757000519680> {emote} <@!378627693606076444>")
    message_R6 = [await channel.send("17.30-18.30"),
                await channel.send("18.30-19.30"),
                await channel.send("19.30-20.30")]
    #embed = discord.Embed(title='Testy', color=0x00ff00) - This lil guy makes a fancy little box. Saved to play with later
    for i in message_R6:
        await i.add_reaction("<:GHOk:793607140735451156>")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 912763830969454602:
        if payload.emoji.name == "<:GHOk:793607140735451156>":
            channel = bot.get_channel(912763830969454602)
            message = await channel.fetch_message(payload.message_id)
            reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count > 1:
                await print(reaction.count)

# TODO - command to check how long has someone spent on AFK status, by checking AFK room on the server
# TODO - Ping user when he's typing anything, when I'm fucking ready for it - Chaosu
# TODO - Sort out the commands for specific actions into different files? just like music.py (work on cogs)
bot.run(HFToken())