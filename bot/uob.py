import os
import discord
from discord import client
from discord.ext import commands


token = os.environ['TOKEN']

description = '''Uobbot'''

bot = commands.Bot(command_prefix='$',
                   descpiprition=description,
                   case_insensitive=True)

bot.remove_command('help')


@bot.event
async def on_ready():

    print('Looged in as\n')

    print(x := f"Name: {bot.user.name} ID:{bot.user.id}")

    print('-'*len(x))


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="HELP", description="All the commands available ", color=0x3AA35C)  # ,color=Hex code
    embed.add_field(name="$uobcontact",
                    value="Will show all the ways to conatact uob \n", inline=False)
    embed.add_field(name="$uobplan", value="UCS\n", inline=False)
    embed.add_field(name="$drop",  value="Drop date\n", inline=False)
    embed.add_field(name="$uobeng", value="UOB ENG Website\n", inline=False)
    embed.add_field(name="$Planner", value="Website Planner\n", inline=False)
    embed.add_field(name="$blackboard", value="Blackboard\n", inline=False)
    embed.add_field(name="$lockdown", value="Lockdown\n", inline=False)
    embed.add_field(
        name="$GPA", value="Websites to calculateGPA\n", inline=False)
    embed.add_field(name="$uoblaw", value="UOB LAW Website\n", inline=False)
    embed.add_field(name="$uobsci", value="UOB SCI Website\n", inline=False)
    embed.add_field(name="$uobcob", value="UOB COB website\n", inline=False)
    embed.add_field(name="$uobit", value="UOB IT website\n", inline=False)
    embed.add_field(name="$olduob", value="Old UOB Website \n", inline=False)
    embed.add_field(name="$uob", value="UOB Main\n", inline=False)
    embed.add_field(name="$sis", value="SiS\n", inline=False)
    embed.add_field(name="$group", value="group\n", inline=False)
    embed.add_field(
        name="$uobpass", value="website to change your password\n", inline=False)

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def sciroles(ctx):
    embed = discord.Embed(

        title="Science College", description="", color=0x7FD24)  # ,color=Hex code
    embed.add_field(name=":one: : 𝐁𝐈𝐎𝐋𝐒𝟏𝟎𝟐", value='\u200b', inline=False)
    embed.add_field(name=":two: : 𝐂𝐇𝐄𝐌𝐘𝟏𝟎𝟏", value='\u200b', inline=False)
    embed.add_field(name=":three: : 𝐂𝐇𝐄𝐌𝐘𝟏𝟎𝟐", value='\u200b', inline=False)
    embed.add_field(name=":four: : 𝐂𝐇𝐄𝐌𝐘𝟏𝟎𝟑", value='\u200b', inline=False)
    embed.add_field(name=":five: : 𝐂𝐇𝐄𝐌𝐘𝟐𝟏𝟏", value='\u200b', inline=False)
    embed.add_field(name=":six: : 𝐂𝐇𝐄𝐌𝐘𝟐𝟐𝟎", value='\u200b', inline=False)
    embed.add_field(name=":seven: : 𝐂𝐇𝐄𝐌𝐘𝟐𝟐𝟏", value='\u200b', inline=False)
    embed.add_field(name=":eight: : 𝐂𝐇𝐄𝐌𝐘𝟐𝟑𝟏", value='\u200b', inline=False)
    embed.add_field(name=":nine: : 𝐂𝐇𝐄𝐌𝐘𝟐𝟒𝟏", value='\u200b', inline=False)
    embed.add_field(name=":a: : 𝐂𝐇𝐄𝐌𝐘𝟯𝟭𝟎", value='\u200b', inline=False)
    embed.add_field(name=":b: : 𝗠𝗔𝗧𝗛𝗦𝟏𝟎𝟏", value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_c: : 𝗠𝗔𝗧𝗛𝗦𝟏𝟎𝟐",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_d: : 𝐌𝐀𝐓𝐇𝐒𝟐𝟎𝟓",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_e: : 𝐌𝐀𝐓𝐇𝐒𝟐𝟏𝟏 ",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_f: : 𝐌𝐀𝐓𝐇𝐒𝟯𝟰𝟮 ",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_g: : 𝐏𝐇𝐘𝐂𝐒𝟏𝟎𝟏",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_h: : 𝐏𝐇𝐘𝐂𝐒𝟏𝟎𝟐",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_i: :𝐒𝐓𝐀𝐓𝟐𝟕𝟑/𝟮𝟳𝟭",
                    value='\u200b', inline=False)

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def engroles(ctx):
    embed = discord.Embed(

        title="Engineering College", description="", color=0xF00A0A)  # ,color=Hex code
    embed.add_field(name=":one: : 𝗖𝗘𝗡𝗚𝟭𝟲𝟬", value='\u200b', inline=False)
    embed.add_field(name=":two: : 𝗖𝗛𝗘𝗡𝗚𝟭𝟭𝟭", value='\u200b', inline=False)
    embed.add_field(name=":three: : 𝗖𝗛𝗘𝗡𝗚𝟭𝟯𝟭", value='\u200b', inline=False)
    embed.add_field(name=":four: : 𝗖𝗛𝗘𝗡𝗚𝟮𝟭𝟭", value='\u200b', inline=False)
    embed.add_field(name=":five: : 𝗖𝗛𝗘𝗡𝗚𝟮𝟭𝟯", value='\u200b', inline=False)
    embed.add_field(name=":six: : 𝗖𝗛𝗘𝗡𝗚𝟮𝟵𝟬", value='\u200b', inline=False)
    embed.add_field(name=":seven: : 𝗖𝗦𝗖𝟭𝟬𝟯", value='\u200b', inline=False)
    embed.add_field(name=":eight: : 𝗘𝗘𝗡𝗚𝟭𝟬𝟬", value='\u200b', inline=False)
    embed.add_field(name=":nine: :𝗖𝗛𝗘𝗡𝗚𝟮𝟰𝟮", value='\u200b', inline=False)
    embed.add_field(name=":a: : 𝗘𝗘𝗡𝗚𝟮𝟱𝟭", value='\u200b', inline=False)
    embed.add_field(name=":b: : 𝗘𝗘𝗡𝗚𝟮𝟳𝟭", value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_c: : 𝗘𝗡𝗚𝗟𝟭𝟬𝟭",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_d: : 𝗘𝗡𝗚𝗟𝟭𝟬2",
                    value='\u200b', inline=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def urroles(ctx):
    embed = discord.Embed(
        title="University Requirements", description="", color=0xCB9D28)  # ,color=Hex code
    embed.add_field(name=":one: : 𝐀𝐑𝐀𝐁𝟏𝟏𝟎", value='\u200b', inline=False)
    embed.add_field(name=":two: : 𝐈𝐒𝐋𝐌𝟏𝟎𝟏", value='\u200b', inline=False)
    embed.add_field(name=":three: : 𝐇𝐈𝐒𝐓𝟏𝟐𝟐", value='\u200b', inline=False)
    embed.add_field(name=":four: : 𝐇𝐑𝐋𝐂𝟏𝟎𝟕", value='\u200b', inline=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def itroles1(ctx):
    embed = discord.Embed(

        title="IT College", description="", color=0x9AE2E2)  # ,color=Hex code
    embed.add_field(name=":one: : 𝐈𝐓𝐂𝐄𝟏𝟎𝟏/𝗜𝗧𝗡𝗘𝟭𝟭𝟬",
                    value='\u200b', inline=False)
    embed.add_field(name=":two: : 𝐄𝐍𝐆𝗟𝟏𝟓𝟒", value='\u200b', inline=False)
    embed.add_field(name=":three: : 𝐄𝐍𝐆𝗟𝟏𝟓𝟓", value='\u200b', inline=False)
    embed.add_field(name=":four: : 𝐄𝐍𝐆𝗟𝟐𝟏𝟗", value='\u200b', inline=False)
    embed.add_field(name=":five: : 𝐈𝐓𝐂𝐄𝟐𝟏𝟏", value='\u200b', inline=False)
    embed.add_field(name=":six: : 𝐈𝐓𝐂𝐄𝟐𝟐𝟏", value='\u200b', inline=False)
    embed.add_field(name=":seven: : 𝐈𝐓𝐂𝐄𝟐𝟑𝟎", value='\u200b', inline=False)
    embed.add_field(name=":eight: : 𝐈𝐓𝐂𝐄𝟐𝟓𝟎/𝟏𝟏𝟐", value='\u200b', inline=False)
    embed.add_field(name=":nine: : 𝐈𝐓𝐂𝐒𝟐𝟓𝟓", value='\u200b', inline=False)
    embed.add_field(name=":a: : 𝗜𝗧𝗖𝗘𝟯𝟏𝟒/𝟮𝟱𝟮", value='\u200b', inline=False)
    embed.add_field(name=":b: : 𝐈𝐓𝐂𝐄𝟑𝟐𝟱", value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_c: : 𝐈𝐓𝐂𝐄𝟑𝟒𝟎",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_d: : 𝗜𝗧𝗖𝗘𝟯𝟱𝟯",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_e: : 𝐈𝐓𝐂𝐄𝟑𝟲𝟒 ",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_f: : 𝐈𝐓𝐂𝐄𝟑𝟳𝟎 ",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_g: : 𝐈𝐓𝐂𝐄𝟒𝟭𝟲",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_h: : 𝐈𝐓𝐂𝐄𝟒𝟱𝟑",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_i: :𝐈𝐓𝐂𝐒𝟏𝟏𝟑",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_j: :𝐈𝐓𝐂𝐒𝟏𝟏𝟒",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_k: :𝐈𝐓𝐂𝐒𝟐𝟏𝟒",
                    value='\u200b', inline=False)

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def itroles2(ctx):
    embed = discord.Embed(

        title="IT College", description="", color=0x9AE2E2)  # ,color=Hex code
    embed.add_field(name=":regional_indicator_m: : 𝐈𝐓𝐂𝐒𝟐𝟓𝟒",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_n: : 𝐈𝐓𝐂𝐒𝟐𝟖𝟓",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_o: : 𝗜𝗧𝗖𝗦𝟯𝟭𝟳 ",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_p: : 𝗜𝗧𝗖𝗦𝟯𝟮𝟭 ",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_r: : 𝐈𝐓𝐂𝐒𝟑𝟑𝟎",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_s: :𝗜𝗧𝗖𝗦𝟯𝟴𝟵",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_t: :𝗜𝗧𝗖𝗦𝟯𝟵𝟲",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_u: :𝐈𝐓𝐒𝐄𝟐𝟎𝟏",
                    value='\u200b', inline=False)
    embed.add_field(name=":regional_indicator_v: :𝗹𝗧𝗡𝗘𝟮𝟯𝟭",
                    value='\u200b', inline=False)

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
    await ctx.send(("23 december 2021"))


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


@bot.command()
async def group(ctx):
    await ctx.send("https://bit.ly/3jQPHhY")


@bot.command()
async def uobpass(ctx):
    await ctx.send("https://profile.uob.edu.bh/showLogin.cc")


@bot.command()
async def wow60(ctx):
    await ctx.send("""
<:IT:886951027725705306> :\t`IT Student`

<:engineering:886951027641827328> :\t`Engineering student`

<:analytics:886951027666980874> :\t`Business Student`

<:Science:887031756123947058> :\t`Science Student`

<:ART:886951027667009536> :\t `ART Student`""")


bot.run(token)
