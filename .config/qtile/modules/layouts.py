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
from helper.colors import wp_colors


layout_defaults = dict(
    margin = 5,
    border_width = 3,
    border_focus=wp_colors[3],
    border_normal=wp_colors[7],
    grow_amount = 2,
    )

floating_layout_defaults = layout_defaults.copy()

layouts = [
    # layout.Max(**layout_defaults),
    # layout.Plasma(),
    # layout.Stack(num_stacks=2),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(name="Monad",
                     auto_maximize=True,
                     change_ratio=0.05,
                     change_size=20,
                     ratio=0.55,
                     min_ratio=0.30,
                     max_ratio=0.75,
                     **layout_defaults
                     ),
    layout.Bsp(name="bsp",
               ratio = 0.5,
               border_on_single= True,
               lower_right = True,
               **layout_defaults,
               ),
    layout.Spiral(**layout_defaults),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(name="Tile", **layout_defaults),
    # layout.TreeTab(),
    # layout.VerticalTile(),
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
        Match(wm_class="bitwarden"),  # bitwarden        
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="FloatWindow"),
        Match(wm_class="qalculate-qt"),
        Match(wm_class="copyq"),
        Match(wm_class="nitrogen"),
        Match(wm_class="nemo-preview-start"),
    ],
    **floating_layout_defaults
)