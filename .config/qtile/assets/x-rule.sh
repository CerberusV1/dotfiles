#!/bin/bash

xprop | grep -e "WM_CLASS" -e "WM_NAME" | awk -F' = ' '{
    if ($1 ~ /WM_CLASS/) {
        printf "WM_CLASS: %s\n", $2
    } else if ($1 ~ /WM_NAME/) {
        printf "WM_NAME: %s\n", $2
    }
}' | sed 's/\"//g'
read -p "Press [Enter] to exit..."