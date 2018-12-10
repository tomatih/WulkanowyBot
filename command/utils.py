import discord
from discord.ext import commands

class Utils():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Be nice and say hello"""
        await ctx.send("Hello {}".format(ctx.author.name))

    @commands.command()
    async def help(self, ctx):
        """Lists all avaible commands"""
        em = discord.Embed()
        em.title = "Help"
        em.description="A list of all commands"
        em.colour=discord.Color.from_rgb(0,255,0)
        a={"name":"t1","value":'s',"inline":False}
        for c in self.bot.commands:
            a['name'] = c.name
            a['value'] = c.help
            em.add_field(**a)
        await ctx.send(embed=em)

    @commands.command()
    async def ping(self,ctx):
        """Shows a ping message"""
        l=self.bot.latency
        print(l)
        await ctx.send("Pong `{0:.0f}s {1:.2f}ms`".format(l//10, l*1000-l//10))

def setup(bot):
    bot.add_cog(Utils(bot))