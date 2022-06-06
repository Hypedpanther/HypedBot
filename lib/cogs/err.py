from discord.ext import commands

class err_log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You are missing a required argument.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('You have passed an invalid argument.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You are missing permissions.')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'This command is on cooldown for {error.retry_after:.2f} seconds.')
        else:
            raise error

def setup(bot):
    bot.add_cog(err_log(bot))