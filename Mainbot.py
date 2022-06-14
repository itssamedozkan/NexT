# bot.py
import os

import discord


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run('OTg2MzkyNjAwOTAwNjg5OTcw.GrZBGN.S6pd8xZU7rzELCNdJLU7PfHzgwakB6lpvrlfcU')