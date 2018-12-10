import discord
from discord.ext import commands
import typing

class wulkanowycog():
    def __init__(self, bot):
        self.bot = bot
        self.role_types = [
            "eszkola.opolskie.pl",
            "vulcan.net.pl",
            "edu.gdansk.pl",
            "umt.tarnow.pl",
            "resman.pl",
            "fakelog.cf"
        ]
    
    @commands.command()
    async def download(self,ctx):
        """Returns the download links"""
        e = discord.Embed()
        e.title = 'Get the app'
        e.colour = discord.Color.from_rgb(255,0,0)
        e.add_field(
            name="Sklep Play",
            value="https://play.google.com/store/apps/details?id=io.github.wulkanowy",
            inline=False
        )
        e.add_field(
            name="APks",
            value="https://wulkanowy.github.io/",
            inline=False
        )
        await ctx.send(embed=e)
    
    @commands.command()
    async def switch_register(self,ctx, role: discord.Role = None):
        """Swithes user register role to the desired one"""
        if not role:
            await ctx.send("Please specify the role that you want")
            return
        if not role.name in self.role_types:
            await ctx.send("This role is invalid")
            return
        usr = ctx.author
        l= []
        for a in usr.roles:
            if not a.name in self.role_types:
                l.append(a)
        l.append(role)
        try:
            await usr.edit(roles=l)
            await ctx.send("Changed role of {} to {}".format(usr,role))
        except discord.errors.Forbidden:
            await ctx.send("Failed to set the role. Missing Permissions")

    

def setup(bot):
    bot.add_cog(wulkanowycog(bot))