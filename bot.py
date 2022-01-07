import discord
from discord.ext import commands
import keys
import os

bot = commands.Bot(command_prefix=keys.PREFIX)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print(e)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}. All systems are operational')

bot.run(keys.DISCORD_TOKEN)