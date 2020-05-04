import discord
from discord.ext import commands, tasks
import asyncio


class EditCog(commands.Cog):


    def __init__(self, client):
        self.client = client
        self.message = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('EditCog is ready')

    @commands.command()
    async def print_line(self, ctx):
        self.message.clear()
        try:
            self.message.append(await ctx.send('-'))
            self.message.append(await ctx.send('.'))
            self.message.append(await ctx.send('a'))
            for i in range(2, 10):
                await asyncio.sleep(1)
                await self.message[0].edit(content='-'*i)
                await self.message[1].edit(content='.'*i)
                await self.message[2].edit(content='a'*i)
        except Exception as e:
            print(e)

    @tasks.loop(seconds=5)
    async def copy(self):
        await self.message.edit('--------')

    @tasks.loop(seconds=60)
    async def gah(self):
        await None


def setup(client):
    client.add_cog(EditCog(client))