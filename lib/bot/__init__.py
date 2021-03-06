import os
from asyncio import sleep
from datetime import datetime
from glob import glob
from sqlite3 import Timestamp
from time import sleep

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Color, Embed, Intents, file
from discord.ext.commands import Bot as _Bot
from discord.ext.commands import CommandNotFound
from isort import file

from ..db import db

PREFIX = "&"
OWNER_IDS = []
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)
    
    def ready_cog(self, cog):
        setattr(self, cog, True)
        print (f"{cog} is ready")
    
    def all_ready(self):
        return all(getattr(self, cog) for cog in COGS)

class Bot(_Bot):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        db.autosave(self.scheduler)
        super().__init__(
         command_prefix=PREFIX,
         owner_ids=OWNER_IDS, 
         intents=Intents.all()
        )
    
    def cog_setup(self):
        for cog in COGS:
            try:
                self.load_extension(f'lib.cogs.{cog}')
                print (f'loaded cog {cog}')
            except Exception as e:
                print(f'Failed to load extension lib.cogs.{cog}')
                print(e)
        print(f'cogs have been loaded!')
    
 
    def run(self, version):
        self.VERSION = version

        print('Initialising bot...')
        
        setup = False
        while not setup:
            self.cog_setup()
            setup = True

        with open ("./lib/bot/token.0", "r", encoding='utf-8') as tf:
            self.TOKEN = tf.read()
        print(f'running bot ...')
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print(f'bot has connected to Discord!')

    async def on_disconnect(self):
        print(f'bot has disconnected from Discord!')
   
    async def on_ready(self):
        if not self.ready:
           
            self.scheduler.start()
            self.guild = self.get_guild(947913659840086076)
            self.stdout = self.get_channel(947913659840086079)
            await self.stdout.send(f'I am now online!')

            embed = Embed(
                title="Bot is now online!",
                description=f"Version: {self.VERSION}",
                color=Color.blue(),
                timestamp = datetime.utcnow()
            )
            fields = [('Author', 'HypedPanther', True),
            ('Name', 'HypedBot', True),
            ('Status', 'Experimental', False ),]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name=f"HypedBot", icon_url=self.guild.icon_url)
            embed.set_footer(text=f"{self.guild.name}", icon_url=self.guild.icon_url)
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            await self.stdout.send(embed=embed)

            while not self.cogs_ready.all_ready():
                await sleep(1)
            self.ready = True
            print(f'bot is ready!' )
        
        elif self.ready:
            print(f'bot is reconnected!')  

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

    async def on_error(self, err, *args, **kwargs):
        if err == 'on_comand_error':
            await args[0].send(f'Something has gone wrong!')
            await self.stdout.send(f'An error has occured!')
            raise err
    
    async def on_command_error(self, error):
        if isinstance(error, CommandNotFound):
            pass
        elif hasattr(error, 'original'):
            raise error.original
        else:
            error

        
bot = Bot()
