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
from libqtile import bar, qtile
from libqtile.lazy import lazy
from modules.popup import show_power_menu
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.popup.templates.mpris2 import COMPACT_LAYOUT
from qtile_extras.widget.groupbox2 import GroupBoxRule
from helper.colors import wp_colors


# --------------------------------------------------------
# Widget Defaults
# --------------------------------------------------------

widget_defaults = dict(
    foreground=wp_colors[7],   
)


# --------------------------------------------------------
# Decorations
# --------------------------------------------------------

decor = {
    "decorations": [
        RectDecoration(
            colour=wp_colors[2],
            radius=14, 
            filled=True, 
            padding_x=2, 
            extrawidth=10,
            group=False,
            )
        ],
}

decor_gr = {
    "decorations": [
        RectDecoration(
            colour=wp_colors[1], 
            radius=14, 
            filled=True, 
            extrawidth=10, 
            padding_x=2, 
            group=True,
            )
        ],
}

decorQ = {
    "decorations": [
        RectDecoration(
            colour=wp_colors[2],
            radius=18, 
            filled=True, 
            padding_x=2, 
            extrawidth=10,
            group=False,
            )
        ],
}

decor_grQ = {
    "decorations": [
        RectDecoration(
            colour=wp_colors[1], 
            radius=18, 
            filled=True, 
            extrawidth=10, 
            padding_x=2, 
            group=True,
            )
        ],
}

decor_trio = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            radius=14, 
            filled=True, 
            extrawidth=10, 
            padding_x=2, 
            group=True,
        )
    ]
}

decor_trioS = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            radius=14, 
            filled=True, 
            extrawidth=10, 
            padding_x=0, 
            group=True,
        )
    ]
}

# --------------------------------------------------------
# Custom functionalities
# --------------------------------------------------------

# HoverWidgetBox by @elParaguayo
class HoverWidgetBox(widget.WidgetBox):       
    def mouse_enter(self, *args, **kwargs):
        self.open()

    def mouse_leave(self, *args, **kwargs):
        self.close()


# --------------------------------------------------------
# GroupBox2 - Rules
# --------------------------------------------------------


def get_groupbox_rules(monitor_specific=False):
    # Base rules applied to all GroupBoxes
    rules = [
        GroupBoxRule(text_colour=wp_colors[15]).when(focused=False, occupied=True),
        GroupBoxRule(text_colour=wp_colors[8]).when(focused=False, occupied=False),
        GroupBoxRule(text_colour=wp_colors[6]).when(focused=True),
        GroupBoxRule(text_colour='#de6e5e').when(focused=False, occupied=True, urgent=True),
    ]
    
    # Add extra rule for a specific monitor (e.g., show "X" as label)
    if monitor_specific:
        rules.append(GroupBoxRule(text=""))
    
    return rules



# --------------------------------------------------------
# Screens
# --------------------------------------------------------

