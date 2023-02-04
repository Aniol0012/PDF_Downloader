#!/bin/bash

# Author: Aniol0012
# Date: Feburary 2023

links=(
    "https://www.example.com/test_1.pdf"
    "https://www.example.com/test_2.pdf"
    "https://www.example.com/test_3.pdf"
    "https://www.example.com/test_4.pdf"
    "https://www.example.com/test_5.pdf"
    "https://www.example.com/test_6.pdf"
    "https://www.example.com/test_7.pdf"
)

if [[ $1 == "-r" ]]; then
    rm -rf *.pdf
    echo "All pdf files removed"
    ls
else
    echo "Printing all links..."

    for link in ${links[@]}; do
        curl -O $link >/dev/null 2>&1
    done

    echo "Done"
fi