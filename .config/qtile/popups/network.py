from libqtile import qtile
from libqtile.lazy import lazy

from res.themes.colors import gruvbox_dark

from qtile_extras.popup.menu import (
    PopupMenu,
    PopupMenuItem,
    PopupMenuSeparator,
    )

items=[
    PopupMenuItem(
            show_icon=False,
            text='󰛳   Network Manager',
            font='Open Sans',
            fontsize=16,
            can_focus=True,
            highlight_method='text',
            foreground=gruvbox_dark["fg0"],
            highlight=gruvbox_dark["green"],
            mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
            ),
    PopupMenuSeparator(),
    PopupMenuItem(
            show_icon=False,
            text='󰐚   Wireguard',
            font='Open Sans',
            fontsize=16,
            highlight_method='text',
            can_focus=True,
            foreground=gruvbox_dark["fg0"],
            highlight=gruvbox_dark["green"],
            mouse_callbacks={"Button1": lazy.spawn("wireguird")},
            )
]

def network_menu(qtile):
        layout = PopupMenu.generate(
                    qtile,
                    pos_x=100,
                    pos_y=100,
                    width=225,
                    opacity=0.7,
                    menuitems=items,
                    background=gruvbox_dark["bg0_soft"]
                    )
        layout.show(relative_to=1, relative_to_bar=True, y=136, x=220)