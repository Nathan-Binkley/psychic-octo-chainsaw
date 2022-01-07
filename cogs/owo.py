from discord.ext import commands
import discord

import sys
sys.dont_write_bytecode = True

class owo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def owo(self, ctx, *arg):
        """OwOs word"""
        arg = " ".join(arg)
        print(f"owo function called on: {arg} ")
        print(f"Before: {arg}")
        arg = arg.replace("l","w")
        arg = arg.replace("r","w")
        print(f"After: {arg}")
        await ctx.send(arg)
    
def setup(bot):
    bot.add_cog(owo(bot))

