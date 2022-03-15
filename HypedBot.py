# Hypedbot.py
import os
from turtle import color
import discord
from flask import Blueprint
from webserver import keep_alive
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', case_insensitive=True)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(f'Failed to load extension {filename}.')
                print(e)

def main():
    load_cogs()
    keep_alive()
    bot.run(TOKEN)
    
if __name__ == '__main__':
    main()
