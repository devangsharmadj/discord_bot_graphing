from dtoken import TOKEN
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='/', description="data graphing bot")

@bot.event
async def on_ready():    
    print('Logged in as')    
    print(bot.user.name)    
    print(bot.user.id)    
    print('------')@bot.event
async def on_message(message):    
    await bot.process_commands(message)
@bot.command()
async def hey(ctx):    
    await ctx.send("hey")


bot.run(TOKEN)