screens = [

    # Screen 1 WQHD 27"
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename='~/.config/qtile/images/standby_rotated.png',                    
                    scale=True,
                    adjust_x=6,
                    adjust_y=1,
                    margin=0,       # Image Sitze
                    mask=True,
                    colour=wp_colors[5],
                    **decorQ,
                    ),             
                widget.Spacer(length=1),
                widget.GroupBox2(
                    font='Font Awesome',
                    fontshadow=wp_colors[0],
                    fontsize=24,
                    visible_groups=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                    padding=8,
                    rules=get_groupbox_rules(monitor_specific=True),
                    **decor_grQ,
                    ),
                widget.Spacer(),
                widget.Clock(
                    font='Open Sans Bold',
                    background=wp_colors[2],
                    fontsize=18,
                    fontshadow=wp_colors[0],
                    padding=3,
                    format="  %d.%m.%y",
                    **decor_trio                         
                    ),
                widget.TextBox(
                    text="",
                    background=wp_colors[2],
                    foreground=wp_colors[7],
                    fontsize=18,
                    fontshadow=wp_colors[0],
                    font='Font Awesome',
                    **decor_trio                    
                    ),
                widget.Sep(
                    background=wp_colors[2],
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=55,
                    padding=0,
                    **decor_trio
                    ),
                widget.Clock(
                    font='Open Sans Ultra-Bold',
                    fontsize=24,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    format="  %H:%M",
                    **decor_trio,
                    ),
                widget.Sep(
                    background=wp_colors[2],
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=55,
                    padding=0,
                    **decor_trio
                    ),
                widget.TextBox(
                    text="  ",
                    fontsize=18,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    foreground=wp_colors[7],
                    font='Font Awesome',
                    **decor_trio                    
                    ),
                widget.Wttr(
                    font='Open Sans Bold',
                    fontsize=18,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    format='%t',
                    **decor_trio
                    ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=23,
                    ),
                widget.Sep(
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=65,
                    padding=20,
                ),
                HoverWidgetBox(
                    close_button_location='right',
                    text_closed=' ',
                    text_open=' ',
                    fontsize=24,
                    fontshadow=wp_colors[0],
                    padding=6,
                    foreground=wp_colors[7],
                    mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                    widgets=[
                        widget.Net(
                            interface='enp42s0',
                            format='  {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}',
                            use_bits=True,
                            fontsize=16,
                            fontshadow=wp_colors[0],
                            font='Open Sans Bold',
                            mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                            **decor_grQ
                            ),                
                    ],
                    **decor_grQ
                    ),
                HoverWidgetBox(
                    close_button_location='right',
                    font='Font Awesome',
                    fontshadow=wp_colors[0],
                    text_closed=' ',
                    text_open=' ',
                    fontsize=24,
                    foreground=wp_colors[7],
                    widgets=[                                              
                        widget.PulseVolume(
                                fontsize=16,
                                fontshadow=wp_colors[0],
                                font='Open Sans Bold',
                                format='  {volume}%',
                                mouse_callbacks={"Button1": lazy.spawn("pavucontrol-qt")},
                                padding=10,
                                **decor_grQ
                                ),
                    ],
                    **decor_grQ,
                    ),
                widget.WidgetBox(
                    close_button_location='right',
                    font='Font Awesome',
                    fontshadow=wp_colors[0],
                    fontsize=24,
                    foreground=wp_colors[7],
                    padding=10,
                    text_closed="",
                    text_open="",
                    widgets=[
                        widget.Sep(
                            foreground=wp_colors[6],
                            linewidth=2,
                            size_percent=55,
                            padding=20,
                            **decor_grQ
                            ),
                        widget.CheckUpdates(
                            distro='Arch_checkupdates',
                            # colour_have_updates=wp_colors[7],
                            # colour_no_updates=wp_colors[7],
                            no_update_string='0',
                            font='Font Awesome Semi-Bold',
                            fontsize=16,
                            fontshadow=wp_colors[0],
                            display_format='{updates}  ',
                            **decor_grQ
                            ), 
                        widget.TextBox(
                            padding=4,
                            text=' ',  
                            font='Font Awesome',
                            fontsize=18,
                            fontshadow=wp_colors[0],                  
                            mouse_callbacks={"Button1": lazy.spawn("./.config/qtile/helper/set-wallpaper.sh")},
                            # foreground=wp_colors[7],
                            **decor_grQ
                            ),
                    ],                    
                    **decor_grQ
                    ),              
                widget.TextBox(
                    fontsize=22,
                    font='Font Awesome',
                    text="  ",
                    mouse_callbacks={"Button1": lazy.spawn("./.config/qtile/helper/power.sh")},
                    ),
            ],
            background="#30363f00",
            size=35,
            margin=[5, 5, 0, 5],
        ),
    ),

    # Screen 2 FHD 27"
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=2,**decor_gr),
                widget.GroupBox2(
                                    font='Font Awesome',
                                    fontshadow=wp_colors[0],
                                    fontsize=20,
                                    padding=6,
                                    visible_groups=['4', '5', '6'],
                                    rules=get_groupbox_rules(monitor_specific=False),
                                    **decor_gr
                                ),
                widget.Spacer(),
                widget.Clock(
                    font='Open Sans Bold',
                    background=wp_colors[2],
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    padding=3,
                    format="  %d.%m.%y",
                    **decor_trioS                         
                    ),
                widget.TextBox(
                    text="",
                    background=wp_colors[2],
                    foreground=wp_colors[7],
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    font='Font Awesome',
                    **decor_trioS                    
                    ),
                widget.Sep(
                    background=wp_colors[2],
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=55,
                    padding=0,
                    **decor_trioS
                    ),
                widget.Clock(
                    font='Open Sans Ultra-Bold',
                    fontsize=24,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    format="  %H:%M",
                    **decor_trioS,
                    ),
                widget.Sep(
                    background=wp_colors[2],
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=55,
                    padding=0,
                    **decor_trioS
                    ),
                widget.TextBox(
                    text="  ",
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    foreground=wp_colors[7],
                    font='Font Awesome',
                    **decor_trioS                    
                    ),
                widget.Wttr(
                    font='Open Sans Bold',
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    format='%t',
                    **decor_trioS
                    ),
                widget.Spacer(),
                widget.TextBox(
                    fontsize=18,
                    fontshadow=wp_colors[0],
                    font='Font Awesome',
                    text="    ",   
                    **decor_gr,                 
                ),
                widget.Mpris2(
                    font='Open Sans Bold',
                    fontsize=14,
                    fontshadow=wp_colors[0],
                    name="mpris2",
                    width=200,
                    scroll=True,
                    scroll_clear=True,
                    format='{xesam:title} - {xesam:artist}',
                    padding=10,
                    paused_text='{track}',
                    popup_layout=COMPACT_LAYOUT,
                    mouse_callback={'Button1': lazy.widget["mpris2"].popup(),},
                    **decor_gr
                    ),
                widget.TextBox(
                    fontsize=18,
                    font='Font Awesome',
                    text="  ",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show p -modi p:rofi-power-menu")},
                    # mouse_callbacks={"Button1": lazy.function(show_power_menu)},
                    ),                               
            ],
            background="#30363f00",
            size=28,
            margin=[5, 5, 0, 5],
        ),

    ),

    # Screen 3 FHD 24"
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox2(
                                    font='Font Awesome',
                                    fontsize=18,
                                    fontshadow=wp_colors[0],
                                    padding=10,
                                    center_aligned=True,
                                    visible_groups=['7', '8', '9'],
                                    highlight_method='text',
                                    rules=get_groupbox_rules(monitor_specific=False),
                                    **decor_gr
                                ),
                widget.Spacer(),
                widget.Clock(
                    font='Open Sans Bold',
                    background=wp_colors[2],
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    padding=3,
                    format="  %d.%m.%y",
                    **decor_trioS                         
                    ),
                widget.TextBox(
                    text="",
                    background=wp_colors[2],
                    foreground=wp_colors[7],
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    font='Font Awesome',
                    **decor_trioS                    
                    ),
                widget.Sep(
                    background=wp_colors[2],
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=55,
                    padding=0,
                    **decor_trioS
                    ),
                widget.Clock(
                    font='Open Sans Ultra-Bold',
                    fontsize=24,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    format="  %H:%M",
                    **decor_trioS,
                    ),
                widget.Sep(
                    background=wp_colors[2],
                    foreground=wp_colors[3],
                    linewidth=2,
                    size_percent=55,
                    padding=0,
                    **decor_trioS
                    ),
                widget.TextBox(
                    text="  ",
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    foreground=wp_colors[7],
                    font='Font Awesome',
                    **decor_trioS                    
                    ),
                widget.Wttr(
                    font='Open Sans Bold',
                    fontsize=16,
                    fontshadow=wp_colors[0],
                    background=wp_colors[2],
                    format='%t',
                    **decor_trioS
                    ),          
                widget.Spacer(),
                widget.TextBox(
                    fontsize=24,
                    font='Font Awesome',
                    text="  ",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show p -modi p:rofi-power-menu")},
                    # mouse_callbacks={"Button1": lazy.function(show_power_menu)},
                    ),      
            ],
            background="#30363f00",
            size=28,
            margin=[5, 5, 0, 5],
        ),
    ),

]

