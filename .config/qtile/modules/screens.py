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
    # background='#222222',    
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

grpBx_rule = [
    GroupBoxRule(text_colour=wp_colors[6]).when(focused=False, occupied=True),
    GroupBoxRule(text_colour=wp_colors[15]).when(focused=False, occupied=False),
    GroupBoxRule(text_colour='#966cb6').when(focused=True),
    
]
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
                    adjust_x=5,
                    margin=0,       # Image Sitze
                    mask=True,
                    colour=wp_colors[15],
                    **decor,
                    ),             
                widget.Spacer(length=1),
                widget.GroupBox2(
                    font='Font Awesome',
                    fontsize=24,
                    visible_groups=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                    padding=5,
                    margin=4, 
                    rules=grpBx_rule,
                    **decor_gr,
                    ),
                widget.Spacer(),
                widget.Clock(
                    font='Font Awesome',
                    fontsize=20 ,
                    padding=3,
                    format="    %H:%M",
                    **decor_gr                         
                    ),
                widget.TextBox(
                    text="  ",
                    fontsize=20,
                    round=wp_colors[7],                    
                    font='Font Awesome',
                    **decor_gr                    
                    ),
                widget.Wttr(
                    font='Ubuntu Mono',
                    fontsize=20,
                    format='%t',
                    **decor_gr
                    ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=23,
                    ),
                HoverWidgetBox(
                    close_button_location='right',
                    text_closed='  ',
                    text_open='  ',
                    fontsize=22,
                    foreground=wp_colors[7],
                    mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                    widgets=[
                        widget.Net(
                            interface='enp42s0',
                            format='  {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}',
                            use_bits=True,
                            fontsize=16,
                            font='Font Awesome',
                            mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                            **decor_gr
                            ),                
                    ],
                    **decor_gr
                    ),
                HoverWidgetBox(
                    close_button_location='right',
                    font='Font Awesome',
                    text_closed=' ',
                    text_open=' ',
                    fontsize=22,
                    foreground=wp_colors[7],
                    widgets=[  
                        widget.Sep(
                            size_percent=60,
                            **decor_gr),                                              
                        widget.PulseVolume(
                                fontsize=18,
                                font='Font Awesome',
                                mouse_callbacks={"Button1": lazy.spawn("pavucontrol-qt")},
                                **decor_gr
                                ),
                    ],
                    **decor_gr,
                    ),
                HoverWidgetBox(
                    close_button_location='right',
                    font='Font Awesome',
                    text_closed=' ',
                    text_open=' ',
                    fontsize=20,
                    foreground=wp_colors[7],
                    mouse_callbacks={"Button1": lazy.spawn("alacritty -T FloatWindow -e ./.config/qtile/assets/update.sh")},
                    widgets=[
                        widget.Sep(
                            size_percent=60,
                            **decor_gr),                                             
                        widget.CheckUpdates(
                            distro='Arch_checkupdates',
                            colour_have_updates=wp_colors[7],
                            colour_no_updates=wp_colors[7],
                            no_update_string='0',
                            font='Font Awesome',
                            fontsize=20,
                            display_format='{updates}',
                            **decor_gr
                            ),                                
                    ],
                **decor_gr  
                ),
                widget.TextBox(
                    text='',  
                    font='Font Awesome',
                    fontsize=22,                  
                    mouse_callbacks={"Button1": lazy.spawn("./.config/qtile/helper/set-wallpaper.sh")},
                    foreground=wp_colors[7],
                    **decor_gr
                    ), 
                widget.TextBox(
                    fontsize=22,
                    font='Font Awesome',
                    text="  ",
                    # mouse_callbacks={"Button1": lazy.spawn("rofi -show p -modi p:rofi-power-menu")},
                    mouse_callbacks={"Button1": lazy.function(show_power_menu)},
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
                widget.GroupBox2(
                                    font='Font Awesome',
                                    fontsize=20,
                                    visible_groups=['4', '5', '6'],
                                    rules=grpBx_rule,
                                    **decor_gr
                                ),
                widget.Spacer(),
                widget.Clock(
                    font='Font Awesome',
                    fontsize=18,
                    padding=3,
                    format="   %H:%M",
                    **decor_gr                         
                    ),
                widget.Spacer(),
                widget.Mpris2(
                    name="mpris2",
                    scroll=False,
                    format='   {xesam:title} - {xesam:artist}',
                    padding=10,
                    paused_text='{track}',
                    popup_layout=COMPACT_LAYOUT,
                    mouse_callback={'Button1': lazy.widget["mpris2"].popup(),},
                    **decor
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
                                    padding=6,
                                    center_aligned=True,
                                    visible_groups=['7', '8', '9'],
                                    highlight_method='text',
                                    rules=grpBx_rule,
                                    **decor_gr
                                ),
                widget.Spacer(),
                widget.Clock(
                    font='Font Awesome',
                    fontsize=20,
                    padding=2,
                    format="    %H:%M",
                    **decor_gr                         
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