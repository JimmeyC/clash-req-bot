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
    if messagetype == 0:
        type = "Message: "
    
    elif messagetype == 1:
        type = "Command:  "
    
    elif messagetype == 2:
        type = "Running: "
    
    elif messagetype == 3:
        type = "Warning: "
    
    elif messagetype == 4:
        type = "Error: "
    
    elif messagetype == 5:
        type = "Failure: "
    
    else:
        type = 'Other: '

    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%d/%m/%Y %H:%M:%S.%f")
    current_time = "["+current_time + "] "
    try:
        lm = open(f"./logs/log-{current_date}.txt", "x")
        lm.write(f"Start of log-{current_date} | Created at {current_time}\n")
        lm.close()
    except FileExistsError:
        test = 0    

    f = open(f"./logs/log-{current_date}.txt", "a")
    f.write(current_time + type + message + "\n")
    f.close()


