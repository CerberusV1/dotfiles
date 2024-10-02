from libqtile import qtile
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
# import Path

def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="~/dotfiles/.config/qtile/images/reboot.png",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={"Button1": lazy.spawn("/.config/qtile/assets/reboot.sh"),},
        ),
        PopupImage(
            filename="~/Downloads/3cx.png",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            # mouse_callbacks={
            #     "Button1": lazy.spawn("/path/to/sleep_cmd")
            # }
        ),
        PopupImage(
            filename="~/Downloads/3cx.png",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.run("./shutdwon.sh")
            }
        ),
        PopupText(
            text="Reboot",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=300,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)