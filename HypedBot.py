# Hypedbot.py
import os
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

@bot.event
async def on_member_join(member):
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    dm_channel = await member.create_dm()
    await dm_channel.send(
        f'Hi {member.name}, welcome to {guild.name} server!'
    )

if __name__ == '__main__':
    load_cogs()
    bot.run(TOKEN)
