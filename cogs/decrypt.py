import discord
from discord.ext import commands
import dcoder

class Decrypt(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="decrypt")
    async def decrypt(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Will do it later LOL")
            await ctx.send(embed=embed)

    @decrypt.command(name="railfence", aliases=['railfence2text', 'railfencetotext'])
    async def railfence(self, ctx, *, text):
        output = dcoder.railfence2text(text)

        embed = discord.Embed(color=0xfffff0, title="Decrypted..")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)

    @decrypt.command(name="caesar", aliases=['caesar2text', 'caesartotext'])
    async def caesar(self, ctx, *, text):
        output = dcoder.caesar2text(text)

        embed = discord.Embed(color=0xfffff0, title="Decrypted..")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Decrypt(client))