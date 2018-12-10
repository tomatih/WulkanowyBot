import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot("$")
bot.remove_command("help")

ext =["wulkanowy","utils"]

for e in ext:
    bot.load_extension(f"command.{e}")

@bot.event
async def on_ready():
    print()
    print(f"Logged as {bot.user}")
    activ = discord.Game(name="Start by typing `$help`",start=datetime.now())
    await bot.change_presence(activity=activ)

@bot.event
async def on_command_error(ctx,error):
    await ctx.send("An error occured\n{}".format(error))
    print(error)

bot.run(open("tokens.txt").read())