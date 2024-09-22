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


layout_defaults = dict(
    margin = 5,
    border_width = 3,
    border_focus="#FFFFFF",
    grow_amount = 3,
    )

floating_layout_defaults = layout_defaults.copy()
floating_layout_defaults["border_width"] = 0

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

floating_layout = layout.Floating(auto_float_typesR=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'notify'},
    {'wmclass': 'popup_menu'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'nm-connection-editor'},  # networkmanager
    {'wmclass': 'bitwarden'},  # bitwarden
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitkm
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ], 
    **floating_layout_defaults
    )