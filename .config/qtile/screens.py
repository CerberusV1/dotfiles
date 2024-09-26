#        _   _ _                                         
#   __ _| |_(_) | ___   ___  ___ _ __ ___  ___ _ __  ___ 
#  / _` | __| | |/ _ \ / __|/ __| '__/ _ \/ _ \ '_ \/ __|
# | (_| | |_| | |  __/ \__ \ (__| | |  __/  __/ | | \__ \
#  \__, |\__|_|_|\___| |___/\___|_|  \___|\___|_| |_|___/
#     |_|                                                
# by cerberus
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------

from libqtile.config import Screen
from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

import os.path

# --------------------------------------------------------
# colors
# --------------------------------------------------------

colors = {
    "background":{
        "bg1": "#3e4241",
        "bg2": "#464f51",
        }, 
    "highlight": {
        "o1": "#df7326",
        "o2": "#e75a1d"
        },
    "black": "#000000",
    "white": "#ffffff"
    }

# background=colors["background"]["bg1"],

# --------------------------------------------------------
# Decorations
# --------------------------------------------------------

decor = {
    "decorations": [
        RectDecoration(
            colour=colors["highlight"]["o1"], 
            radius=10, 
            filled=True, 
            padding=3, 
            extrawidth=10,
            group=False,
            )
        ],
}

decor_gr = {
    "decorations": [
        RectDecoration(
            colour=colors["highlight"]["o2"], 
            radius=10, 
            filled=True, 
            extrawidth=10, 
            padding=3, 
            group=True,
            )
        ],
}

# --------------------------------------------------------
# Screens
# --------------------------------------------------------


screens = [

    # Screen 1 WQHD 27"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Image(
                    filename='~/Pictures/icons/arch/arch_linux_icon_132588.png',
                    scale=True,
                    adjust_x=5,
                    **decor,
                    ),
                widget.Spacer(length=1,**decor_gr),
                widget.GroupBox(
                    font='sans',
                    fontsize=25,
                    padding=3,
                    visible_groups=['1', '2', '3'],
                    highlight_method='text',
                    urgent_alert_method="text",
                    **decor_gr,
                    ),
                widget.Spacer(length=1),
                widget.Clock(
                    font='Font Awesome',
                    foreground=colors["white"],
                    fontsize=18,
                    padding=3,
                    format="    %H:%M",
                    **decor_gr                         
                    ),
                widget.Wttr(
                                font='sans',
                                fontsize=16,
                                format='%c %t',
                                **decor_gr
                    ),
                widget.Spacer(),
                widget.Net(
                                fontsize=20,
                                font='Font Awesome',
                                mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                                foreground=colors["white"],
                                interface="enp42s0",
                                format='   {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                                prefix='M',
                                **decor
                            ),
                                    
                widget.Systray(
                    icon_size=23,
                    ),
                widget.Volume(
                        foreground=colors["white"],
                        fontsize=20,
                        font='Font Awesome',
                        cannel='Master',
                        fmt='  ',
                        mouse_callbacks={"Button1": lazy.spawn("pavucontrol-qt")},
                        **decor_gr
                    ),
                widget.CheckUpdates(
                            distro='Arch_checkupdates',
                            colour_have_updates="#ff0000",
                            colour_no_updates="#00ff00",
                            no_update_string='  0',
                            font='Font Awesome',
                            fontsize=18,
                            display_format='  {updates}',
                            **decor_gr
                            ),
            ],
            background="00000000",
            size=35,
        ),
    ),

    # Screen 2 FHD 27"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(length=1,**decor_gr),
                widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    padding=5,
                                    margin_x=5,
                                    visible_groups=['4', '5', '6'],
                                    highlight_method='text',
                                    **decor_gr
                                ),
                widget.Spacer(),
                widget.Clock(
                    font='Font Awesome',
                    foreground=colors["white"],
                    fontsize=18,
                    padding=3,
                    format="   %H:%M",
                    **decor_gr                         
                    ),                
            ],
            background="00000000",
            size=28,
        ),

    ),

    # Screen 3 FHD 24"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(length=1,**decor_gr),
                widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    padding=3,
                                    visible_groups=['7', '8', '9'],
                                    highlight_method='text',
                                    **decor_gr
                                ),
                widget.Spacer(),
                widget.Clock(
                    font='Font Awesome',
                    foreground=colors["white"],
                    fontsize=18,
                    padding=2,
                    format="    %H:%M",
                    **decor_gr                         
                    ),                
            ],
            background="00000000",
            size=26,
        ),
    ),

]