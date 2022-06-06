import json
from datetime import datetime
from aiohttp import ClientSession
from discord import Color, Embed
from discord.ext.commands import Cog, command


class weather(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_cog("Weather")

    @command(name='weather', help='Gets the weather for a given city')
    async def weather(self, ctx, city:str):
        with open("settings\\weather_config.json", "r") as jsonfile:
                data = json.load(jsonfile)
                weather_api_key = data["weather_api_key"]
                base_url = data["weather_url"]
                url = f'{base_url}?q={city}&appid={weather_api_key}&units=metric'
        async with ClientSession() as session:
            async with session.get(url) as resp:
                r = resp.json()
        if r["cod"] != "404":
            async with ctx.message.channel.typing():
                current_temperature = r["main"]["temp"]
                current_pressure = r["main"]["pressure"]
                current_humidity = r["main"]["humidity"]
                weather_description = r["weather"][0]["description"]
                embed = Embed(
                    title=f"Weather in {city}",
                    color= Color.green(),
                    timestamp=datetime.utcnow()
                    )

                fields = [("Descripition", f"**{weather_description}**",False),
                "Temperature(C)", f"**{current_temperature}°C**",False,
                ("Humidity(%)", f"**{current_humidity}%**",False),
                ("Atmospheric Pressure(hPa)",f"**{current_pressure}hPa**",False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            await ctx.send("City Not Found")

def setup(bot):
    bot.add_cog(weather(bot))
