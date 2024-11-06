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

from libqtile import qtile
from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy

# --------------------------------------------------------------------
# Set default apps
# --------------------------------------------------------------------

terminal = "alacritty" 
browser = "firefox"
filemanager = "nemo"

# --------------------------------------------------------------------
# Keybindings
# --------------------------------------------------------------------

mod = "mod4" # SUPER KEY
alt = "mod1"
# KeybindStart
keys = [

    # KB_GROUP-Focus Window
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # KB_GROUP-Move Window
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "h", lazy.layout.swap_left(), desc="Move window to the left - Monad"),
    Key([mod, "shift"], "l", lazy.layout.swap_right(), desc="Move window to the left - Monad"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # KB_GROUP-Resize Window
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod], "m", lazy.layout.shrink(), desc="Grow window to the top"),
    Key([mod], "i", lazy.layout.grow(), desc="Grow window to the bottom"),

    # KB_GROUP-Window Controls
    Key([mod], "n", lazy.layout.normalize(), desc="Normalize all window sizes"),
    Key([mod, "shift"], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize window"),
    Key([mod, "shift"], "s", lazy.layout.toggle_auto_maximize(), desc="Toggle auto maximize"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle full screen"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip windows"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # KB_GROUP-System Controls
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # KB_GROUP-Audio and Media Control    
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="Mute Audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 2"), desc="Lower Volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 2"), desc="Next Song"),
    
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous Media"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play Pause Media"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next Media"),
        
    # KB_GROUP-Rofi Menus
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn Rofi D-Run"),
    Key([alt], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Spawn Windows"),
    Key([mod], "p", lazy.spawn("rofi -show ssh"), desc="Spawn Rofi SSH-Connections"),

    # KB_GROUP-ScratchPad
    Key(["control"], "1", lazy.group["scratchpad"].dropdown_toggle("term"), desc="Opens a PopUp Terminal"),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer'), desc="Opens pavucontrol"),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('files'), desc="Opens Nemo in a Scratchpad"),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('yt'), desc="Opens YTM in a Scratchpad"),
    Key([], "XF86Calculator", lazy.group['scratchpad'].dropdown_toggle('calc'), desc="Open Calculator in scratchpad"),

    # KB_GROUP-Programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "v", lazy.spawn("copyq toggle"), desc="Shows Clipboard"),
    Key([mod, "shift"], "q", lazy.spawn("flameshot gui"), desc="Screenshot selection"),
    Key([mod, "shift"], "b", lazy.spawn(browser), desc="Opens Browser on current screen"),
    Key([mod, "shift"], "p", lazy.spawn("firefox --private-window"), desc="Opens Private Browser on current screen"),
    Key([mod, "shift"], "e", lazy.spawn(filemanager), desc="Opens File Manager"),
    Key([mod], "b", lazy.spawn("bitwarden-desktop"), desc="Opens Bitwarden"),
    Key([mod, "control"], "a", lazy.spawn("python /home/cerberus/dotfiles/.config/qtile/helper/autoclicker.py"), desc="Autoclicker On"),
    Key([mod, "control"], "s", lazy.spawn("pkill -f autoclicker.py"), desc="Autoclicker Off"),
    
    Key([mod, "shift"], "i", lazy.spawn("alacritty --config-file=/home/cerberus/.config/alacritty/cheat-sheet.toml -T FloatWindow -e ./.config/qtile/helper/cheat-sheet.py"), desc="Opens Cheat-Sheet"),
    
    
]

# --------------------------------------------------------------------
# Drag floating layouts
# --------------------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# KeybindEnd
