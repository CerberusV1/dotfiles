#        _   _ _        _                 _
#   __ _| |_(_) | ___  | |__   ___   ___ | | _____
#  / _` | __| | |/ _ \ | '_ \ / _ \ / _ \| |/ / __|
# | (_| | |_| | |  __/ | | | | (_) | (_) |   <\__ \
#  \__, |\__|_|_|\___| |_| |_|\___/ \___/|_|\_\___/
#     |_|
# by cerberus
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------
from libqtile import hook, qtile
import subprocess
import os.path

# --------------------------------------------------------------------
# HOOK startup
# --------------------------------------------------------------------


@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/res/scripts/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])


@hook.subscribe.startup_complete
def go_to_group1():
    qtile.focus_screen(0)
    qtile.groups_map["1"].toscreen()
