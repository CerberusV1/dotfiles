import json
import os

# Open path to pywal color scheme

with open(os.path.expanduser("~/.cache/wal/colors.json")) as f:
    wal_colors = json.load(f)
    
    
wp_colors = [
    wal_colors['colors']['color0'],  # Hintergrundfarbe
    wal_colors['colors']['color1'],  # Akzentfarbe 1
    wal_colors['colors']['color2'],  # Akzentfarbe 2
    wal_colors['colors']['color3'],  # usw.
    wal_colors['colors']['color4'],
    wal_colors['colors']['color5'],
    wal_colors['colors']['color6'],
    wal_colors['colors']['color7']
]