import random
from discord.ext import commands
from discord.ext.commands import Cog

class tricks(Cog):
    def __init__(self, bot):
        self.bot = bot
    @Cog.listener()
    async def on_ready(self):
        self.bot.stdout.send(f'Tricks cog is ready!')
        print('tricks cog is ready')

    @commands.command(name='roller', help='Rolls a dice')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)]
        await ctx.send(', '.join(dice))

def setup(bot):
    bot.add_cog(tricks(bot))
