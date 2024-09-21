#   ___ _____ ___ _     _____    ____             __ _       
#  / _ \_   _|_ _| |   | ____|  / ___|___  _ __  / _(_) __ _ 
# | | | || |  | || |   |  _|   | |   / _ \| '_ \| |_| |/ _` | 
# | |_| || |  | || |___| |___  | |__| (_) | | | |  _| | (_| | 
#  \__\_\|_| |___|_____|_____|  \____\___/|_| |_|_| |_|\__, | 
#                                                      |___/ 
#
#
#

# --------------------------------------------------------
# Imports
# --------------------------------------------------------

from libqtile import bar, layout, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

import os.path
import subprocess

# --------------------------------------------------------
# Your configuration
# --------------------------------------------------------

wallpaper = os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/wallhaven-exq28r.png")
# wallpaper_mode ="fill"

# --------------------------------------------------------
# Set default apps
# --------------------------------------------------------

terminal = "alacritty"
browser = "firefox"     

# --------------------------------------------------------
# Keybindings
# --------------------------------------------------------

mod = "mod4" # SUPER KEY

keys = [

    # Focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window around"),
    # ________________________________________________________


    # Move
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # ________________________________________________________


    # Size
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Up", lazy.layout.shrink(), desc="Grow window to the top"),
    Key([mod, "control"], "Down", lazy.layout.grow(), desc="Grow window to the bottom"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # ________________________________________________________


    # Floating
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
    # ________________________________________________________


    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # ________________________________________________________


    # Split
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # ________________________________________________________


    # System
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # ________________________________________________________


    # Programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn Rofi"),
    Key([mod], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Spawn Rofi"),
    # Key([mod], "p", lazy.spawn("rofi -show ssh"), desc="Spawn Rofi"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Screenshot selection"),
    # ________________________________________________________
    
]


# --------------------------------------------------------
# Groups / Workspaces
# --------------------------------------------------------

groups = [

    # Screen 0
    Group(name="1", screen_affinity=0, label=""),
    Group(name="2", screen_affinity=0, label=""),
    Group(name="3", screen_affinity=0, label=""),

    # Screen 1
    Group(name="4", screen_affinity=1, label="", matches=[Match(wm_class="firefox")]),
    Group(name="5", screen_affinity=1, label="", matches=[Match(wm_class="youtube music")]),
    Group(name="6", screen_affinity=1, label=""),

    # Screen 2
    Group(name="7", screen_affinity=2, label="", matches=[Match(wm_class="discord")]),  
    Group(name="8", screen_affinity=2, label=""),
    Group(name="9", screen_affinity=2, label=""),
    
]


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return
        elif len(qtile.screens) == 2:
            qtile.groups_map[name].toscreen()
            return

        if name in '123':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        elif name in '456':
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(2)
            qtile.groups_map[name].toscreen()    

    return _inner

for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))

def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return
        elif len(qtile.screens) == 2:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in "123":
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        elif name in "456":
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(2)
            qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    keys.append(Key([mod, "shift"], i.name, lazy.function(go_to_group_and_move_window(i.name))))


# --------------------------------------------------------
# Layouts
# --------------------------------------------------------

layouts = [
    # layout.Columns(),
    # layout.Max(),
    layout.Bsp(
        ratio = 0.5,
        margin = 5,
        shift_windows = True,
        grow_amount = 5,
        # border_width = 2,
    ),
]


# ------------------------------------------------------------
# Setup Widget Defaults ->  depricated with multiple screens 
#                           which have different resolutions
# ------------------------------------------------------------

# widget_defaults = dict(
#     font="sans",
#     fontsize=18,
#     padding=3,
# )
# extension_defaults = widget_defaults.copy()


# --------------------------------------------------------
# Decorations
# --------------------------------------------------------

decR = {
    "decorations": [
        PowerLineDecoration(
                                path="forward_slash"
                            )
    ],
    "padding": 5,
}

decL = {
    "decorations": [
        PowerLineDecoration(
                                path="back_slash"
                            )
    ],
    "padding": 5,
}



# --------------------------------------------------------
# Widgets
# --------------------------------------------------------

# Groupboxes for the different screens
bar_groupbox_2 = widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    background="#033f67",
                                    padding=3,
                                    visible_groups=['4', '5', '6']
                                )

bar_groupbox_3 = widget.GroupBox(
                                    font='sans',
                                    fontsize=14,
                                    background="#033f67",
                                    padding=3,
                                    visible_groups=['7', '8', '9']
                                )

