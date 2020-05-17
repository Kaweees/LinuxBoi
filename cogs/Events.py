# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import discord
from discord.ext import commands

from logging_files.events_logging import logger


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # - TODO: Get default channel and create a nice embed to send a message about basic info about bot
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        logger.info(f"Events | Joined Guild: {guild.name} | ID: {guild.id}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        logger.info(f"Events | Left Guild: {guild.name} | ID: {guild.id}")


def setup(bot):
    bot.add_cog(Events(bot))
