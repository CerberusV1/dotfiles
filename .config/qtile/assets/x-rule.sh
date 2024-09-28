#!/bin/bash

xprop | grep -e "WM_CLASS" -e "WM_NAME" -e "WM_SIZE"| awk -F' = ' '{
    if ($1 ~ /WM_CLASS/) {
        printf "WM_CLASS: %s\n", $2
    } else if ($1 ~ /WM_NAME/) {
        printf "WM_NAME: %s\n", $2
    } else if ($1 ~ /WM_SIZE/) {
        printf "WM_Size: %s\n", $3
    }
}' | sed 's/\"//g'
read -p "Press [Enter] to exit..."