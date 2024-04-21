import discord
from discord.ext import commands
from model import get_class
import random
import os



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def mem(ctx):
    img_name = (random.choice(os.listdir('images')))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def advice(ctx):
    advices = random.choice([' Попробуйте уменьшить потребление энергии.','Поддерживайте и участвуйте в зеленых инициативах.','Изучайте информацию о проблеме глобального потепления и действуйте в соответствии с полученными знаниями.'])
    await ctx.send(advices)



@bot.command()
async def check(ctx):
    if ctx.message.attachments:
       for attachment in ctx.message.attachments:
           file_name = attachment.filename
           file_url = attachment.url
           await attachment.save(f'images/{file_name}')
           result = get_class(model="keras_model.h5", labels="labels.txt", image=f"images/{file_name}")
           await ctx.send(result)
           if result[1] == 'метал':
               print('+')
           else:
               print('-')

    elif ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            result = get_class(model="keras_model.h5", labels="labels.txt", image=f"images/{file_name}")
            await ctx.send(result)
            if result[0] == 'стекло':
                print('+')
            else:
                print('-')

    elif ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            result = get_class(model="keras_model.h5", labels="labels.txt", image=f"images/{file_name}")
            await ctx.send(result)
            if result[2] == 'пластик':
                print('+')
            else:
                print('-')
    else:
        await ctx.send('Вы забыли загрузить картинку')
        
