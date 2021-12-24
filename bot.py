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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="his incompetent coder"))

@bot.event  # whatever is down here, its mine - KaKari
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.content}")
    if message.author == bot.user:
        return
    if "@everyone" in message.content:
        await message.channel.send('<:ping:768891917848281119> {0}'.format(message.author.mention))
    await bot.process_commands(message)

#@bot.event
#async def on_raw_reaction_add(payload):
#    if payload.channel_id == 912763830969454602:
#        if payload.emoji.name == "<:GHOk:793607140735451156>":
#            channel = bot.get_channel(912763830969454602)
#            message = await channel.fetch_message(payload.message_id)
#            reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
#            if reaction and reaction.count > 1:
#                print(reaction.count)

# TODO - command to check how long has someone spent on AFK status, by checking AFK room on the server
# TODO - Ping user when he's typing anything, when I'm fucking ready for it - Chaosu
# TODO - Sort out the commands for specific actions into different files? just like music.py (work on cogs)
bot.run(HFToken())