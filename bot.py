import discord
from discord.ext import commands
from HaveFunToken import HFToken
# Importing cogs for the bot
import botCommands
import music
import discordLogging
import tatsuReaction

bot = commands.Bot(command_prefix='$', intents = discord.Intents.all(), case_insensitive=True, help_command=None)

cogs = [music, discordLogging, tatsuReaction, botCommands]
for i in range(len(cogs)):
    cogs[i].setup(bot)

# wait for bot's responsiveness and set it's status
@bot.event
async def on_ready():
    print('{0.user} online and operating.'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your wishes"))

@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.content}")
    if message.author == bot.user:
        return
    if "@everyone" in message.content:
        await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention))
    await bot.process_commands(message)

# TODO - command to check how long has someone spent on AFK status, by checking AFK room on the server
# TODO - write code for reminder about whatever event ex. ($reminder 2000 today Przypomnij o filmie)
# TODO - calendar with server events
# TODO(?) - storage for some links(?) make a database for storing stuff

bot.run(HFToken())


# GIT TEST COMMIT