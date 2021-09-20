import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.group()
    async def hello(self, ctx):
        await ctx.send("hi")

    @hello.group()
    async def hi(self, ctx):
        await ctx.send("hello")


def setup(client):
    client.add_cog(Example(client))
