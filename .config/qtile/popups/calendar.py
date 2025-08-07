import subprocess

from libqtile import qtile

from qtile_extras import widget
from qtile_extras.popup.toolkit import (PopupRelativeLayout,
                                        PopupWidget,
                                        )

from res.themes.colors import gruvbox_dark

# https://discord.com/channels/955163559086665728/1166312212223250482/1322614846155657370
# check for this PR to change back the code with the message contents to the prev code of the widget:
# PopupWidget(
#                 pos_x=0.051,
#                 pos_y=0.415,
#                 height=0.6,
#                 width=0.9,
#                 widget=widget.GenPollCommand(
#                     cmd="cal",
#                     shell=True,
#                     font='mono',
#                     fontsize=20,
#                     markup=False,
#                     # background=gruvbox_dark["blue"],
#                     )


def parse_cal():
    process = subprocess.run(
        "cal",
        capture_output=True,
        text=True,
    )
    body = process.stdout.strip()
    lines = body.splitlines()
    maxlen = max(len(l) for l in lines)
    output = []
    for line in body.splitlines():
        if len(line) < maxlen:
            line += " " * (maxlen - len(line))
        output.append(line)
    return "\n".join(output).strip("\n")


def calendar(qtile):
    layout = PopupRelativeLayout(
        qtile,
        rows=7,
        cols=9,
        width=300,
        height=310,   
        opacity=0.8,
        hide_on_mouse_leave=True,
        close_on_click=False,
        border_width=0,
        background=gruvbox_dark["bg0_soft"],
        controls=[
            PopupWidget(
                pos_x=0,
                pos_y=0,
                height=0.2,
                width=0.9,
                v_align="middle",
                h_align="center",
                widget=widget.Wttr(
                    fontsize=40,
                    format='%c'
                    )
                ),
            PopupWidget(
                pos_x=0.3,
                pos_y=0.05,
                height=0.05,
                width=0.9,
                v_align="middle",
                h_align="center",
                widget=widget.Wttr(
                    font='Open Sans Bold',
                    fontsize=18,
                    format='Actual: %t'
                    )
                ),
            PopupWidget(
                pos_x=0.3,
                pos_y=0.12,
                height=0.05,
                width=0.9,
                widget=widget.Wttr(
                    font='Open Sans',
                    fontsize=14,
                    format='Feels: %f'
                    )
                ),
            PopupWidget(
                pos_x=0.05,
                pos_y=0.2,
                height=0.05,
                width=0.9,
                widget=widget.Wttr(
                    font='Open Sans',
                    fontsize=14,
                    format='Wind: %w  Prec: %p'
                    )
                ),
            PopupWidget(
                pos_x=0.05,
                pos_y=0.25,
                height=0.11,
                width=0.9,
                widget=widget.Wttr(
                    font='Open Sans Bold',
                    fontsize=14,
                    format='City: %l', # \nFeel;%f Wind: %w'
                    )
                ),
            PopupWidget(
                pos_x=0.051,
                pos_y=0.38,
                height=0.6,
                width=0.9,
                widget=widget.GenPollText(
                    func=parse_cal,
                    font='mono',
                    fontsize=20,
                    markup=False,
                    )
                ),
        ]
    )
    layout.show(relative_to=3, 
                relative_to_bar=True, 
                y=3, 
                x=-3, 
                )