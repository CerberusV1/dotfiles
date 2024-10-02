#        _   _ _        _                         _       
#   __ _| |_(_) | ___  | | __ _ _   _  ___  _   _| |_ ___ 
#  / _` | __| | |/ _ \ | |/ _` | | | |/ _ \| | | | __/ __|
# | (_| | |_| | |  __/ | | (_| | |_| | (_) | |_| | |_\__ \
#  \__, |\__|_|_|\___| |_|\__,_|\__, |\___/ \__,_|\__|___/
#     |_|                       |___/                     
# by cerberus
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------
from libqtile import layout
from libqtile.config import Match
from modules import colors
# from helper.colors import wp_colors


layout_defaults = dict(
    margin = 5,
    border_width = 2,
    border_focus=colors["highlight"]["o1"],
    border_normal=colors["white"],
    grow_amount = 3,
    )

floating_layout_defaults = layout_defaults.copy()
# floating_layout_defaults["border_width"] = 2

layouts = [
    # layout.Max(**layout_defaults),
    layout.Bsp(name="bsp", **layout_defaults, shift_windows = True, ratio = 0.5,),
    # layout.Stack(num_stacks=2),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
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
        Match(wm_class="bitwarden"),  # bitwarden        
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="FloatWindow"),
        Match(wm_class="qalculate-qt"),
        Match(wm_class="copyq"),
        Match(wm_class="nitrogen"),
    ],
    **floating_layout_defaults
)