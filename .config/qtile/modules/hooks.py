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
    autostartscript = "~/.config/qtile/helper/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
    from libqtile import qtile
    qtile.to_screen(1)
    qtile.spawn("firefox")
    

@hook.subscribe.client_new
def move_bitwarden_to_current(client):
    if client.window.get_wm_class() == ('bitwarden', 'Bitwarden'):
        client.togroup(qtile.current_group.name)
        client.group.toscreen(toggle=False)



