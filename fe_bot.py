from random import randint
import random
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

def roll_d6():
    outcome = randint(1, 6)
    if outcome == 1:
        return ":one:"
    elif outcome == 2:
        return ":two:"
    elif outcome == 3:
        return ":three:"
    elif outcome == 4:
        return ":four:"
    elif outcome == 5:
        return ":five:"
    elif outcome == 6:
        return ":six:"


Client = discord.Client()
bot_prefix = "fe."
client = commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_ready():
    print("Bot Online")
    print("Name: {}".format(client.user.name))


@client.command(pass_context=True)
async def roll():
    await client.say(roll_d6() + roll_d6() + roll_d6())


@client.command(pass_context=True)
async def new_char():
    await client.say("Create New Char")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$generate'):
        await client.send_message(message.channel, "What level of resources?")

        def res_level(m):
            return m.content.isdigit()

        res = await client.wait_for_message(timeout=5.0, author=message.author, check=res_level)

        if res is None:
            fmt = "Sorry, you took too long."
            await client.send_message(message.channel, fmt)
            return
        if int(res.content) == 1:
            points = 1

            variantN = randint(0, 10)
            shellsN = randint(0, 10)
            variant = ""
            shells = ""

            if (variantN == 0):
                variant = "Burst Spores"
            elif (variantN == 1):
                variant = "Gauss"
            elif (variantN == 2):
                variant = "Ion"
            elif (variantN == 3):
                variant = "Irradiated"
            elif (variantN == 4):
                variant = "Particle"
            elif (variantN == 5):
                variant = "Rail"
            elif (variantN == 6):
                variant = "Self-Propelled"
            elif (variantN == 7):
                variant = "Spine Launcher"
            elif (variantN >= 8):
                variant = "Standard"

            if (shellsN == 0):
                shells = "Dispersion"
            elif (shellsN == 1):
                shells = "Dummy"
            elif (shellsN == 2):
                shells = "Electro-Gravity"
            elif (shellsN == 3):
                shells = "Kinetic"
            elif (shellsN == 4):
                shells = "Shrapnel"
            elif (shellsN == 5):
                shells = "Smoke"
            elif (shellsN == 6):
                shells = "Snare"
            elif (shellsN >= 7):
                shells = "Normal"



            await client.send_message(message.channel, "Pistol; with " + variant + " variation and " + shells + " shells.")
        elif int(res.content) == 2:
            await client.send_message(message.channel, "res level 2")
        else:
            await client.send_message(message.channel, "Invalid option")


@client.command(pass_context=True)
async def loot(res: int):
    await client.say(res)


client.run(os.environ["DiscordBot"])
