#!/bin/bash

# Use: start script -> select wp -> close nitrogen
# Attention: short delay caused by Qtile reload

# Opens Nitrogen to select the wallpaper
nitrogen

# Get path of set wallpaper from first monitor which provides the color scheme
WALLPAPER=$(grep -oP '(?<=file=).*' ~/.config/nitrogen/bg-saved.cfg | head -n 1)

# Check if path exists
if [ -f "$WALLPAPER" ]; then
    wal --backend haishoku -i "$WALLPAPER" -n  #--saturate 0.7
    wal -R -n
else
    echo "Couldnt find valid image"
fi

# Restart Qtile to apply colors
qtile cmd-obj -o cmd -f restart

# Update Firefox-Theme
pywalfox update
