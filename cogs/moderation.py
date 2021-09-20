import discord
from discord.ext import commands
import platform
import asyncio
import re

import utils.json

time_regex = re.compile("(?:(\d{1,5})(d|h|m|s))+?")
time_dict = {"d": 86400, "h": 3600, "m": 60, "s": 1}


class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = agrument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += tune_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(f"{value} is an invalid time key. d|h|m|s are valid arguments")
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number.")
        return time


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(name="mute", description="Mutes a specified user for a specified time.", ussage="<user> [time]")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, time: TimeConverter = None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            await ctx.send("No muted role was found. Please create one called `Muted`.")
            return

        await member.add_roles(role)
        await ctx.send(f"Muted `{member.display_name}` for {time}s." if time else f"Muted `{member.display_name}`.")

        if time:
            await asyncio.sleep(time)

            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f"Unmuted `{member.display_name}`.")

    @commands.command(name="unmute", description="Unmutes a specified user.", ussage="<user>")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            await ctx.send("No muted role was found. Please create one called `Muted`.")
            return

        if role not in member.roles:
            await ctx.send(f"`{member.display_name}` is not muted.")
        await member.remove_roles(role)
        await ctx.send(f"Unmuted `{member.display_name}`.")


    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)

        channel = self.bot.get_channel(805652712598405190)
        embed = discord.Embed(title=f"{ctx.author.name} kicked: {member.name}", description=reason)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(user=member, reason=reason)

        channel = self.bot.get_channel(805652712598405190)
        embed = discord.Embed(title=f"{ctx.author.name} banned: {member.name}", description=reason)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)

        channel = self.bot.get_channel(805652712598405190)
        embed = discord.Embed(title=f"{ctx.author.name} unbanned: {member.name}", description=reason)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount + 1)
        channel = self.bot.get_channel(805652712598405190)
        embed = discord.Embed(title=f"{ctx.author.name} purged: {ctx.channel.name}",
                              description=f"{amount} messages were cleared.")
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
