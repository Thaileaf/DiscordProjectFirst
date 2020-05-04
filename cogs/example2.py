import discord
from discord.ext import commands


class Exaxmple2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example2 cog is online')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Ping!')

def setup(client):
    client.add_cog(Exaxmple2(client))