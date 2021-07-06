


import sys
import os
command_code = sys.argv[1]
command = sys.argv[2]
script_id = sys.argv[3]

print(command_code)
print(command)
print(script_id)

if script_id == "" or command == "" or command_code == "":
    import sys
    print("Command Formation")
    print("Example:\npython server.py [command_code] [command] [script_id]")
    sys.exit()



#writing the payload file

the_command_line = f"{command_code}{command}"

writer = open(script_id, "w")
writer.write(the_command_line)
writer.close()

#Moving file to order folder

os.system(f"move {script_id} order")


os.system("python pusher.py")