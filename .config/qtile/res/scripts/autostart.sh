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
# Essentials
# -----------------------------------------------------
# Load polkit agent
gnome-keyring-daemon --start --components=pkcs11,secrets,ssh &
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &

# -----------------------------------------------------
# Configure Screens
# -----------------------------------------------------
"$HOME"/.screenlayout/screens.sh &

# -----------------------------------------------------
# Autostart Applications
# -----------------------------------------------------
picom &              # Compositor
nitrogen --restore & # Wallpaper Manager
copyq &              # Clipboard Manager
flameshot &          # Screenshot Tool
discord &            # Discord
steam -silent &      # Steam
firefox &            # Firefox
youtube-music &      # YT-Music
bitwarden-desktop &  # Bitwarden Passwordmanager
joplin &             # Note Taking
rnote &              # Hand-Written Notes
"$HOME"/Documents/scripts/wacom_screen_config.sh &
librewolf &
