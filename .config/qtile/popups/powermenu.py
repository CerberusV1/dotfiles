from libqtile.lazy import lazy
from res.themes.colors import gruvbox_dark
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupText,
)
# qtile/resources/themes/colors.py
def power_menu(qtile):
    layout = PopupRelativeLayout(
        qtile,
        width=800,
        height=250,
        opacity=0.7,
        # border=gruvbox_dark["red"],
        # border_width=3,
        background=gruvbox_dark["bg0_soft"],
        initial_focus=None,
        controls=[
                    
        PopupText(
            # Lock betterlockscreen --lock blur
            text="",
            fontsize=80,
            pos_y=0,
            pos_x=0.1,
            width=0.2,
            height=1,
            mouse_callbacks={"Button1": lazy.spawn("betterlockscreen --lock blur")},
            highlight_method='text',
            highlight=gruvbox_dark["green"],
        ),
        PopupText(
            # Hybrid Sleep systemctl hybrid-sleep
            text="󰒲",
            fontsize=80,
            pos_y=0,
            pos_x=0.32,
            width=0.2,
            height=1,
            mouse_callbacks={"Button1": lazy.spawn("systemctl hybrid-sleep")},
            highlight_method='text',
            highlight=gruvbox_dark["yellow"],
        ),
        PopupText(
            # Hibernate systemctl hibernate
            text="",
            fontsize=80,
            pos_y=0,
            pos_x=0.55,
            width=0.2,
            height=1,
            mouse_callbacks={"Button1": lazy.spawn("systemctl hibernate")},
            highlight_method='text',
            highlight=gruvbox_dark["orange"],
        ),
        PopupText(
            # Power off systemctl poweroff
            text="",
            fontsize=80,
            pos_y=0,
            pos_x=0.8,
            width=0.2,
            height=1,
            mouse_callbacks={"Button1": lazy.spawn("systemctl poweroff")},
            highlight_method='text',
            highlight=gruvbox_dark["red"],
        ),
        ],
    )
    layout.show(relative_to=5, relative_to_bar=True, hide_on_timeout=5)
