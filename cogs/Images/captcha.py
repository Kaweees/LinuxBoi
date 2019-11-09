import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Captcha(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def captcha(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={ctx.author.avatar_url_as(size=4096, format=None, static_format='png')}&username=Orange") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ Captcha Verification")
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Captcha: {ctx.author}")


def setup(client):
    client.add_cog(Captcha(client))
