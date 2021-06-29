#Remote Code Upadater
import os
import sys 
import requests
import subprocess
import time

script_id_number = 444
new_command_url = f"https://rcu-d.netlify.app/order/{script_id_number}"
new_command = requests.get(new_command_url).text
print(new_command)


shagato = sys.argv[1]
print(shagato)