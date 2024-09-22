#!/bin/bash
#   ___ _____ ___ _     _____   ____  _             _    
#  / _ \_   _|_ _| |   | ____| / ___|| |_ __ _ _ __| |_  
# | | | || |  | || |   |  _|   \___ \| __/ _` | '__| __| 
# | |_| || |  | || |___| |___   ___) | || (_| | |  | |_  
#  \__\_\|_| |___|_____|_____| |____/ \__\__,_|_|   \__| 
#                                                        
# by cerberus 
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

# Start flameshot
flameshot &

# Start bitwarden in systray
bitwarden-desktop &

# Load discord
discord &

# Start steam in systray
steam -silent &

# Start YTM
youtube-music &






