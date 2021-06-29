import os
script_reg_number = input("Reg_ID: ")
command_for_remote_shell = input("Command For Remote Shell:|")

with open(script_reg_number, "w") as commands:
    commands.write(command_for_remote_shell)
    commands.close()
command_for_moving_command_file_to_order_folder = f"move {script_reg_number} order"
os.system(command_for_moving_command_file_to_order_folder)
