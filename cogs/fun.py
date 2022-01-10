from discord.ext import commands
import discord
import random

import sys
sys.dont_write_bytecode = True

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.insults = self.load_insults()

    @commands.command()
    async def bubblewrap(self, ctx):

        msg = ''
        for _ in range(0, 5):
            for _ in range(0, 10):
                msg += '||pop!|| '
            msg += '\n'

        await ctx.send(msg)

    def load_insults(self):
        with open("cogs/data/insults.txt", "r") as f:
            return f.read().splitlines() #I don't know if this will work lmao

    @commands.command()
    async def insult(self, ctx, user = None):
        if not user:
            msg = self.insults[random.randInt(len(self.insults))]
        else:
            msg = f"Hey {user}! {self.insults[random.randInt(len(self.insults))]}" #I don't know how well this will work either lol
        await ctx.send(msg)

    

def setup(bot):
    bot.add_cog(fun(bot))