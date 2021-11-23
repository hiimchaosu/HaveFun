import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} online.'.format(client));

@client.event
async def on_message(message):
    if message.author == client.user:
        return;
    if "@everyone" in message.content:
        await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention));

client.run('OTEyNjQ1MTQxMjU5NTEzODc2.YZy9BQ.DbSPxgYxI_2MbPs2OjLE6rSLCxM');