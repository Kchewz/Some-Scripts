import os
import random
#from git import Repo
import subprocess

os.chdir("/Users/Kchewz/desktop/github/quest-of-the-ages")
commits = random.randint(1,21)

while commits != 0:
    print("------------ " + str(commits) +" COMMITS LEFT------------")
    file = open("QoA_help.txt", "a")
    file.write(" ")
    file.close()
    subprocess.call(["git", "add", "-A"])
    subprocess.call(["git", "commit", "-m", "Update QoA_help.txt"])
    subprocess.call(["git", "push"])
    commits-=1
