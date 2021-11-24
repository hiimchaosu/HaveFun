import discord
import logging
import datetime
from discord.ext import commands
from HaveFunToken import HFToken

# set bot's prefix to '$'
bot = commands.Bot(command_prefix='$')
#client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()

def maturka_time():  # Counting days inbetween two dates.
    current_date = datetime.date.today()
    target_date = datetime.date(2022, 5, 4)
    days_left = target_date - current_date
    return days_left.days

@bot.event # wait for bot's responsiveness
async def on_ready():
    print('{0.user} online and operating.'.format(bot))

@bot.event  # whatever is down here, its mine - KaKari
async def on_message(message):
    if message.author == bot.user:
        return;
    if "matura" in message.content:
        await message.channel.send(
            f'Matury zaczynają się 4 Maja 2022, środa o godz. 9.00. Szykuj dupe <@!697518297096257577>, bo zostało ci {maturka_time()} dni. ')
    if "@everyone" in message.content:
        await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention))
    await bot.process_commands(message)

@bot.command() # Commands for BM side of the server as for now I guess - KaKari - TODO tidy up R6 role, then change to ping the role
async def R6(channel):
    emote = "<:kitkuPaf:848926844832186388>"
    await channel.send(f"Its time for a game of R6 honey: <@!404579956874674176> {emote} <@!230697738784735232> {emote} <@!532665219927769099> {emote} <@!697518297096257577> {emote} <@!300652757000519680> {emote} <@!378627693606076444>")

# Ping user when he's typing anything - Chaosu
@bot.event
async def on_typing(channel, user, when):
    if channel.id == 912763830969454602:
        print(f"{user} is typing message in {channel} {when}")  # Additional comment for console output
        # await channel.send('Widze jak tam sobie piszesz {0}'.format(user.mention)) - TODO - ping every now and then, not fucking spam pings lmao

bot.run(HFToken())