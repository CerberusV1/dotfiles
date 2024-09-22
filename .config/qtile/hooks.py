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
from libqtile import hook

import subprocess
import os.path

# --------------------------------------------------------------------
# HOOK startup
# --------------------------------------------------------------------

@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
    from libqtile import qtile
    qtile.cmd_to_screen(1)
    qtile.cmd_spawn("firefox")
    

