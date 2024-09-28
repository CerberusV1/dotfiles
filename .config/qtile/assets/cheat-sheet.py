#!/usr/bin/env python3
import re
from pathlib import Path

# Define the file path using Path and expand user directory
file_path = Path("~/dotfiles/.config/qtile/keys.py").expanduser()

# Initialize a flag for header printing
header_printed = False

def capitalize_first_letter(s):
    """Capitalize the first letter of each key."""
    return s.capitalize() if s else ""

def replace_keys(key):
    """Replace Mod and Control with Super and Ctrl."""
    if key == "mod":
        return "Super"
    elif key == "control":
        return "Ctrl"
    return key

with open(file_path, 'r') as file:
    for line in file:
        # Skip lines that contain "# Key("
        if '# Key(' in line:
            continue
        
        # Check for KB_GROUP headers
        if '# KB_GROUP-' in line:
            if header_printed:
                print("")  # Add a blank line before the next header
            # Print the header in bold yellow, removing "KB_GROUP-"
            print(f"\n\033[1;33m{line.strip().replace('KB_GROUP-', '').strip()}\033[0m\n")
            header_printed = True

        # Check for Key bindings
        match = re.search(r'Key\(\[(.*?)\], "(.*?)", lazy\..*, desc="(.*)"\)', line)
        if match:
            # Get the modifier keys
            keys = match.group(1).replace("'", "").replace('"', '').split(', ')
            # Get the main key
            key = match.group(2)  
            # Get the description
            description = match.group(3)

            # Prepare the key strings for each key position
            mod1 = capitalize_first_letter(replace_keys(keys[0])) if len(keys) > 0 else ""
            mod2 = capitalize_first_letter(replace_keys(keys[1])) if len(keys) > 1 else ""
            key_str = capitalize_first_letter(key)  # The main key
            
            # Print the keys in their respective columns
            print(f" {mod1:<6} {mod2:<8} {key_str:<30}{description}")

# Wait for user input before exiting
input("Press [Enter] to exit...")


