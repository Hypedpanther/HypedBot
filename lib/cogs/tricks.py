import random
from discord.ext.commands import Cog, command

class tricks(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_sender = None
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_cog("tricks")

    @command(name='hello', help='Returns Greeting to User', aliases=['hi', 'hey', 'sup', 'yo', 'hola'])
    async def greeting(self, ctx):
        greetings = [
            f'Hello {ctx.author.name}!',f'Hi {ctx.author.name}!',f'Hey {ctx.author.name}!',
            f'Howdy {ctx.author.name}!',f'Greetings {ctx.author.name}!', f'Sup {ctx.author.name}!']
        response = random.choice(greetings)
        if self.last_sender != ctx.author.id:
            self.last_sender = ctx.author.id
            await ctx.send(response)
        else:
            await ctx.send(f'{ctx.author.name}, This feels like a good time to say a greeting again!, {response}')
    

def setup(bot):
    bot.add_cog(tricks(bot))
