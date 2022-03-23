from discord.ext import commands


class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.bot.get_channel(952684786860834896).send(
            f'Welcome to **{member.guild.name}**{member.mention} go check out <#947913659840086079> to say hi!')
        await member.send(f'Wlecome to **{member.guild.name}**{member.mention} be sure to enjoy your time here!')

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        pass


def setup(bot):
    bot.add_cog(welcome(bot))