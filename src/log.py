from datetime import datetime
from os import mkdir

try:
    mkdir("./logs")
except FileExistsError:
    test = 0
try:
    mkdir("./temp")
except FileExistsError:
    test = 0

def log(messagetype, message = ""):
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


    if messagetype == 0:
        type = "Message: "
    
    elif messagetype == 1:
        type = "Command:  "
    
    elif messagetype == 2:
        type = "Running: "
    
    elif messagetype == 3:
        type = "Success: "
    
    elif messagetype == 4:
        type = "Warning: "
    
    elif messagetype == 5:
        type = "Error: "
    
    elif messagetype == 6:
        type = "Failure: "
    
    elif messagetype == 7:
        type = "Stopped"
    
    elif messagetype == 8:
        type = "Started"
    
    else:
        type = 'Other: '

    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%d/%m/%Y %H:%M:%S.%f")
    current_timee = "["+current_time + "] "
    try:
        lm = open(f"./logs/log-{current_date}.txt", "x")
        lm.write(f"Start of log-{current_date} | Created at {current_timee}\n")
        lm.close()
    except FileExistsError:
        test = 0    

    f = open(f"./logs/log-{current_date}.txt", "a")
    if messagetype == 7:
        f.write("--------------------------------[Server Stopped At: "+ current_time +"]-------------------------------------------\n\n")
    elif messagetype == 8:
        f.write("--------------------------------[Server Started At: "+ current_time +"]-------------------------------------------\n")
    else:
        f.write(current_timee + type + message + "\n")
    f.close()


