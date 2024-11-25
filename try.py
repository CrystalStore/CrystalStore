import discord
from discord.ext import commands

# Define bot prefix and initialize the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def calculate_price(rate, robux):
    price = (robux / 1000) * rate
    return round(price, 2)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Command for USD-based calculation
@bot.command(name="$")
async def price_calculator_usd(ctx, rate: float, robux: int):
    try:
        price = calculate_price(rate, robux)
        await ctx.send(f"The price for {robux} Robux at ${rate}/1k is: **${price}**")
    except Exception as e:
        await ctx.send("An error occurred. Please use the format: `!$ <rate> <amount>`")

# Command for PHP-based calculation
@bot.command(name="php")
async def price_calculator_php(ctx, rate: float, robux: int):
    try:
        price = calculate_price(rate, robux)
        await ctx.send(f"The price for {robux} Robux at ₱{rate}/1k is: **₱{price}**")
    except Exception as e:
        await ctx.send("An error occurred. Please use the format: `!php <rate> <amount>`")

# Run the bot

TOKEN = 'MTMwMjkxNjk4NTQxMTIxMTI3NQ.GiGT6L.t_KqvZHp-PBalUU2ObZYpYX1qCGd-7rO-O6Q1o'
bot.run(TOKEN)
