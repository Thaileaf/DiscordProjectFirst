import discord
from discord.ext import commands, tasks
import asyncio
import random

class AnimalRace(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.reactions = {}
        self.race = 'Waiting'
        self.message = None
        self.time = 20
        self.goal = 30
        self.is_race_going = False

    @commands.command()
    async def dick_race(self, ctx):
        await ctx.send('React to enter it in the the dick race')
        self.message = await ctx.send(self.race)
        for i in range(self.time, 0, -1):
            if self.reactions:
                self.race = f'{i} seconds remaining\n>>> '
                for reaction in self.reactions:
                    self.race = f'{self.race}{reaction}\n'
                await self.message.edit(content=self.race)
            await asyncio.sleep(1)
        for i in range(3, 0, -1):
            self.race = f'{i}...\n>>> '
            for reaction in self.reactions:
                self.race = f'{self.race}{reaction}\n'
            await self.message.edit(content=self.race)
            await asyncio.sleep(1)
        self.is_race_going = True
        while True:
            try:
                run_amount = round(random.triangular(0, 5, 2))
                runner = random.choice(list(self.reactions.keys()))
                if self.reactions[runner][1] > self.goal:
                    converter = commands.MemberConverter()
                    await ctx.send(f'{runner} reaction by {self.reactions[runner][0].mention} won by cheating like the bitch they are but has the biggest dick')
                    self.is_race_going = False
                    break
                else:
                    self.reactions[runner][1] += run_amount
                self.race = f'\n>>> '
                for reaction in self.reactions:
                    left = self.goal - self.reactions[reaction][1]
                    self.race = f'{self.race}' + f' ' * self.reactions[reaction][1] + f'{reaction}' + f' ' * left + f'|\n'
                await self.message.edit(content=self.race)
                await asyncio.sleep(.5)
            except Exception as e:
                print(e)
                break




    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if not self.reactions or user not in list(self.reactions.values())[0] and reaction not in list(self.reactions.keys()):
            await reaction.message.add_reaction(reaction.emoji)
            self.reactions.update({reaction: [user, 0]})

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if self.is_race_going:
            self.reactions[reaction][1] += 1
        print('hi')





def setup(client):
    client.add_cog(AnimalRace(client))