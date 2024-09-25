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
        }
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
            padding_y=4, 
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
            padding_y=4, 
            group=True,
            )
        ],
}

# --------------------------------------------------------
# Widgets
# --------------------------------------------------------

# Groupboxes for the different screens
bar_groupbox_2 = widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    background="#033f67",
                                    padding=3,
                                    visible_groups=['4', '5', '6']
                                )

bar_groupbox_3 = widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    background="#033f67",
                                    padding=3,
                                    visible_groups=['7', '8', '9']
                                )

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
                    **decor,
                    ),
                widget.GroupBox(
                    font='sans',
                    fontsize=14,
                    padding=3,
                    visible_groups=['1', '2', '3'],
                    **decor,
                    ),
                widget.Clock(
                    font='Font Awesome',
                    foreground="#a37aed",
                    fontsize=18,
                    padding=3,
                    format="   %H:%M",
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
                                fontsize=16,
                                font='Font Awesome',
                                mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                                foreground="#a37aed",
                                interface="enp42s0",
                                format='  {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                                **decor
                            ),                    
                widget.Systray(
                    **decor_gr
                    ),
                widget.Volume(
                        foreground="#a37aed",
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

    # # Screen 2 FHD 27"
    # Screen(
    #     wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
    #     wallpaper_mode="fill",
    #     top=bar.Bar(
    #         [
                
    #         ],
    #         size=26,
    #     ),

    # ),

    # # Screen 3 FHD 24"
    # Screen(
    #     wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
    #     wallpaper_mode="fill",
    #     top=bar.Bar(
    #         [
                
    #         ],
    #         size=26,
    #     ),
    # ),

]