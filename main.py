import discord
from discord.ext import commands
import os

print(os.system("python -m pip install dcoder --user"))

intents = discord.Intents.default()

client = commands.Bot(command_prefix="d!", intents=intents)

for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        try:
            client.load_extension(f"cogs.{i[:-3]}")
        except Exception as e:
            print(e)
        print(f"Loaded {i}")

client.run(input("Enter the token: "))