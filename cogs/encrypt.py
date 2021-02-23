import discord
from discord.ext import commands
import dcoder

class Encrypt(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="encrypt")
    async def encrypt(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Will do it later LOL")
            await ctx.send(embed=embed)

    @encrypt.command(name="railfence", aliases=['etxt2railfence', 'texttorailfence'])
    async def railfence(self, ctx, *, text):
        output = dcoder.railfence2text(text)

        embed = discord.Embed(color=0xfffff0, title="Encrypted..")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)

    @encrypt.command(name="caesar", aliases=['text2caesar', 'texttocaesar'])
    async def caesar(self, ctx, *, text):
        output = dcoder.caesar2text(text)

        embed = discord.Embed(color=0xfffff0, title="Encrypted..")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Encrypt(client))