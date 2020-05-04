import discord
from discord.ext import commands, tasks


def is_me(ctx):
    return ctx.author.id == 207665886092328960


class Checks11(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Check Cog is online')

    @tasks.loop(seconds=60)
    async def still_ready(self):
        print('Still ready')

    @commands.command()
    async def print_author(self, ctx):
        print(ctx.author)
        await ctx.send(ctx.author)

    @commands.command()
    @commands.check(is_me)  # Checks only for 1 command. Needs static func
    async def example(self, ctx):
        await ctx.send(f'Hi I\'m {ctx.author}')

    async def cog_check(self, ctx):  # Checks for all commands
        return ctx.author.id == 207665886092328960


def setup(client):
    client.add_cog(Checks11(client))