import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.environ['TOKEN']

desecription =\
    '''
    uobbot
    '''

bot = commands.Bot(command_prefix='$',
                   descpiprition=desecription,
                   case_insensitive=True)


@bot.event
async def on_ready():

    print('Looged in as\n')

    x = f"Name: {bot.user.name} ID:{bot.user.id}"
    print(x)

    print('-'*len(x))


@bot.command()
async def uobcontact(ctx):
    await ctx.send("For inuiries \n wa.me/+97316633366 \n studentcc@uob.edu.bh \n dsa@uob.edu.bh \n UOB Sakheer Telephone Exchange :17438888 \n UOB Isa Telephnone Exchange 17876666  ")


@bot.command()
async def uobplan(ctx):
    await ctx.send(" http://ucs.uob.edu.bh/index.php ")


@bot.command()
async def uobit(ctx):
    await ctx.send(" https://cit.uob.edu.bh/ ")


@bot.command()
async def olduob(ctx):
    await ctx.send(" http://offline.uob.edu.bh/en/")


@bot.command()
async def drop(ctx):
    await ctx.send("23 december 2021")


@bot.command()
async def uobeng(ctx):
    await ctx.send("https://engineering.uob.edu.bh/")


@bot.command()
async def Planner(ctx):
    await ctx.send("https://sis.uob.edu.bh/uob_sis_prod/UI/StudentView/planner.htm")


@bot.command()
async def Blackboard(ctx):
    await ctx.send("https://blackboard.uob.edu.bh/")


@bot.command()
async def lockdown(ctx):
    await ctx.send("https://download.respondus.com/lockdown/download.php?id=688217046")


@bot.command()
async def GPA(ctx):
    await ctx.send("https://www.uob-bh.com/forum/pages/gpa/ \n https://uobgpa.github.io/v3/")


bot.run(token)
