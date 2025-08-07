#        _   _ _        _                         _
#   __ _| |_(_) | ___  | | __ _ _   _  ___  _   _| |_ ___
#  / _` | __| | |/ _ \ | |/ _` | | | |/ _ \| | | | __/ __|
# | (_| | |_| | |  __/ | | (_| | |_| | (_) | |_| | |_\__ \
#  \__, |\__|_|_|\___| |_|\__,_|\__, |\___/ \__,_|\__|___/
#     |_|                       |___/
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------
from libqtile import layout
from libqtile.config import Match

layout_defaults = dict(
    margin=3,
    border_width=0,
    # border_focus=gruvbox_dark["red"],
    # border_normal=gruvbox_dark["fg1"],
    grow_amount=2,
)

floating_layout_defaults = layout_defaults.copy()

layouts = [
    # layout.Max(**layout_defaults),
    # layout.Plasma(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(
        name="Monad",
        auto_maximize=True,
        change_ratio=0.05,
        change_size=20,
        ratio=0.55,
        min_ratio=0.30,
        max_ratio=0.75,
        single_border_width=0,
        **layout_defaults,
    ),
    layout.Bsp(
        name="bsp",
        ratio=0.5,
        lower_right=True,
        **layout_defaults,
    ),
    layout.Spiral(**layout_defaults),
    # layout.Stack(num_stacks=2),
    # layout.MonadWide(**layout_defaults),
    # layout.RatioTile(**layout_defaults),
    # layout.Tile(name="Tile", **layout_defaults),
    # layout.TreeTab(**layout_defaults),
    layout.VerticalTile(**layout_defaults),
    # layout.Zoomy(**layout_defaults),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="nm-connection-editor"),  # networkmanager
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="FloatWindow"),
        Match(wm_class="qalculate-qt"),
        Match(wm_class="copyq"),
        Match(wm_class="nitrogen"),
        Match(wm_class="nemo-preview-start"),
        Match(wm_class="wireguird"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="org.gnome.FileRoller"),
        Match(wm_class="lximage-qt"),
    ],
    **floating_layout_defaults,
)
