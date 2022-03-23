import random
from discord.ext import commands

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='roll', help='Rolls a dice')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)]
        await ctx.send(', '.join(dice))

def setup(bot):
    bot.add_cog(dice(bot))
