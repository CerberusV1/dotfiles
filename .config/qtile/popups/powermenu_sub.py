from pydoc import importfile
from libqtile import qtile
from libqtile.lazy import lazy

from res.themes.colors import gruvbox_dark

from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText,
)

def powermenu_2(qtile):
    layout = PopupRelativeLayout(
        qtile,
        width=170,
        height=50,   
        opacity=0.7,
        hide_on_mouse_leave=True,
        close_on_click=False,
        border_width=0,
        background=gruvbox_dark["bg0_soft"],
        controls=[
            PopupText(
                # Lock
                text='',
                fontsize=22,
                pos_x=0.07,
                pos_y=0.05,
                height=0.8,
                width=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("betterlockscreen --lock blur")},
            ),
            PopupText(
                # Reboot
                text='',
                fontsize=22,
                pos_x=0.3,
                pos_y=0.05,
                height=0.8,
                width=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("systemctl reboot")},
            ),
            PopupText(
                # Suspend
                text='󰒲',
                fontsize=22,
                pos_x=0.54,
                pos_y=0.05,
                height=0.8,
                width=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("systemctl suspend")},
            ),
            PopupText(
                # Shutdown
                text='',
                fontsize=22,
                pos_x=0.78,
                pos_y=0.05,
                height=0.8,
                width=0.2,
                can_focus=True,
                v_align="middle",
                h_align="center",
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("systemctl poweroff")},
            ),
        ]
    )
    layout.show(relative_to=1, relative_to_bar=True, y=136, x=30)