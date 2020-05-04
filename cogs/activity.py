import discord
from discord.ext import commands, tasks
from itertools import cycle

class Activity(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.activity = cycle(['Piss simulator 2k21', 'Pissing on some nerds', 'Floor piss', 'Not pissing', 'Pizz'])

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_activity.start()
        await self.client.change_presence(activity=discord.Game('Pissing Simulator 2k19'))

    @tasks.loop(seconds=60)
    async def change_activity(self):
        await self.client.change_presence(activity=discord.Game(next(self.activity)))



def setup(client):
    client.add_cog(Activity(client))
