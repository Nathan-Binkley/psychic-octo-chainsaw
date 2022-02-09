import discord
from discord.ext import commands
import keys
import os
import json

# On load, load in prefixes of all servers
with open("settings.json", "r") as f:
        settings = json.load(f)

        
def prefix_getter(bot, message):
    with open("settings.json", "r") as f:
        settings = json.load(f)

    id = message.guild.id

    return settings[str(id)]["prefix"]


bot = commands.Bot(command_prefix=prefix_getter)

# --------------------------------

# Load in word DB
with open("cogs/wordle_DB/db.json", "r") as f:
    try:
        score_db = json.load(f)
    except Exception as e:
        print(f"Wordle Database failed to load: {e}")
        score_db = {}
    print("Database Loaded")

#---------------------------------

# Loads cogs in automatically
for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print(e)

# Wordle DB stuff -- Need to find a way to move this over to the wordle cog, but I can't think of way without imports but that's not how it should work, right?
async def add_to_db(user, day, score, message):
    user_scores = score_db.get(user, {})

    day_score = user_scores.get(day, None)

    if day_score:
        await message.channel.send(f"{message.author.mention} tried to cheat!")
        return False

    user_scores[day] = score
    score_db[user] = user_scores
    with open("cogs/wordle_DB/db.json", "w") as f:
        json.dump(score_db, f, indent = 4)
    return True

# ------

# Display status message, confirming it is active
@bot.event
async def on_ready():
    for server in bot.guilds:
        if str(server.id) not in settings:
                settings[server.id] = {}
                settings[server.id]["prefix"] = keys.DEFAULT_PREFIX # SET DEFAULT PREFIX IF NOT IN DB
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    for server in bot.guilds:
        print(f"Currently connected to: {server.id} | {server.name} | Prefix: {settings[str(server.id)]['prefix']}")
        
    print(f'We have logged in as {bot.user}. All systems are operational')
    
#------------------

# Handle joining a server, set default prefix
@bot.event
async def on_guild_join(self, guild):
    with open("settings.json", "r") as f:
        settings = json.load(f)
    settings[guild.id] = {}
    settings[guild.id]["prefix"] = keys.DEFAULT_PREFIX
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)

#Handle specific non-command messages
@bot.event
async def on_message(message): 
    words = message.content.split()
    if len(words) >= 3:
        try:
            if words[0] == "Wordle" and message.channel.name == "wurdle" and int(words[1]):
                day = words[1]

                score = words[2].split("/")[0] if words[2].split("/")[0] != "X" else "7" # fancy

                security = await add_to_db(message.author.name + f"#{message.author.discriminator}", day, score, message)
                if security:
                    await message.channel.send(f'{message.author.mention}, your score of `{score}` has been recorded. To see your overall wordle statistics, use `$wordle_stats`')
        except Exception as e:
            print("Wordle processing error",e)
    # on_message actually overwrites the sending of the message to the command processor. 
    # So this line is necessary
    await bot.process_commands(message)

    


bot.run(keys.DISCORD_TOKEN)