import discord
from discord.ext import commands
import dcoder

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="atbash")
    async def atbash(self, ctx, *, text):
        output = dcoder.atbash2text(text)

        embed = discord.Embed(color=0xfffff0, title="Atbash")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)
    
    @commands.command(name="reverse", aliases=['flip'])
    async def reverse(self, ctx, *, text):
        output = dcoder.reverse(text)

        embed = discord.Embed(color=0xfffff0, title="Text-Reverse")
        embed.set_author(name=f"{ctx.author}", icon_url=(ctx.author.avatar_url or ctx.author.default_avatar_url))
        embed.add_field(name="Input: ", value=text, inline=False)
        embed.add_field(name="Output: ", value=output)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(General(client))