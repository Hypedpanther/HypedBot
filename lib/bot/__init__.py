from sqlite3 import Timestamp
from discord import Intents
from datetime import datetime
from discord import Color
from discord import Embed
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Bot as _Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from isort import file


PREFIX = "&"
OWNER_IDS = []
class Bot(_Bot):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().__init__(
         command_prefix=PREFIX,
         owner_ids=OWNER_IDS, 
         intents=Intents.all()
        )
    
    def run(self, version):
        self.VERSION = version
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
            self.ready = True
            self.guild = self.get_guild()
            print(f'bot is ready!') 
             
            channel = self.get_channel()
            await channel.send(f'I am now online!')

            embed = Embed(
                title="Bot is now online!",
                description=f"Version: {self.VERSION}",
                color=Color.blue(),
                timestamp = datetime.utcnow()
            )
            fields = [('Author', 'Author', True),
            ('Name', 'HypedBot', True),
            ('Status', 'Experimental', False ),]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name=f"HypedBot", icon_url=self.guild.icon_url)
            embed.set_footer(text=f"{self.guild.name}", icon_url=self.guild.icon_url)
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            await channel.send(embed=embed)

            #await channel.send(file=file("./data/images/hypedbot.png"))
        
        elif self.ready:
            print(f'bot is reconnected!')  

    async def on_message(self, message):
        pass
    async def on_error(self, err, *args, **kwargs):
        if err == 'on_comand_error':
            await args[0].send(f'An error has occured!')
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            pass
        elif hasattr(error, 'original'):
            raise error.original
        else:
            error
bot = Bot()