import discord
from discord.ext import commands, tasks
import os
import pyowm
import psutil
import random


class Howgay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def howgay(self, ctx, member: discord.Member):
        author = ctx.message.author
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        gay_rate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29,
                    30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                    57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
                    82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 96, 98, 99, 100]

        embed.set_author(name="• Howgay?")
        embed.add_field(name="You are...", value=f"{random.choice(gay_rate)}% gay :gay_pride_flag: → {str(member.mention)}")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Howgay(client))