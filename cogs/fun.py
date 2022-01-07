from discord.ext import commands
import discord

import sys
sys.dont_write_bytecode = True

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bubblewrap(self, ctx):

        msg = ''
        for _ in range(0, 5):
            for _ in range(0, 10):
                msg += '||pop!|| '
            msg += '\n'

        await ctx.send(msg)

def setup(bot):
    bot.add_cog(fun(bot))