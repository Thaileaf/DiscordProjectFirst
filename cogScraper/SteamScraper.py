import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import json

class SteamScraper(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.url = 'https://www.whenisthenextsteamsale.com/'



    def get_time_left(self):
        driver = webdriver.Chrome(chrome_options=self.chrome_options)
        driver.get(self.url)

        script = driver.execute_script('return document.documentElement.outerHTML')
        html = soup(script, 'html.parser')
        next_sale = html.find('h1',{'id':'nextSale'}).text.lstrip('Next: ') # Name of sale
        sale_date = html.find('h2',{'id':'saleDate'}).text # Calender date
        details_large = html.find('p',{'id':'detailsLarge'}).text # Weeks left
        main_timer = html.find('p',{'id':'mainTimer'}).text #
        sub_timer = html.find('p',{'id':'subTimer'}).text

        try:
            confirmation = html.find('p', {'id': 'notconfirmedLabel'}).text.strip('\n')
        except:
            confirmation = 'confirmed'

        info = [details_large, main_timer, sub_timer, next_sale, sale_date, confirmation]
        driver.quit()
        return info



    @commands.Cog.listener()
    async def on_ready(self):
        # Prints message when cog is online
        print('Steam Scraper Ready')
        # self.post_steam_sale.start()

    @commands.command()
    async def set_channel(self, ctx):
        # Sets whatever channel this command was called in the default place to post steam sales
        with open('../DiscordSettings/SteamScraperSettings.json', 'r+') as f:
            channel_dict = json.load(f)
            channel_dict[ctx.guild] = ctx.channel
            f.seek(0)
            json.dump(channel_dict, f)
            f.truncate()

    @commands.command()
    async def check_sale(self, ctx):
        print('hello')
        try:
            info = await self.get_time_left()
            await ctx.send(
                f'''
                            Upcoming Steam Sale:\n
                            {info[3]}\n
                            {info[4]} {info[5]}\n
                            {info[0]}\n
                            {info[1]}\n
                            {info[2]}\n
                            ''')
        except Exception as e:
            print(e)

    # @tasks.loop(hours=12)
    # async def post_steam_sale(self):
    #     pass


def setup(client):
    client.add_cog(SteamScraper(client))





