import discord
from discord.ext import commands
import asyncio
import sqlite3
import os

class Compete(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="race")
    async def race(self, ctx, difficulty=None):

        if difficulty is None:
            return await ctx.send("Choose a difficulty from the following list `easy|medium|hard`")

        import json
        import random
        import time

        with open("cogs/raceAndCompete.json", "r") as f:
            data = json.load(f)

        mode = data.get(difficulty)

        if mode is None:
            return await ctx.send("Not a valid difficulty choose one from the following list `easy|medium|hard`")

        await ctx.send("""Hello there User 👋🏻,
It is me, Cryptographer, it seems like you wanna compete ( Test Yourself ), You will be given 5 minutes to decode the following text
After you have Solved it You are supposed to DM me ( You NEED TO have your DMs Open in order to do this. ).
Feel free to send `Yes` or `Y` in the chat within a minute if you wanna compete.
""")

        try:
            message = await self.client.wait_for('message', timeout= 60, check=lambda message: message.author==ctx.author)
        except asyncio.TimeoutError:
            return await ctx.send("Request timed out.")
        
        if message.content.lower() not in ["y", "yes"]:
            return
        
        stuff = random.choice(mode)
        await ctx.send(f"Decode the following ```{stuff['key']}```")

        start_time = time.time()

        try:
            answer = await self.client.wait_for('message', timeout=300.0, check=lambda message: message.author.id == ctx.author.id and isinstance(message.channel, discord.DMChannel) and message.content.lower() == stuff["finalAnswer"])
        except asyncio.TimeoutError:
            return await ctx.send(f"{ctx.author.mention}, didn't answer in enough time, no points were given.")

        end_time = time.time()
        total_time = int(end_time - start_time)

        await ctx.send(f"CONGRATS! {ctx.author.mention} You have been awarded 1 or 2 points depending on the difficulty ( hard mode is 2 and the remaing are 1 ).")

        conn = sqlite3.connect('./data/competeWins.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM wins WHERE UserID = ?", (ctx.author.id, ))
        something = cursor.fetchone()

        sql, val = "", ""
        if something is None:
            sql = "INSERT INTO wins (UserID, Wins, TimeTaken) VALUES (?, ?, ?)"
            val = (ctx.author.id, (2 if difficulty.lower() == "hard" else 1), total_time)
            print(val)
        else:
            sql = "UPDATE wins SET (wins, timetaken) = (?, ?) WHERE UserId = ?"
            current_wins = something[1]
            val = ((current_wins + (2 if difficulty.lower() == "hard" else 1)), total_time, ctx.author.id)

        cursor.execute(sql, val)

        conn.commit()
        cursor.close()
        conn.close()


def setup(client):
    client.add_cog(Compete(client))
