from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

class notification(commands.Cog):
    def __init__(self, bot):
        self.scheduler = AsyncIOScheduler()
        self.bot = bot
        
    @commands.Cog.listener()
    async def print_message(self):
        channel = self.get_channel(947913659840086079)
        await channel.send('Weekly reminder: Check out the HypedBot Github!')
    async def notification(self):
        self.scheduler.add_job(self.print_message, CronTrigger(second = 0))#(day_of_week = 0, hour=12, minute=0))

def setup(bot):
    bot.add_cog(notification(bot))