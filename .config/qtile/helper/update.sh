#!/bin/bash

# System Update
figlet -m-2 "Updating System..."
sudo pacman -Syu 

# Confirmation for system update
read -p "Do you want to proceed with the system update? (y/n): " -n 1 -r
echo    # New line
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo pacman -Syu --noconfirm
else
    echo "System update canceled."
    exit 1
fi

# Update AUR Packages (optional)
figlet "Updating AUR Packages..."
if command -v yay &> /dev/null; then
    echo "Available AUR updates:"
    yay -Syu

    # Confirmation for AUR update
    read -p "Do you want to proceed with the AUR update? (y/n): " -n 1 -r
    echo    # New line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        yay -Syu --noconfirm
    else
        echo "AUR update canceled."
    fi
fi

# Update Flatpak Packages
figlet "Updating Flatpaks..."
if command -v flatpak &> /dev/null; then
    flatpak update --assumeyes 

    # Confirmation for Flatpak update
    read -p "Do you want to proceed with the Flatpak update? (y/n): " -n 1 -r
    echo    # New line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        flatpak update -y
    else
        echo "Flatpak update canceled."
    fi
else
    echo "Flatpak is not installed."
fi

figlet "Update done."
read -p "  Press [Enter] to exit..."
