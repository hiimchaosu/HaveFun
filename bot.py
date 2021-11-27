import discord
import logging
import datetime
from discord.ext import commands
from HaveFunToken import HFToken

# set bot's prefix to '$'
bot = commands.Bot(command_prefix='$')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()
intents.members = True

def maturka_time():  # Counting days inbetween two dates.
    current_date = datetime.date.today()
    target_date = datetime.date(2022, 5, 4)
    days_left = target_date - current_date
    return days_left.days

@bot.event # wait for bot's responsiveness and set it's status
async def on_ready():
    print('{0.user} online and operating.'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="his incompetent coder"))

@bot.event  # whatever is down here, its mine - KaKari
async def on_message(message):
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
    await channel.send(f"It's time for a game of R6 honey: <@!404579956874674176> {emote} <@!230697738784735232> {emote} <@!532665219927769099> {emote} <@!697518297096257577> {emote} <@!300652757000519680> {emote} <@!378627693606076444>")

# For now it stays as a command to test it's functionality - TODO a command to check how long has someone spent on AFK status, by checking AFK room on the server

@bot.command()
async def AFK():
    channelAFK = bot.get_channel(746348405906735174)  # Gets the channel test, 339789195767709697 - for test
    AFKmembers = channelAFK.members  # Finds members connected to the channel
    AFKmemids = []
    for AFKmember in AFKmembers:
        AFKmemids.append(AFKmember.id)
    print(AFKmemids)

# TODO - Ping user when he's typing anything, when I'm fucking ready for it - Chaosu
@bot.event
async def on_typing(channel, user, when):
    pass
    #print(when.second - 60)
    #if channel.id == 912763830969454602:
    #    print(f"{user} is typing message in {channel} {when}")  # Additional comment for console output
    #    await channel.send('Widze jak tam sobie piszesz {0}'.format(user.mention))

bot.run(HFToken())