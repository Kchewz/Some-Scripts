###!/bin/bash
##
##cd
##cd "/Users/Kchewz/desktop/github/kchewz.github.io"
##i=0
##for DAYS in $(seq 105 3705); do
##        COMMITS=$((1 + RANDOM % 20))
##        while [ $i -ne $COMMITS ]; do
##                echo " " >> readme.md
##                git add -A
##                git commit --date="$DAYS day ago" -m "Update README.md"
##                git push
##                i=$((i+1))
##        done
##        i=0
##        echo "-----------------------Did day $DAYS-----------------------"
##done

import os
import random
#from git import Repo
import subprocess

os.chdir("/Users/Kchewz/desktop/github/quest-of-the-ages")
commits = random.randint(1,21)
#repo = Repo("/Users/Kchewz/desktop/github/quest-of-the-ages")
#index = Repo.init(path).index

while commits != 0:
    print("------------ " + str(commits) +" COMMITS LEFT------------")
    file = open("QoA_help.txt", "a")
    file.write(" ")
    file.close()
    subprocess.call(["git", "add", "-A"])
    subprocess.call(["git", "commit", "-m", "Update QoA_help.txt"])
    subprocess.call(["git", "push"])
    #repo.add(file)
    #origin.add("git add -A")
    #origin.commit("Update QoA_help.txt")
    #origin.push()
    commits-=1
