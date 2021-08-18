from twitchio.ext import commands, pubsub
from config import token_
import asyncio
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

database = []


class order:
    name = None
    game = None

    def __init__(self, name, game):
        self.name = name
        self.game = game     


f = open('games.txt', 'r')
for line in f.readlines():
    print(line)
    line = line.split()
    name = line[0]
    print(name)
    line.pop(0)
    game = ' '.join(line)
    print(game)
    database.append(order(name, game))
f.close()

print(database)

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=str(token_), prefix='?',initial_channels=['BuyWell','ze6ypo'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Нюхай бебру {ctx.author.name}!')

    @commands.command()
    async def addgame(self, ctx: commands.Context):
        print(ctx.author.is_subscriber)
        if True:
            print(ctx.author.is_subscriber)
            print(ctx.message.content)
            str = ctx.message.content.split()
            str.pop(0)
            game = ' '.join(str)
            print(game)
            name = ctx.author.name
            print(name)
            database.append(order(name, game))
            with open('games.txt', 'w') as file:
                for person in database:
                    file.write(person.name + ' ' + person.game + '\n')
            with open('RGG Roll/lists/wheel.dat', 'w') as file:
                for person in database:
                    file.write(person.game + '\n')
            await ctx.send(f' {ctx.author.name} добавил')

    @commands.command()
    async def gamelist(self, ctx: commands.Context):
        text = ''
        for person in database:
            text += person.name + ' - ' + person.game + '; '
        print(text)
        await ctx.send(text)

    @commands.command()
    async def porf(self, ctx: commands.Context):
        driver = webdriver.Chrome()
        driver.get("https://porfirevich.ru")
        element = driver.find_element_by_class_name("ql-editor")
        str = ctx.message.content.split()
        str.pop(0)
        text2 = ' '.join(str)
        element.send_keys(text2)
        element.send_keys(Keys.TAB)
        await asyncio.sleep(10)
        new_text = driver.find_elements_by_tag_name("strong")
        for elem in range(len(new_text)):
            await asyncio.sleep(5)
            if elem == 1:
                print(new_text[elem].text)
                text2 += new_text[elem].text
        await ctx.send(text2)
        driver.quit()

bot = Bot()
bot.run()
