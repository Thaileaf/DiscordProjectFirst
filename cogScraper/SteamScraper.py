import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

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
        next_sale = soup.find('h1',{'id':'nextSale'}).text.strip('Next: ')
        sale_date = soup.find('h2',{'id':'saleDate'}).text
        details_large = soup.find('p',{'id':'detailsLarge'}).text
        main_timer = soup.find('p',{'id':'mainTimer'}).text
        sub_timer = soup.find('p',{'id':'subTimer'}).text

        try:
            confirmation = soup.find('p', {'id': 'notconfirmedLabel'}).text
        except:
            confirmation = 'confirmed'

        info = [details_large, main_timer, sub_timer, next_sale, sale_date, confirmation]
        return info

    @commands.Cog.listener()
    async def on_ready(self):
        print('Steam Scraper Ready')
        self.post_steam_sale.start()

    @tasks.loop(hours=12)
    async def post_steam_sale(self):
        pass


def setup(client):
    client.add_cog(client)




