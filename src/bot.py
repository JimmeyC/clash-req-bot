
from click import command
import discord
from src import log, clashexecute
import os 
from dotenv import load_dotenv
from discord.ext import commands


    

#log types
    # 0 = Message
    # 1 = Command
    # 2 = Running
    # 3 = Success
    # 4 = Warning
    # 5 = Error
    # 6 = Failure
    # 7 = Break- When the program ends it will put a line break in to show where it restarted if there was an issue 
    # 8 = Break- When the program Starts it will put a line break in to show where it restarted if there was an issue 
    # 9+ = Other

try:
    f = open("token.txt","r")
    token = f.readline()
    if token == "INSERT_TOKEN":
        print("Please put your token into token.txt and start the program again!")
        log.log(5, "Missing token")
        log.log(4, "Stopping")
        log.log(7)
        exit()
    TOKEN = token
    intents = discord.Intents.all()
    intents.dm_messages = True
    log.log(3, "Enabled Intents")

    bot = commands.Bot(command_prefix='!', intents = intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is online and functional")
        log.log(3, "Client has started")

    @bot.listen()
    async def on_member_join(member):
        await member.send("Hello and welcome to the ***Black Dragons*** CoC Automatic donation server.")
        log.log(3, f"Sent message to {member}")
        await member.send("Please make sure you're in the clan as this will not work.")
        log.log(3, f"Sent message to {member}")
        await member.send("Thanks bbg")
        log.log(3, f"Sent message to {member}")

    @bot.command()
    async def request(troopset,spell, ctx,):
        log.log(1,f"Requesting {troopset}, {spell} from {ctx.author}")
        await ctx.send("Balls itch")




    log.log(2, "Starting client")
    bot.run(TOKEN)
except ModuleNotFoundError:
    log.log(5, "Module [clahsexecute] was not found")
    log.log(6, "User attempted to start bot.py")
    log.log(0, "Make sure to start the program from init.py!")
    log.log(7)
    exit()