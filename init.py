#check packages
from os import mkdir
from src import log

#log types
    # 0 = Message
    # 1 = Command
    # 2 = Running
    # 3 = Success
    # 4 = Warning
    # 5 = Error
    # 6 = Failure 
    # 7+ = Other


print(" █████╗ ██╗   ██╗████████╗ ██████╗      ██████╗ ██████╗  ██████╗    ██████╗  ██████╗ ███╗   ██╗ █████╗ ████████╗███████╗██████╗ ")
print("██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔════╝██╔═══██╗██╔════╝    ██╔══██╗██╔═══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗")
print("███████║██║   ██║   ██║   ██║   ██║    ██║     ██║   ██║██║         ██║  ██║██║   ██║██╔██╗ ██║███████║   ██║   █████╗  ██████╔╝")
print("██╔══██║██║   ██║   ██║   ██║   ██║    ██║     ██║   ██║██║         ██║  ██║██║   ██║██║╚██╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗")
print("██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ╚██████╗╚██████╔╝╚██████╗    ██████╔╝╚██████╔╝██║ ╚████║██║  ██║   ██║   ███████╗██║  ██║")
print("╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝      ╚═════╝ ╚═════╝  ╚═════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
print("Made with love by JimmeyC on github <3")


try:
    import discord
    log.log(3, "Discord.py is installed")
    import pyautogui
    log.log(3, "pyautogui is installed")
    print("Successfully imported discord & PyAutoGUI")

except ModuleNotFoundError:
    log.log(5, "Discord.py and pyautogui are not installed")
    import subprocess
    import sys
    log.log(2, "Installing discord.py")
    subprocess.check_call([sys.executable, "pip", "install", "discord"])
    log.log(3, "Installed discord.py")
    log.log(2, "Installing pyautogui")
    subprocess.check_call([sys.executable, "pip", "install", "pyautogui"])
    log.log(3, "Installed pyautogui")
    

    print("Please run the program again!")
    log.log(4, "Stopping")
    exit()

try:
    b = open("token.txt",'x')
    log.log(3, "Created token file")
    b.write('INSERT_TOKEN')
    b.close()
except FileExistsError:
    log.log(5, "token.txt exists")
from src import bot
