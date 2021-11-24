import discord
import logging
import datetime
from HaveFunToken import HFToken

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

def maturka_time(): #Counting days inbetwen two dates.
    current_date = datetime.date.today()
    target_date = datetime.date(2022, 5, 4)
    days_diff = target_date - current_date
    return days_diff.days

@client.event
async def on_ready():
    print('{0.user} online and operating.'.format(client));

@client.event
async def on_message(message):
    if message.author == client.user:
        return;
    if "@everyone" in message.content:
        await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention));
    if "matura" in message.content:
        await message.channel.send(
            'Matury zaczynają się 4 Maja 2022, środa o godz. 9.00. Szykuj dupe <@!697518297096257577>, bo zostało ci ', maturka_time())
client.run(HFToken());