import discord
from discord.ext import commands
import dcoder

class Decode(commands.Cog):
    def __init__(self, client):
        self.client = client
        print(f"{__name__} Successfully loaded.")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("OH ok, i am here")
    

    @commands.group(name="decode")
    async def decode(self, ctx, option=None):
        if option is None:
            embed = discord.Embed()
            await ctx.send(embed=embed)        
    

    @decode.command(name="test")
    async def test(self, ctx):
        await self.test(ctx)


    
def setup(client):
    client.add_cog(Decode(client))
