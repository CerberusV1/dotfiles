from libqtile import qtile

from qtile_extras import widget
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupWidget,
)

from res.themes.colors import gruvbox_dark


def monitor(qtile):
    layout = PopupRelativeLayout(
        qtile,
        rows=7,
        cols=9,
        width=600,
        height=420,
        opacity=0.8,
        hide_on_mouse_leave=True,
        close_on_click=False,
        border_width=0,
        background=gruvbox_dark["bg0_soft"],
        controls=[],
    )
    layout.show(
        relative_to=5,
        relative_to_bar=True,
        # y=3,
        # x=-3,
    )
