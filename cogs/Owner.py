"""
LinuxBoi - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import random
import discord
from discord.ext import commands
from logging_files.owner_logging import logger


class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, activity, *, status):
        # Type 0 = Playing a game, Type 1 = Live on Twitch, Type 2 = Listening, Type 3 = Watching
        await self.client.change_presence(activity=discord.Activity(type=activity, name=status))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Bot status changed!",
            description=f"• My status has been updated to: `{status}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent Status: {ctx.author} | Activity: {activity} | Status: {status}")

    @status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="Please put a valid option! Example: `l!status <type> <status>`"
            )
            await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def guilds(self, ctx):
        for guild in self.client.guilds:
            await ctx.send(f"Guild: {guild} | ID: {guild.id}")

    @commands.is_owner()
    @commands.command()
    async def get_invite(self, ctx, id: int):
        guild = self.client.get_guild(id)

        for channel in guild.text_channels:
            channels = [channel.id]

        picked = random.choice(channels)
        channel = self.client.get_channel(picked)

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title=f"→ Invite from guild",
            description=f"• Invite: {await channel.create_invite(max_uses=1)}"
        )

        await ctx.author.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message):
        await channel.send(message)

        logger.info(f"Fun | Sent Say: {ctx.author}")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Channel!",
                description="• Please put a valid channel! Example: `l!say #channel <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!say #channel <message>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Shutdown",
            description="• Performing a shutdown on the bot... ( :wave: )"
        )

        await ctx.send(embed=embed)
        await self.client.logout()

        logger.info(f"Owner | Sent Shutdown: {ctx.author}")


def setup(client):
    client.add_cog(Owner(client))