import discord
from discord.ext import commands
import keys
import os
import json

bot = commands.Bot(command_prefix=keys.PREFIX)


# Load in word DB
with open("cogs/wordle_DB/db.json", "r") as f:
    try:
        score_db = json.load(f)
    except Exception as e:
        print(f"Database failed to load: {e}")
        score_db = {}
    print("Database Loaded")

# Loads cogs in automatically
for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print(e)

async def add_to_db(user, day, score, message):
    user_scores = score_db.get(user, {})

    day_score = user_scores.get(day, None)
    
    if day_score:
        await message.channel.send(f"{message.author.mention} tried to cheat!")
        return False

    user_scores[day] = score
    score_db[user] = user_scores
    with open("cogs/wordle_DB/db.json", "w") as f:
        json.dump(score_db, f)
    return True

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}. All systems are operational')

@bot.event
async def on_message(message): 
    words = message.content.split()
    if words[0] == "Wordle" and message.channel.name == "wurdle":
        day = words[1]

        score = words[2].split("/")[0] if words[2].split("/")[0] != "X" else 0 # fancy

        security = await add_to_db(message.author.name + f"#{message.author.discriminator}", day, score, message)
        if security:
            await message.channel.send(f'{message.author.mention}, your score of `{score}` has been recorded. To see your overall wordle statistics, use `$wordle_stats`')
    
    
    await bot.process_commands(message)

    


bot.run(keys.DISCORD_TOKEN)