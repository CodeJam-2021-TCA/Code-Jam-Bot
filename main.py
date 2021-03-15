import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="d!", case_insensitive=True, help_command=None)

@client.event
async def on_command_error(ctx, error):
    if hasattr(error, "original"):
        error = error.original

    if isinstance(error, commands.errors.CommandNotFound):
        pass
    else:
        await ctx.send(f"An Error occured {str(error)}.")


@client.event
async def on_ready():
    print("I am Ready 👋🏻.")

for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        try:
            client.load_extension(f"cogs.{i[:-3]}")
        except Exception as e:
            print(e)
        print(f"Loaded {i}")

client.run(input("Enter the token: "))
