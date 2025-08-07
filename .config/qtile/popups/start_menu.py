from libqtile import qtile
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText,
    PopupWidget,
)

from res.themes.colors import gruvbox_dark
from popups.settings import settings
from popups.network import network_menu
from popups.powermenu_sub import powermenu_2
from popups.monitor import monitor


def start_menu(qtile):
    layout = PopupRelativeLayout(
        qtile,
        width=350,
        height=150,
        opacity=0.7,
        hide_on_mouse_leave=True,
        close_on_click=False,
        border_width=0,
        background=gruvbox_dark["bg0_soft"],
        controls=[
            # Row 1
            PopupImage(
                # Qtile logo
                pos_x=0,
                pos_y=0,
                height=0.3,
                width=0.3,
                mask=True,
                colour=gruvbox_dark["blue"],
                filename="/home/cerberus/.config/qtile/res/images/standby_rotated.png",
            ),
            PopupWidget(
                # Welcome banner, fetching user name from $USER
                pos_x=0.241,
                pos_y=0.12,
                height=0.15,
                width=0.8,
                widget=widget.GenPollCommand(
                    foreground=gruvbox_dark["orange"],
                    cmd="echo Welcome $USER",
                    shell=True,
                    font="Open Sans Bold",
                    fontsize=20,
                    width=250,
                    scroll=True,
                ),
            ),
            # PopupText(
            #    # Steam Gamemode (Controller)
            #    pos_x=0,
            #    pos_y=0,
            #    width=0.3,
            #    height=0.3,
            #    can_focus=True,
            #    v_align="middle",
            #   h_align="center",
            #    background=gruvbox_dark["green"],
            # ),
            PopupText(
                # Steam Gamemode (Controller)
                text="󰊴",
                fontsize=34,
                pos_x=0.271,
                pos_y=0.4,
                width=0.34,
                height=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method="text",
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                background=gruvbox_dark["bg2"],
                mouse_callbacks={
                    "Button1": lazy.spawn("steam steam://open/bigpicture")
                },
            ),
            PopupText(
                # Settings
                text="",
                fontsize=22,
                pos_x=0.631,
                pos_y=0.4,
                width=0.34,
                height=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method="text",
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                background=gruvbox_dark["bg2"],
                mouse_callbacks={"Button1": lazy.function(settings)},
            ),
            PopupText(
                # Power-Menu Popup
                text="󱖘",
                fontsize=24,
                pos_x=0.035,
                pos_y=0.7,
                width=0.22,
                height=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method="text",
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                background=gruvbox_dark["bg2"],
                mouse_callbacks={"Button1": lazy.function(powermenu_2)},
            ),
            PopupText(
                # Bluetooth
                text="󰨇",
                fontsize=22,
                pos_x=0.271,
                pos_y=0.7,
                width=0.22,
                height=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method="text",
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                background=gruvbox_dark["bg2"],
                mouse_callbacks={"Button1": lazy.function(monitor)},
            ),
            PopupText(
                # Network Popup
                text="󰌘",
                fontsize=24,
                pos_x=0.511,
                pos_y=0.7,
                width=0.22,
                height=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method="text",
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                background=gruvbox_dark["bg2"],
                mouse_callbacks={"Button1": lazy.function(network_menu)},
            ),
            PopupText(
                # Audiocontrol
                text="",
                fontsize=24,
                pos_x=0.75,
                pos_y=0.7,
                width=0.22,
                height=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method="text",
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                background=gruvbox_dark["bg2"],
                mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
            ),
            PopupText(
                # "extras"
                text="extras",
                font="Open Sans Bold",
                foreground=gruvbox_dark["fg2"],
                fontsize=10,
                pos_x=0.055,
                pos_y=0.57,
                height=0.05,
                width=0.15,
            ),
        ],
    )
    layout.show(relative_to=1, relative_to_bar=True, y=3, x=3)

