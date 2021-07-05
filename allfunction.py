import sys



import subprocess


def comexesilent(command):
    import subprocess
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    #si.wShowWindow = subprocess.SW_HIDE # default
    subprocess.call(command, startupinfo=si)


def repeatchecker(command_number_online):
    last_code = open("last_code", "r").readline()
    print(last_code)
    new_code = command_number_online
    print(new_code)
    if last_code == str(new_code):
        return True
    
    if str(new_code) == " ":
        return True
    else:
        return False



