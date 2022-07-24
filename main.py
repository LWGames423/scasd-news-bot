import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a robot")

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))
