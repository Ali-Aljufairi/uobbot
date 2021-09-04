import os
from discord import client
import discord
from discord import embeds
from discord.colour import Colour
from discord.embeds import Embed
from discord.ext import commands



token = os.environ['TOKEN']

desecription =\
    '''
    Uobbot
    '''

bot = commands.Bot(command_prefix='$',
                   descpiprition=desecription,
                   case_insensitive=True)

bot.remove_command('help')


@bot.event
async def on_ready():

    print('Looged in as\n')

    print(x := f"Name: {bot.user.name} ID:{bot.user.id}")

    print('-'*len(x))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="HELP", description="All the commands available ",color=0x3AA35C) #,color=Hex code
    embed.add_field(name="$uobcontact", value="Will show all the ways to conatact uob \n",inline=False)
    embed.add_field(name="$uobplan", value="UCS\n",inline=False)
    embed.add_field(name="$drop",  value="Drop date\n",inline=False)
    embed.add_field(name="$uobeng",value="UOB ENG Website\n",inline=False)
    embed.add_field(name="$Planner", value="Website Planner\n",inline=False)
    embed.add_field(name="$blackboard", value="Blackboard\n",inline=False)
    embed.add_field(name="$lockdown", value="Lockdown\n",inline=False)
    embed.add_field(name="$GPA", value="Websites to calulateGPA\n",inline=False)
    embed.add_field(name="$uoblaw", value="UOB LAW Website\n",inline=False)
    embed.add_field(name="$uobsci", value="UOB SCI Website\n",inline=False)
    embed.add_field(name="$uobcob", value="UOB COB website\n",inline=False)
    embed.add_field(name="$uobit", value="UOB IT website\n",inline=False)
    embed.add_field(name="$olduob",value="Old UOB Website \n",inline=False)
    embed.add_field(name="$uob",value="UOB Main\n",inline=False) 
    embed.add_field(name="$sis",value="SiS\n",inline=False)     
    await ctx.send(embed=embed)






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
    await ctx.send("https://sis.uob.edu.bh/uob_sis_prod/UI/StudentView/planner.html")


@bot.command()
async def Blackboard(ctx):
    await ctx.send("https://blackboard.uob.edu.bh/")


@bot.command()
async def lockdown(ctx):
    await ctx.send("https://download.respondus.com/lockdown/download.php?id=688217046")


@bot.command()
async def GPA(ctx):
    await ctx.send("https://www.uob-bh.com/forum/pages/gpa/ \n https://uobgpa.github.io/v3/")


@bot.command()
async def uoblaw(ctx):
    await ctx.send("https://law.uob.edu.bh/")


    
@bot.command()
async def uobsci(ctx):
    await ctx.send("https://science.uob.edu.bh/")


    
@bot.command()
async def uobcit(ctx):
    await ctx.send("https://teachers.uob.edu.bh/")


        
@bot.command()
async def uobcob(ctx):
    await ctx.send("https://cob.uob.edu.bh/")


@bot.command()
async def uob(ctx):
    await ctx.send("https://uob.edu.bh/")

@bot.command()
async def sis(ctx):
    await ctx.send("https://sis.uob.edu.bh/UOB_SIS_PROD/Default.aspx")



@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')



bot.run(token)
