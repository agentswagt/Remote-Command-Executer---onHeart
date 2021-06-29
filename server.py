import os
import sys

#reg_number
script_reg_number = sys.argv[1]
script_reg_number = str(script_reg_number)
#one_time_code
one_time_code = sys.argv[2]
one_time_code = str(one_time_code)
#command
command_for_remote_shell = sys.argv[3]
command_for_remote_shell = str(command_for_remote_shell)

command_for_moving_command_file_to_order_folder = f"move {script_reg_number} order"


with open(script_reg_number, "w") as commands:
    commands.write(one_time_code + command_for_remote_shell)
    commands.close()

os.system(command_for_moving_command_file_to_order_folder)

print(script_reg_number, command_for_remote_shell, one_time_code)