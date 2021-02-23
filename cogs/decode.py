import discord
from discord.ext import commands
import dcoder

class Decode(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("OH ok, i am here")
    
    @commands.group(name="decode")
    async def decode(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Will do it later LOL")
            await ctx.send(embed=embed)  
    
    @decode.command(name="binary", aliases=['binary2text', 'binarytotext'])
    async def binary(self, ctx, *, text):
        output = dcoder.bin2text(text)

        embed = discord.Embed(color=0xfffff0, title="Decocded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
        
    @decode.command(name="octal", aliases=["octal2text", 'octaltotext'])
    async def octal(self, ctx, *, text):
        output = dcoder.oct2text(text)

        embed = discord.Embed(color=0xfffff0, title="Decocded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
    
    @decode.command(name="hex", aliases=['hex2text', 'hextotext'])
    async def hexadecimal(self, ctx, *, text):
        output = dcoder.hex2text(text)

        embed = discord.Embed(color=0xfffff0, title="Decocded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
    
    @decode.command(name="ascii", aliases=['ascii2text', 'asciitotext'])
    async def ascii(self, ctx, *, text):
        output = dcoder.ascii2text(text)

        embed = discord.Embed(color=0xfffff0, title="Decocded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        raise error
        
def setup(client):
    client.add_cog(Decode(client))