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
from qtile_extras.widget.decorations import PowerLineDecoration

import os.path


# --------------------------------------------------------
# Decorations
# --------------------------------------------------------

decR = {
    "decorations": [
        PowerLineDecoration(
                                path="forward_slash"
                            )
    ],
    "padding": 5,
}

decL = {
    "decorations": [
        PowerLineDecoration(
                                path="back_slash"
                            )
    ],
    "padding": 5,
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

# Keychord Widget to display the keychords in the top bar
bar_keychord = widget.Chord(
                                font='sans',
                                fontsize=14,
                                padding=3,
                                chords_colors={"launch": ("#ff0000", "#ffffff"),},
                                name_transform=lambda name: name.upper(),
                            )

# Clock Widget
bar_clockFHD = widget.Clock(
                                font='sans',
                                fontsize=14,
                                background="#033f67",
                                padding=3,
                                format="%d.%m.%y %H:%M",                       
                            )

# Spacer (flexible)
bar_spacer = widget.Spacer(
                                background="#101533",
                            )

# Spacer (fixed)
bar_spacerFixed = widget.Spacer(
                                background="#033f67",
                                length=10
                            )
# Spacer (fixed)
bar_spacerFixedWQHD = widget.Spacer(
                                background="#033f67",
                                length=10,
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
                widget.Spacer(
                                background="#033f67",
                                length=20,
                                **decL
                            ),
                widget.Wttr(
                                background="#05606b",
                                font='sans',
                                fontsize=16,
                                format='%c %t',
                                **decL
                            ),
                widget.Net(
                                background="#033f67",
                                fontsize=16,
                                font='Font Awesome',
                                mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                                foreground="#a37aed",
                                interface="enp42s0",
                                format='  {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                                **decL
                            ),
                widget.Spacer(
                                background="#101533",
                                **decL
                            ),
                widget.GroupBox(
                                    font='sans',
                                    fontsize=26,
                                    padding=3,
                                    background="#033f67",
                                    highlight_method="text",
                                    spacing=10,
                                    visible_groups=['1', '2', '3'],
                                ),
                widget.Spacer(
                                background="#033f67",
                                length=1,
                                **decR
                            ),
                widget.Spacer(
                                background="#10153310",
                                **decR
                            ),
                widget.CheckUpdates(
                                        distro='Arch_checkupdates', 
                                        background="#05606b",
                                        colour_have_updates="#ff0000",
                                        colour_no_updates="#00ff00",
                                        no_update_string='  0',
                                        font='Font Awesome',
                                        fontsize=16,
                                        display_format='  {updates}',
                                        **decR,
                                    ),
                widget.PulseVolume(
                                background="#033f67",
                                foreground="#a37aed",
                                fontsize=16,
                                font='Font Awesome',
                                cannel='Master',
                                fmt='   {}',
                                mouse_callbacks={"Button1": lazy.spawn("pavucontrol-qt")},
                                **decR,
                            ),
                widget.Systray(
                                background="#05606b",
                                **decR 
                            ),
                widget.Clock(
                                font='Font Awesome',
                                background="#033f67",
                                foreground="#a37aed",
                                fontsize=18,
                                padding=3,
                                format="   %H:%M",                         
                            ),
                bar_spacerFixedWQHD,
            ],
            background="#000000ff",
            size=35,
        ),
    ),

    # Screen 2 FHD 27"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(
                                background="#033f67",
                                length=20,
                                **decL
                            ),
                widget.Spacer(
                                background="#101533",
                                **decL
                            ),
                bar_groupbox_2,
                widget.Spacer(
                                background="#033f67",
                                length=1,
                                **decR
                            ),
                widget.Spacer(
                                background="#101533",
                                **decR
                            ),
                bar_clockFHD,
                bar_spacerFixed,
            ],
            size=26,
        ),

    ),

    # Screen 3 FHD 24"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(
                                background="#033f67",
                                length=20,
                                **decL
                            ),
                widget.Spacer(
                                background="#101533",
                                **decL
                            ),
                bar_groupbox_3,
                widget.Spacer(
                                background="#033f67",
                                length=1,
                                **decR
                            ),
                widget.Spacer(
                                background="#101533",
                                **decR
                            ),
                bar_clockFHD,
                bar_spacerFixed,
            ],
            # margin=[5,5,0,5],
            size=26,
        ),
    ),

]