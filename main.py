import discord
from discord.ext import commands
import os

intents = discord.Intents.default()

client = commands.Bot(command_prefix="d!", intents=intents)

@client.event
async def on_ready(*args, **kwargs):
    print("I am ready")
    print(args)
    print(kwargs)


for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        client.load_extension(f"cogs.{i[:-3]}")
        print(f"Loaded {i}")

client.run(input("Enter the token: "))