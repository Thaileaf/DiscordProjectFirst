import discord
from discord.ext import commands, tasks
from cogs import AnimalRace

class Tetris(commands.Cog):

    def __init__(self, client):
        self.client = client

