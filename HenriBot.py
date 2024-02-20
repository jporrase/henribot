import discord
from discord.ext import commands
import random
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("The HenriBot is ready for use!")
    print("------------------------------")

@client.command(help="Says Hello")
async def hello(ctx):
    await ctx.send("Hello, I am HenriBot")

@client.command(help="Generates a number from 0 to 100")
async def randomnumber(ctx):
    await ctx.send(random.randint(0, 100))

@client.command(help="Flips a coin.")
async def flip(ctx):
    outcome = "Heads" if random.choice([True, False]) else "Tails"
    await ctx.send(f"🪙 Coin flip result: {outcome}")

@client.command(help="Rolls a dice with a specified number of sides.")
async def roll(ctx, sides: int = 6):
    number = random.randint(1, sides)
    await ctx.send(f"🎲 Rolled a {sides}-sided dice and got {number}!")

@client.command(help="Displays information about the server.")
async def serverinfo(ctx):
    server = ctx.guild
    num_members = server.member_count
    server_name = server.name
    description = server.description
    await ctx.send(f"Server Name: {server_name}\nMembers: {num_members}\nDescription: {description or 'No description'}")




client.run('MTE4OTk5OTA4NTgxNDU2NzA0Mw.G0xvV-.zrdxIeFisMu_SpiwmzjbDK7Mk5P7VyTM8hgqkw')

