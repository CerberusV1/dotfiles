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
from popup import show_power_menu
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.popup.templates.mpris2 import COMPACT_LAYOUT


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
            line_colour=colors["white"],
            line_width=2, 
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
            colour=colors["highlight"]["o2"],            
            line_colour=colors["white"],
            line_width=2,  
            radius=14, 
            filled=True, 
            extrawidth=10, 
            padding_x=2, 
            group=True,
            )
        ],
}


# HoverWidgetBox by @elParaguayo
class HoverWidgetBox(widget.WidgetBox):       
    def mouse_enter(self, *args, **kwargs):
        self.open()

    def mouse_leave(self, *args, **kwargs):
        self.close()

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
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun -show-icons")},
                    scale=True,
                    adjust_x=5,
                    margin=7,       # Image Sitze
                    **decor,
                    ),                
                widget.Spacer(length=1),
                widget.GroupBox(
                    font='sans',
                    fontsize=30,
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
                    fontsize=20 ,
                    padding=3,
                    format="    %H:%M",
                    **decor_gr                         
                    ),
                widget.TextBox(
                    text="  ",
                    fontsize=20,
                    foreground=colors["white"],                    
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
                    mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                    widgets=[
                        widget.Net(
                            interface='enp42s0',
                            format='  {down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}',
                            use_bits=True,
                            fontsize=16,
                            foreground=colors["white"],                    
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
                    widgets=[  
                        widget.Sep(
                            foreground=colors["white"],
                            size_percent=60,
                            **decor_gr),                                              
                        widget.PulseVolume(
                                foreground=colors["white"],
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
                    widgets=[
                        widget.Sep(
                            foreground=colors["white"],
                            size_percent=60,
                            **decor_gr),                                             
                        widget.CheckUpdates(
                            distro='Arch_checkupdates',
                            colour_have_updates=colors["white"],
                            colour_no_updates=colors["white"],
                            no_update_string='0',
                            font='Font Awesome',
                            fontsize=20,
                            display_format='{updates}',
                            mouse_callbacks={"Button1": lazy.spawn("alacritty -T FloatWindow -e ./.config/qtile/assets/update.sh")},
                            **decor_gr
                            ),                                
                    ],
                **decor_gr  
                ),
                widget.TextBox(
                    foreground=colors["white"],
                    fontsize=24,
                    font='Font Awesome',
                    text="  ",
                    mouse_callbacks={"Button1": lazy.function(show_power_menu)},
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
                widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    padding=5,
                                    margin_x=5,
                                    visible_groups=['4', '5', '6'],
                                    highlight_method='text',
                                    **decor_gr
                                ),
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
            size=28,
        ),
    ),

]