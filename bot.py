# Import Discord Package
import discord
from discord.ext import commands
import logging
from pathlib import Path
import json
# import pandas as pd
# import subprocess
# import pyautogui
# import time
# import keyboard
# import random
# import win32api, win32con, win32gui
import os
import motor.motor_asyncio

import utils.json
from utils.mongo import Document

# Getting the Directory
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")


async def get_prefix(bot, message):
    # Checks if it is gotten in a DM
    if not message.guild:
        return commands.when_mentioned_or("-")(bot, message)

    try:
        data = await bot.config.find(message.guild.id)

        # Make sure we have a usable prefix
        if not data or "prefix" not in data:
            return commands.when_mentioned_or("-")(bot, message)
        return commands.when_mentioned_or(data["prefix"])(bot, message)
    except:
        return commands.when_mentioned_or("-")(bot, message)


# Defining Info
secret_file = json.load(open(cwd + "/bot_config/secrets.json"))
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, owner_id=182278697804365824)
bot.config_token = secret_file["token"]
bot.connection_url = secret_file["mongo"]
logging.basicConfig(level=logging.INFO)

bot.blacklisted_users = []
bot.cwd = cwd

bot.version = "0.0.1"

bot.colors = {
    'WHITE': 0xFFFFFF,
    'AQUA': 0x1ABC9C,
    'GREEN': 0x2ECC71,
    'BLUE': 0x3498DB,
    'PURPLE': 0x9B59B6,
    'LUMINOUS_VIVID_PINK': 0xE91E63,
    'GOLD': 0xF1C40F,
    'ORANGE': 0xE67E22,
    'RED': 0xE74C3C,
    'NAVY': 0x34495E,
    'DARK_AQUA': 0x11806A,
    'DARK_GREEN': 0x1F8B4C,
    'DARK_BLUE': 0x206694,
    'DARK_PURPLE': 0x71368A,
    'DARK_VIVID_PINK': 0xAD1457,
    'DARK_GOLD': 0xC27C0E,
    'DARK_ORANGE': 0xA84300,
    'DARK_RED': 0x992D22,
    'DARK_NAVY': 0x2C3E50
}
bot.color_list = [c for c in bot.colors.values()]


@bot.event
async def on_ready():
    # Functionality (DO STUFF)
    # change_status.start()
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Getting Is Top'))

    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(bot.connection_url))
    bot.db = bot.mongo["DanBot"]
    bot.config = Document(bot.db, "config")
    print("Initialized Database\n-----")
    for document in await bot.config.get_all():
        print(document)


@bot.event
async def on_message(message):
    # Ignore the bot
    if message.author.id == bot.user.id:
        return

    # Blacklist system
    if message.author.id in bot.blacklisted_users:
        return

    # Whenever the bot is tagged, respond with its prefix
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        data = await bot.config.get_by_id(message.guild.id)
        if not data or "prefix" not in data:
            prefix = "-"
        else:
            prefix = data["prefix"]
        await message.channel.send(f"My prefix is `{prefix}`. This message will delete after `15` seconds", delete_after=15)

    await bot.process_commands(message)


if __name__ == "__main__":
    for filename in os.listdir(cwd + '/cogs'):
        if filename.endswith('.py') and not filename.startswith("_"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    bot.run(bot.config_token)
