#!/usr/bin/env bash

uptime=$(uptime -p | sed -e 's/up //g')
dir="~/.config/rofi/"
rofi_command="rofi -theme $dir/power.rasi"

# Options
terminal=""
shutdown="󰐥"
reboot="󰜉"
suspend="󰒲"


options="$terminal\n$suspend\n$reboot\n$shutdown"

chosen="$(echo -e "$options" | $rofi_command -p "Uptime: $uptime" -dmenu -selected-row 0)"
case $chosen in
    $shutdown)
        systemctl poweroff
        ;;
    $reboot)
        systemctl reboot
        ;;
    $suspend)
        systemctl suspend
        ;;
    $terminal)
        alacritty
        ;;
esac
