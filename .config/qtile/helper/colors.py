import json
import os

# Open path to pywal color scheme

with open(os.path.expanduser("~/.cache/wal/colors.json")) as f:
    wal_colors = json.load(f)
    
    
wp_colors = [
    wal_colors['colors']['color0'],  # Black
    wal_colors['colors']['color1'],  # Accent 1
    wal_colors['colors']['color2'],  # Accent 2
    wal_colors['colors']['color3'],  # Mask Color
    wal_colors['colors']['color4'],  # Window Border,
    wal_colors['colors']['color5'],  # Warn Color
    wal_colors['colors']['color6'],  # ------
    wal_colors['colors']['color7'],  # Text Color
    wal_colors['colors']['color8'],  # Dunkle Hintergrundfarbe
    wal_colors['colors']['color9'],  # Helle Fehlerfarbe
    wal_colors['colors']['color10'], # Helle Akzentfarbe 1
    wal_colors['colors']['color11'], # Helle Akzentfarbe 2
    wal_colors['colors']['color12'], # Helle Warnfarbe
    wal_colors['colors']['color13'], # Helle Sekundärfarbe
    wal_colors['colors']['color14'], # Helle Hilfsfarbe
    wal_colors['colors']['color15'], # Helle Textfarbe
]