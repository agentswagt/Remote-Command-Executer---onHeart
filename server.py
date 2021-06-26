
script_reg_number = input("Reg_ID: ")
command_for_remote_shell = input("Command For Remote Shell:|")
with open(script_reg_number, "w") as commands:
    commands.write(command_for_remote_shell)
    commands.close()
