import discord
from discord.ext import commands

class Decode(commands.Cog):
    def __init__(self, client):
        self.client = client
        print(f"{__name__} Successfully loaded.")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("OH ok, i am here")

    
def setup(client):
    client.add_cog(Decode(client))
