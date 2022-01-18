from discord.ext import commands
import discord
import json


import sys
sys.dont_write_bytecode = True

class options(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.valid_prefixes = ",.<>?;:'\"[{]}-_=+()!~*@$%^&"

    async def is_valid_prefix(self, char):
        if char in [i for i in self.valid_prefixes]:
            return True
        return False

    @commands.command()
    async def set_prefix(self, ctx, character):
        # Length check
        if len(character) != 1:
            msg = f"Your prefix is too long. It needs to be one character and in the following list: {self.valid_prefixes}"
            await ctx.send(msg)
            return

        #Validity check
        if not await self.is_valid_prefix(character):
            msg = f"{character} is not a valid prefix. It needs to be in the following list: {self.valid_prefixes}"
            await ctx.send(msg)
            return

        with open("settings.json", "r") as f:
            settings = json.load(f)

        settings[str(ctx.guild.id)]["prefix"] = character
        
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)

        msg = f"Prefix has been set to `{character}` for this server"   
        await ctx.send(msg)


    @commands.command()
    async def get_prefix(self, ctx):
        with open("settings.json", "r") as f:
            settings = json.load(f)

        character = settings[str(ctx.guild.id)]["prefix"] 
        msg = f"Prefix has been set to `{character}` for this server"
        await ctx.send(msg)
                

def setup(bot):
    bot.add_cog(options(bot))