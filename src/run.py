import discord
from .api import *
from discord.ext import commands
from datetime import datetime, timedelta

config_color = 0x00ff00;

app = commands.Bot(command_prefix='!CTF ')

@app.event 
async def on_ready(): 
    print(app.user.name, 'has connected to Discord!') 
    await app.change_presence(status=discord.Status.online, activity=None) 

@app.command() 
async def info(ctx):

    embed = discord.Embed(title='CTFtime bot 설명서',description='디스코드를 이용하여 ctftime.org에 있는 CTF의 일정을 쉽게 확인할 수 있습니다.', color = config_color)
    embed.set_author(name="me2nuk", url="https://me2nuk.kro.kr/about/", icon_url="https://i.imgur.com/i6tFiIu.jpg")
    embed.add_field(name='!CTF week',value='현재 날짜의 일주일 전, 후에 개최되는 대회명을 나열합니다.', inline=False)
    embed.add_field(name='!CTF week_info',value='현재 날짜의 일주일 전, 후에 개최되는 대회의 상세한 정보를 나열합니다.', inline=False)
    embed.add_field(name='!CTF Td',value='오늘 진행중인 CTF의 상세한 정보를 나열합니다.', inline=False)
    embed.add_field(name='!CTF q <CTF name>',value='해당 <CTF name>의 정보를 나열합니다.', inline=False)
    embed.add_field(name='!CTF q_info <CTF name>',value='해당 <CTF name>의 상세한 정보를 나열합니다.', inline=False)
    embed.set_footer(text='초대 링크 : https://discord.com/api/oauth2/authorize?client_id=825034113413152818&permissions=0&scope=bot')
    embed.set_image(url='https://i.imgur.com/Cv39KTq.png')

    await ctx.send(embed=embed)

@app.command()
async def week(ctx):

    week_ago = (datetime.today() - timedelta(7)).strftime("%Y-%m-%dT00:00:00Z")
    week_later = (datetime.today() + timedelta(7)).strftime("%Y-%m-%dT00:00:00Z")

    r = calendar(MINTime=week_ago, MAXTime=week_later)
    result = r.urlopen()

    items = []

    for i in range(0,len(result['items'])):
        items.append(result['items'][i]['summary'])

    embed = discord.Embed(title='!CTF week',description='현재 날짜의 일주일 전, 후에 개최되는 대회명을 나열합니다.', color = config_color)
    embed.set_footer(text=('\n'+'\n'.join(items)))

    await ctx.send(embed=embed)

@app.command()
async def week_info(ctx):
    week_ago = (datetime.today() - timedelta(7)).strftime("%Y-%m-%dT00:00:00Z")
    week_later = (datetime.today() + timedelta(7)).strftime("%Y-%m-%dT00:00:00Z")

    r = calendar(MINTime=week_ago, MAXTime=week_later)
    result = r.urlopen()

    embed = discord.Embed(title='!CTF week_info',description='현재 날짜의 일주일 전, 후에 개최되는 대회의 상세한 정보를 나열합니다.', color = config_color)

    for i in range(0,len(result['items'])):
        embed.add_field(name=f"{i+1}. {result['items'][i]['summary']}",value=result['items'][i]['description'], inline=False)

    await ctx.send(embed=embed)

@app.command()
async def Td(ctx):

    week_ago = (datetime.today()).strftime("%Y-%m-%dT00:00:00Z")
    week_later = (datetime.today()).strftime("%Y-%m-%dT23:59:59Z")

    r = calendar(MINTime=week_ago, MAXTime=week_later)
    result = r.urlopen()

    print(result['items'])

    items = []

    embed = discord.Embed(title='!CTF Td',description='오늘 진행중인 CTF의 상세한 정보를 나열합니다.', color = config_color)

    for i in range(0,len(result['items'])):
        
        items.append(
            {
                'summary':result['items'][i]['summary'], 
                'description':result['items'][i]['description']
            }
        )
        
    count = 0

    if items:
        for i in items:
            if i.get('description'):
                count += 1
                embed.add_field(name=f"{count}. {i['summary']}",value=i['description'], inline=False)
    if count == 0:
        embed.set_footer(text='해당 정보를 찾지 못했습니다.')
    else:
        embed.set_footer(text='해당 정보를 찾지 못했습니다.')

    await ctx.send(embed=embed)

@app.command()
async def q(ctx, *text):

    Search = '%20'.join([i for i in text])

    info = ' '.join([i for i in text])

    embed = discord.Embed(title='CTFtime q', description='해당 {}의 정보를 나열합니다.'.format(info), color = config_color)

    items = []

    r = calendar_Queries(Search=Search)
    result = r.urlopen()

    for i in range(0, len(result['items'])):
        items.append(result['items'][i]['summary'])

    if items:
        embed.set_footer(text=('\n'+'\n'.join(items)))

    else:
        embed.set_footer(text=('\n'+'\n'.join(items)))

    await ctx.send(embed=embed)

@app.command()
async def q_info(ctx, *text):

    Search = '%20'.join([i for i in text])
    r = calendar_Queries(Search=Search)
    result = r.urlopen()

    info = ' '.join([i for i in text])

    embed = discord.Embed(title='!CTF q_info',description=f'해당 {info} 의 정보를 나열합니다.', color = config_color)

    items = []

    for i in range(0,len(result['items'])):
        if result['items'][i].get('description'):    
            items.append(
                {
                    'summary':result['items'][i]['summary'], 
                    'description':result['items'][i]['description']
                }
            )

    count = 0

    if items:

        for i in items:
            if i.get('description'):
                count += 1
                embed.add_field(name=f"{count}. {i['summary']}",value=i['description'], inline=False)

    elif count == 0:

        embed.set_footer(text='해당 정보를 찾지 못했습니다.')

    else:

        embed.set_footer(text='해당 정보를 찾지 못했습니다.')

    await ctx.send(embed=embed)