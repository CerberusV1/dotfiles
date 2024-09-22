#        _   _ _        _                  
#   __ _| |_(_) | ___  | | _____ _   _ ___ 
#  / _` | __| | |/ _ \ | |/ / _ \ | | / __|
# | (_| | |_| | |  __/ |   <  __/ |_| \__ \
#  \__, |\__|_|_|\___| |_|\_\___|\__, |___/
#     |_|                        |___/     
# by cerberus
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------
from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy

# --------------------------------------------------------------------
# Set default apps
# --------------------------------------------------------------------

terminal = "alacritty"   

# --------------------------------------------------------------------
# Keybindings
# --------------------------------------------------------------------

mod = "mod4" # SUPER KEY
alt = "mod1"

keys = [

    # Focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window around"),
    # ________________________________________________________


    # Move
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # ________________________________________________________


    # Size
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Up", lazy.layout.shrink(), desc="Grow window to the top"),
    Key([mod, "control"], "Down", lazy.layout.grow(), desc="Grow window to the bottom"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # ________________________________________________________


    # Floating
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
    # ________________________________________________________


    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # ________________________________________________________


    # Split
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # ________________________________________________________


    # System
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # ________________________________________________________


    # Programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn Rofi"),
    Key([alt], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Spawn Rofi"),
    # Key([mod], "p", lazy.spawn("rofi -show ssh"), desc="Spawn Rofi"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Screenshot selection"),
    # ________________________________________________________
    
]

# --------------------------------------------------------------------
# Drag floating layouts
# --------------------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
