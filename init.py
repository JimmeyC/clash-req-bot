#check packages
try:
    import discord
    import pyautogui
    print("Successfully import discord & PyAutoGUI")
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "pip", "install", "discord"])
    subprocess.check_call([sys.executable, "pip", "install", "pyautogui"])
    print("Please run the program again!")
    exit()

