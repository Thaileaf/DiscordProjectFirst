import discord
from discord.ext import commands, tasks

class Snake(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.