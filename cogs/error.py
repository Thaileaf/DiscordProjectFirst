import discord
from discord.ext import commands


class Error(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please send in all required arguments')

    # @commands.command()
    # async def clear(self, ctx, amount: int):
    #     await ctx.channel.purge(limit=amount)
    #
    # @clear.error
    # async def clear_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send('Please specify amount of messages to delete')



def setup(client):
    client.add_cog(Error(client))