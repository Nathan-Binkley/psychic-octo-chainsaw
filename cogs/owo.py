from discord.ext import commands
import discord

import random
import sys
sys.dont_write_bytecode = True

class owo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.filterList = ['://','www.','.com','.net','.gov','.org','https','http', '@', '#', 'RT']
        self.customEndings = ['( ͡° ͜ʖ ͡°) ',"*nuzzles you* OwO ", "*Pounces on Daddy's lap* UwU What's this? ",  "*stares deep into your eyes* I wuv you ", "*Kisses you* ", "º꒳º ", "Pwease Daddy? I can be youw pwincess (⑅˘꒳˘) " ,"OwO *notices bulge* ", "ouo ", "rawr XD ", "owo ", "UwU ", "*Softly pets your cute head* ", "Do you need some nuzzle wuzzle?"]
        self.customBeginnings = ['Mommy ', '*Stares into your eyes and says* ', '( ͡° ͜ʖ ͡°) ', '*purrs on your lap* ', '*Jumps on Daddy\'s lap* ']

    @commands.command()
    async def owo(self, ctx, *arg):
        owod = ""
        text = ctx.message.content.split(" ", 1)[1]
        texts = text.split(" ") #Split on spaces
        for i in texts: #for each item in the split list
            i = i.rstrip()  #remove \n characters 
        
            temp = False 
            for j in self.filterList: #allows filtering based on predetermined list
                if j in i:  # if filter index in the original word
                    owod += i   #ignore it
                    temp = True
                    break
            if not temp:    # if filter index not in word
                for j in i: # go through each letter
                    if j == "l" or j == "r":    # replace
                        owod += "w"
                    elif j == "L" or j == "R": # replace
                        owod += "W"
                    else:
                        owod += j #add if no replace (not r or l)
            owod += " "

        if len(owod) < 150: # add custom beginning
            try:
                helper = random.randint(0,len(self.customBeginnings)-1)
                owod = self.customBeginnings[helper] + "\n" + owod + "\n"
            except:
                pass

        if len(owod) < 150: # add custom ending
            try:
                helper = random.randint(0,len(self.customEndings)-1)
                owod += self.customEndings[helper]
            except:
                pass

        await ctx.send(owod)
    
def setup(bot):
    bot.add_cog(owo(bot))

