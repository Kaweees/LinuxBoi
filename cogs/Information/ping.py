import discord
from discord.ext import commands
from logging_files.information_logging import logger


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        ping = str(round(self.client.latency * 1000))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Ping command", value="• The latency is " + ping + "ms")

        await ctx.send(embed=embed)

        await logger.info(f"Information | Sent Ping: {ctx.author}")


def setup(client):
    client.add_cog(Ping(client))