# Keychord Widget to display the keychords in the top bar
bar_keychord = widget.Chord(
                                font='sans',
                                fontsize=14,
                                padding=3,
                                chords_colors={"launch": ("#ff0000", "#ffffff"),},
                                name_transform=lambda name: name.upper(),
                            )

# Clock Widget
bar_clockFHD = widget.Clock(
                                font='sans',
                                fontsize=14,
                                background="#033f67",
                                padding=3,
                                format="%d.%m.%y %H:%M",                       
                            )

# Spacer (flexible)
bar_spacer = widget.Spacer(
                                background="#101533",
                            )

# Spacer (fixed)
bar_spacerFixed = widget.Spacer(
                                background="#033f67",
                                length=10
                            )
# Spacer (fixed)
bar_spacerFixedWQHD = widget.Spacer(
                                background="#033f67",
                                length=10,
                            )


# --------------------------------------------------------
# Screens
# --------------------------------------------------------


screens = [

    # Screen 1 WQHD 27"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(
                                background="#033f67",
                                length=20,
                                **decL
                            ),
                widget.Wttr(
                                background="#05606b",
                                font='sans',
                                fontsize=16,
                                format='%c %t',
                                **decL
                            ),
                widget.Net(
                                background="#033f67",
                                fontsize=16,
                                font='Font Awesome',
                                mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},
                                foreground="#a37aed",
                                interface="enp42s0",
                                format='  {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                                **decL
                            ),
                widget.Spacer(
                                background="#101533",
                                **decL
                            ),
                widget.GroupBox(
                                    font='sans',
                                    fontsize=26,
                                    padding=3,
                                    background="#033f67",
                                    highlight_method="text",
                                    spacing=10,
                                    visible_groups=['1', '2', '3'],
                                ),
                widget.Spacer(
                                background="#033f67",
                                length=1,
                                **decR
                            ),
                widget.Spacer(
                                background="#10153310",
                                **decR
                            ),
                widget.CheckUpdates(
                                        distro='Arch_checkupdates', 
                                        background="#05606b",
                                        colour_have_updates="#ff0000",
                                        colour_no_updates="#00ff00",
                                        no_update_string='  0',
                                        font='Font Awesome',
                                        fontsize=16,
                                        display_format='  {updates}',
                                        **decR,
                                    ),
                widget.Volume(
                                background="#033f67",
                                foreground="#a37aed",
                                fontsize=16,
                                font='Font Awesome',
                                fmt='   {}',
                                mouse_callbacks={"Button1": lazy.spawn("pavucontrol-qt")},
                                **decR,
                            ),
                widget.Systray(
                                background="#05606b",
                                **decR 
                            ),
                widget.Clock(
                                font='Font Awesome',
                                background="#033f67",
                                foreground="#a37aed",
                                fontsize=18,
                                padding=3,
                                format="   %H:%M",                         
                            ),
                bar_spacerFixedWQHD,
            ],
            background="#000000ff",
            size=35,
        ),
    ),

    # Screen 2 FHD 27"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(
                                background="#033f67",
                                length=20,
                                **decL
                            ),
                widget.Spacer(
                                background="#101533",
                                **decL
                            ),
                bar_groupbox_2,
                widget.Spacer(
                                background="#033f67",
                                length=1,
                                **decR
                            ),
                widget.Spacer(
                                background="#101533",
                                **decR
                            ),
                bar_clockFHD,
                bar_spacerFixed,
            ],
            size=26,
        ),

    ),

    # Screen 3 FHD 24"
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), "Pictures/Wallpaper/orange.jpg"),
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(
                                background="#033f67",
                                length=20,
                                **decL
                            ),
                widget.Spacer(
                                background="#101533",
                                **decL
                            ),
                bar_groupbox_3,
                widget.Spacer(
                                background="#033f67",
                                length=1,
                                **decR
                            ),
                widget.Spacer(
                                background="#101533",
                                **decR
                            ),
                bar_clockFHD,
                bar_spacerFixed,
            ],
            # margin=[5,5,0,5],
            size=26,
        ),
    ),

]


# --------------------------------------------------------
# Drag floating layouts
# --------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


# --------------------------------------------------------
# General Setup
# --------------------------------------------------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 18


# --------------------------------------------------------
# Define floating layouts
# --------------------------------------------------------

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
        
    ]
)


# --------------------------------------------------------
# Window Manager Name
# --------------------------------------------------------

wmname = "Qtile"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#leider behalten auch mit dieser configuration die icons einen transperenten hintergrund
# --------------------------------------------------------

# HOOK startup
@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
