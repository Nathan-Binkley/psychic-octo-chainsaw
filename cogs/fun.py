from typing import List
from discord.ext import commands
import discord
import random
import keys
import requests
import json

import sys
sys.dont_write_bytecode = True

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.insults = self.load_insults()
        self.giphy_key = keys.GIPHY_API

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
    async def insult(self, ctx, *target):
        target = list(target)    
        target = " ".join(target)

        if not target:
            msg = self.insults[random.randint(0,len(self.insults))]
        else:
            msg = f"Hey {target}! {self.insults[random.randint(0, len(self.insults))]}" #I don't know how well this will work either lol
        await ctx.send(msg)

    @commands.command()
    async def gif(self, ctx):
        # Load a json object from the string returned by the URL.
        req = json.loads(requests.get("http://api.giphy.com/v1/gifs/random", params = { "api_key": self.giphy_key } ).text)
        gif = req["data"]["embed_url"]
        msg = f"{gif}"
        await ctx.send(msg)

    

def setup(bot):
    bot.add_cog(fun(bot))