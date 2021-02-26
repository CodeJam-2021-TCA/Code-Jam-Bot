import discord 
from discord.ext import commands
import json

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(nmae="help", aliases=["commands", "who-tf-are-you"])
    async def help(self, ctx, subcommand="default"):
        with open('helpCommand.json', "r") as f:
            data = json.load(f)

        try: 
            embed = discord.Embed.from_dict(data[subcommand.lower()])
        except KeyError:
            return await ctx.send("Not a valid command use `d!help` to see all the commands.")

        await ctx.send(embed=embed)
        
        

    
def setup(client):
    client.add_cog(Help(client))