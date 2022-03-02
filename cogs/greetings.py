import random
from discord.ext import commands

class greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='hello', help='greets the user')
    async def greeting(self, ctx):
        greetings = [
            f'Hello {ctx.author.name}!',f'Hi {ctx.author.name}!',f'Hey {ctx.author.name}!',
            f'Howdy {ctx.author.name}!',f'Greetings {ctx.author.name}!']
        response = random.choice(greetings)
        await ctx.send(response)


def setup(bot):
    bot.add_cog(greetings(bot))