import discord
import json
import requests
from discord.ext import commands
import aiohttp
 
class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='weather', help='Gets the weather for a given city')
    async def weather(self, ctx, city: str):
        async with aiohttp.ClientSession() as session:
            with open("HypedBot\config.json", "r") as jsonfile:
                data = json.load(jsonfile)
                weather_api_key = data["weather_api_key"]
                base_url = data["weather_url"]
                url = f'{base_url}?q={city}&appid={weather_api_key}&units=metric'
                response = requests.get(url)
                x = response.json()
                channel = ctx.message.channel
                if x["cod"] != "404":
                    async with channel.typing():
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_pressure = y["pressure"]
                        current_humidity = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        embed = discord.Embed(title=f"Weather in {city}",color=ctx.guild.me.top_role.color,
                        timestamp=ctx.message.created_at,)
                        embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
                        embed.add_field(name="Temperature(C)", value=f"**{current_temperature}°C**", inline=False)
                        embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                        embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                        embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                        embed.set_footer(text=f"Requested by {ctx.author.name}")
                        await channel.send(embed=embed)
                else:
                    await channel.send("City not found.")

def setup(bot):
    bot.add_cog(weather(bot))