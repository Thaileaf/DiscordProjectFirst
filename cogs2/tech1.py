import discord
from discord.ext import commands, tasks

class Tech1(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.id = 308132483436642306
        self.guild = self.client.get_guild(308132483436642306)
        self.channel = 'ai'

    @commands.Cog.listener()
    async def on_message(self, message):
        print('hello')
        if message.content.find('number') != -1:
            if str(message.channel) == self.channel:
                await message.channel.send(f'there are {self.guild.member_count} people in this server')






def setup(client):
    client.add_cog(Tech1(client))