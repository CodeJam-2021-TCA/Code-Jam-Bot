import discord
from discord.ext import commands
import dcoder

class Encode(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("OH ok, i am here")
    
    @commands.group(name="encode")
    async def encode(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Will do it later LOL")
            await ctx.send(embed=embed)  
    
    @encode.command(name="binary", aliases=['text2binary', 'texttobinary'])
    async def binary(self, ctx, *, text):
        output = dcoder.text2bin(text)

        embed = discord.Embed(color=0xfffff0, title="Encoded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
        
    @encode.command(name="octal", aliases=["text2octal", 'texttooctal'])
    async def octal(self, ctx, *, text):
        output = dcoder.text2oct(text)

        embed = discord.Embed(color=0xfffff0, title="Encoded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
    
    @encode.command(name="hex", aliases=['text2hex', 'texttohex'])
    async def hexadecimal(self, ctx, *, text):
        output = dcoder.text2hex(text)

        embed = discord.Embed(color=0xfffff0, title="Encoded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
    
    @encode.command(name="ascii", aliases=['text2ascii', 'texttoascii'])
    async def ascii(self, ctx, *, text):
        output = dcoder.text2ascii(text)

        embed = discord.Embed(color=0xfffff0, title="Encoded.")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        raise error
        
def setup(client):
    client.add_cog(Encode(client))