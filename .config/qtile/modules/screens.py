#        _   _ _
#   __ _| |_(_) | ___   ___  ___ _ __ ___  ___ _ __  ___
#  / _` | __| | |/ _ \ / __|/ __| '__/ _ \/ _ \ '_ \/ __|
# | (_| | |_| | |  __/ \__ \ (__| | |  __/  __/ | | \__ \
#  \__, |\__|_|_|\___| |___/\___|_|  \___|\___|_| |_|___/
#     |_|
# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------
from libqtile.config import Screen
from libqtile import bar
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.groupbox2 import GroupBoxRule

from plugins.notifications import Notifier

from popups.powermenu import power_menu
from popups.start_menu import start_menu
from popups.calendar import calendar
from popups.mpris2_layout import MPRIS2_LAYOUT
from popups.volume_notification import VOL_POPUP

from res.themes.colors import gruvbox_dark


# --------------------------------------------------------
# GroupBox2 rules
# --------------------------------------------------------
def get_groupbox_rules(monitor_specific=True):
    # Base rules applied to all GroupBoxes
    rules = [
        GroupBoxRule(text_colour=gruvbox_dark["bg3"]).when(
            focused=False, occupied=True
        ),
        GroupBoxRule(text_colour=gruvbox_dark["aqua"]).when(
            focused=False, occupied=False
        ),
        GroupBoxRule(text_colour=gruvbox_dark["fg3"]).when(focused=True),
        GroupBoxRule(text_colour=gruvbox_dark["red"]).when(
            focused=False, occupied=True, urgent=True
        ),
        GroupBoxRule(visible=False).when(focused=False, occupied=False),
    ]

    # Add extra rule for a specific monitor (e.g., show "X" as label)
    if monitor_specific:
        rules.append(GroupBoxRule(text=""))
    return rules


# --------------------------------------------------------
# Widget Defaults
# --------------------------------------------------------
widget_defaults = dict(font="Open Sans", fontsize=18, foreground=gruvbox_dark["fg1"])
extension_defaults = widget_defaults.copy()

# --------------------------------------------------------
# Screens
# --------------------------------------------------------
bar.Bar
screens = [
    Screen(
        # Center Screen
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    fontsize=24,
                    foreground=gruvbox_dark["blue"],
                    mouse_callbacks={"Button1": lazy.function(start_menu)},
                ),
                widget.GroupBox2(
                    padding=5,
                    fontsize=22,
                    font="Open Sans",
                    center_aligned=True,
                    visible_groups=[
                        "1",
                        "2",
                        "3",
                        "0",
                        "f8",
                        "f9",
                        "f10",
                        "f11",
                        "f12",
                    ],
                    hide_unused=True,
                    rules=get_groupbox_rules(monitor_specific=False),
                ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=21,
                ),
                widget.Spacer(length=6),
                widget.Clock(mouse_callbacks={"Button1": lazy.function(calendar)}),
                widget.Spacer(length=2),
                widget.TextBox(
                    font="Open Sans",
                    fontsize=20,
                    text=" ",
                    mouse_callbacks={"Button1": lazy.function(power_menu)},
                ),
                #                widget.PulseVolumeExtra(
                #                    mode="popup",
                #                    fmt="",
                #                    popup_layout=VOL_POPUP,
                #                    popup_hide_timeout=3,
                #                    popup_show_args={"relative_to": 8, "y": -70},
                #                ),
            ],
            background=gruvbox_dark["bg0_hard"],
            opacity=0.75,
            size=32,
            margin=[3, 3, 0, 3],
        ),
    ),
    Screen(
        # Right Screen
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    fontsize=24,
                    foreground=gruvbox_dark["blue"],
                    mouse_callbacks={"Button1": lazy.function(start_menu)},
                ),
                widget.GroupBox2(
                    padding=6,
                    fontsize=22,
                    margin=7,
                    font="Open Sans",
                    center_aligned=True,
                    visible_groups=["7", "8", "9", "f2", "f4", "f5", "f6"],
                    hide_unused=True,
                    rules=get_groupbox_rules(monitor_specific=False),
                ),
                widget.Spacer(),
                widget.WidgetBox(
                    fontsize=22,
                    text_closed="󱤟",
                    text_open="󱤠",
                    widgets=[
                        widget.Memory(
                            format="  {MemPercent}%",
                            font="Open Sans",
                        ),
                        widget.CPU(
                            format="  {load_percent}%",
                            font="Open Sans",
                        ),
                    ],
                ),
                widget.Spacer(length=6),
                widget.Clock(mouse_callbacks={"Button1": lazy.function(calendar)}),
                widget.Spacer(length=2),
                widget.TextBox(
                    font="Open Sans",
                    fontsize=20,
                    text=" ",
                    mouse_callbacks={"Button1": lazy.function(power_menu)},
                ),
            ],
            background=gruvbox_dark["bg0_hard"],
            opacity=0.75,
            size=32,
            margin=[3, 3, 0, 3],
        ),
    ),
    Screen(
        # Left Screen
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    fontsize=24,
                    foreground=gruvbox_dark["blue"],
                    mouse_callbacks={"Button1": lazy.function(start_menu)},
                ),
                widget.GroupBox2(
                    padding=6,
                    fontsize=22,
                    font="Open Sans",
                    center_aligned=True,
                    visible_groups=[
                        "4",
                        "5",
                        "6",
                        "f1",
                        "f7",
                        "f3",
                    ],
                    hide_unused=True,
                    rules=get_groupbox_rules(monitor_specific=False),
                ),
                widget.Spacer(length=20),
                widget.Mpris2(
                    name="mpris2",
                    width=350,
                    scroll=True,
                    scroll_clear=True,
                    foreground=gruvbox_dark["fg1"],
                    format="{xesam:title} - {xesam:artist}",
                    paused_text="{track}   ",
                    popup_layout=MPRIS2_LAYOUT,
                    poll_interval=15,
                    popup_show_args={"relative_to": 2, "relative_to_bar": True, "y": 3},
                    mouse_callbacks={"Button1": lazy.widget["mpris2"].toggle_player()},
                ),
                widget.Spacer(),
                widget.Clock(mouse_callbacks={"Button1": lazy.function(calendar)}),
                widget.Spacer(length=2),
                widget.TextBox(
                    fontsize=20,
                    text=" ",
                    mouse_callbacks={"Button1": lazy.function(power_menu)},
                ),
            ],
            background=gruvbox_dark["bg0_hard"],
            opacity=0.75,
            size=32,
            margin=[3, 3, 0, 3],
        ),
    ),
    Screen(
        # Left Screen
        top=bar.Bar(
            [],
            background=gruvbox_dark["bg0_hard"],
            opacity=0.75,
            size=32,
            margin=[3, 3, 0, 3],
        ),
    ),
]

notifier = Notifier(
    x=1155,
    y=38,
    width=250,
    height=96,
    format="<b>{summary}</b>\n{app_name}\n{body}",
    # file_name='/home/cerberus/.config/qtile/normal.png',    # Not working
    foreground=gruvbox_dark["fg1"],
    background=(
        gruvbox_dark["bg0_hard"],
        gruvbox_dark["bg0_hard"],
        gruvbox_dark["orange"],
    ),
    horizontal_padding=8,
    vertical_padding=8,
    opacity=0.65,
    border_width=0,
    font="Open Sans",
    font_size=16,
    overflow="truncate",
    fullscreen="queue",
    screen=0,
    actions=True,
    # wrap=True
)
