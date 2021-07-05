import subprocess
import time
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#si.wShowWindow = subprocess.SW_HIDE # default

time.sleep(5)

subprocess.call("del client.py", startupinfo=si)