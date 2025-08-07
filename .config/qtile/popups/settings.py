from libqtile import qtile
from libqtile.lazy import lazy

from res.themes.colors import gruvbox_dark

from qtile_extras.popup.menu import (
    PopupMenu,
    PopupMenuItem,
    PopupMenuSeparator,
    )

items = [
    PopupMenuItem(# Wallpaper setting
                show_icon=False,
                text=' 󰸉   Nitrogen Wallpaper',
                font='Open Sans',
                fontsize=16,
                can_focus=True,
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("nitrogen")},
                ),
    PopupMenuSeparator(),
    PopupMenuItem(# Arandr
                show_icon=False,
                text=' 󰹑   Arandr Display',
                font='Open Sans',
                fontsize=16,
                can_focus=True,
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("arandr")},),
    PopupMenuSeparator(),
    PopupMenuItem(# VS-Code qtile config
                show_icon=False,
                text='    Qtile Config',
                font='Open Sans',
                fontsize=16,
                can_focus=True,
                highlight_method='text',
                foreground=gruvbox_dark["fg0"],
                highlight=gruvbox_dark["green"],
                mouse_callbacks={"Button1": lazy.spawn("code /home/cerberus/.config/")},),
]

def settings(qtile):
    layout = PopupMenu.generate(
                    qtile,
                    pos_x=100,
                    pos_y=100,
                    width=225,
                    opacity=0.7,
                    menuitems=items,
                    background=gruvbox_dark["bg0_soft"]
                    )
    layout.show(relative_to=1, relative_to_bar=True, y=75, x=325)

