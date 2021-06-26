
import os

pusher_ID = "1213123"

os.system("git add .")
os.system(f"git commit -m \"commited by pusher {pusher_ID}\"")
os.system("git push -u origin master")