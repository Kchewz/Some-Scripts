#!/bin/bash

cd
cd "/Users/Kchewz/desktop/github/kchewz.github.io"
i=0
for DAYS in $(seq 2032 3705); do
        COMMITS=$((1 + RANDOM % 1))
        while [ $i -ne $COMMITS ]; do
                echo " " >> README.md
                git add -A
                git commit --date="$DAYS day ago" -m "Update README.md"
                git push
                i=$((i+1))
        done
        i=0
        echo "-----------------------Did day $DAYS-----------------------"
done

