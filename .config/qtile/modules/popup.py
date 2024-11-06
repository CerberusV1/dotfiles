from libqtile import qtile
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
# import Path

def show_power_menu(qtile):
    layout = PopupRelativeLayout(
        qtile,
        rows=2,
        cols=3,
        width=150,
        height=300,
        controls=[
        PopupImage(
            filename="~/dotfiles/.config/qtile/images/reboot.png",
            pos_x=0.1,
            pos_y=0,
            width=0.8,
            height=0.3,
            mouse_callbacks={"Button1": lazy.spawn("./.config/qtile/helper/reboot.sh")},
        ),
        PopupImage(
            filename="~/dotfiles/.config/qtile/images/sleep.png",
            pos_x=0.1,
            pos_y=0.33,
            width=0.8,
            height=0.3,
            mouse_callbacks={"Button1": lazy.spawn("./.config/qtile/helper/test.sh")},
        ),
        PopupImage(
            filename="~/dotfiles/.config/qtile/images/standby.png",
            pos_x=0.1,
            pos_y=0.66,
            width=0.8,
            height=0.3,
            highlight="A00000",
            mouse_callbacks={"Button1": lazy.spawn("./.config/qtile/helper/test.sh")},
        ),
    ],
        background="00000060",
        initial_focus=None,
    )

    layout.show(relative_to=3, relative_to_bar=True)