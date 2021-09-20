import discord
from discord.ext import commands
import platform
import random

import utils.json


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    async def stats(self, ctx):
        """
        Bot Statistics
        """

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        statsEmbed = discord.Embed(title=f"{self.bot.user.name} Stats", description="\uFEFF", color=ctx.author.color,
                                   timestamp=ctx.message.created_at)
        statsEmbed.add_field(name="Bot Version: ", value=self.bot.version)
        statsEmbed.add_field(name="Python Version: ", value=pythonVersion)
        statsEmbed.add_field(name="Discord.py Version: ", value=dpyVersion)
        statsEmbed.add_field(name="Total Guilds: ", value=str(serverCount))
        statsEmbed.add_field(name="Total Members: ", value=str(memberCount))
        statsEmbed.add_field(name="Bot Developers: ", value="<@182278697804365824>")

        statsEmbed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
        statsEmbed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=statsEmbed)



def setup(bot):
    bot.add_cog(Misc(bot))
