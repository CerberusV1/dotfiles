#!/bin/bash
#   ___ _____ ___ _     _____   ____  _             _    
#  / _ \_   _|_ _| |   | ____| / ___|| |_ __ _ _ __| |_  
# | | | || |  | || |   |  _|   \___ \| __/ _` | '__| __| 
# | |_| || |  | || |___| |___   ___) | || (_| | |  | |_  
#  \__\_\|_| |___|_____|_____| |____/ \__\__,_|_|   \__| 
#                                                        
#  
# ----------------------------------------------------- 

# -----------------------------------------------------
# Autostart Services
# -----------------------------------------------------

# Load picom
picom &

# Load notification service
dunst &

# Load polkit agent
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1

# Load power manager
# xfce4-power-manager &


# -----------------------------------------------------
# Autostart Apps
# -----------------------------------------------------

# Load flameshot
flameshot &

# Load bitwarden
bitwarden-desktop &

# Load discord
discord &

# Load firefox
firefox --new-instance &

# Load steam in systray
steam -silent &







