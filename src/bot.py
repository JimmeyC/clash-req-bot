import discord
from src import log
import os 
from dotenv import load_dotenv

#log types
    # 0 = Message
    # 1 = Command
    # 2 = Running
    # 3 = Success
    # 4 = Warning
    # 5 = Error
    # 6 = Failure 
    # 7+ = Other


f = open("token.txt","r")
token = f.readline()
if token == "INSERT_TOKEN":
    print("Please put your token into token.txt and start the program again!")
    log.log(5, "Missing token")
    log.log(4, "Stopping")
    exit()
load_dotenv()

