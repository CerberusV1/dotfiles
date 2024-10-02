#        _   _ _                                        
#   __ _| |_(_) | ___    __ _ _ __ ___  _   _ _ __  ___ 
#  / _` | __| | |/ _ \  / _` | '__/ _ \| | | | '_ \/ __|
# | (_| | |_| | |  __/ | (_| | | | (_) | |_| | |_) \__ \
#  \__, |\__|_|_|\___|  \__, |_|  \___/ \__,_| .__/|___/
#     |_|               |___/                |_|        
# by cerberus
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------


from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from keys import terminal, filemanager

from keys import keys, mod

# --------------------------------------------------------
# Groups / Workspaces
# --------------------------------------------------------

groups = [

    # Screen 0
    Group(name="1", screen_affinity=0, label="⏺"),
    Group(name="2", screen_affinity=0, label="⏺"),
    Group(name="3", screen_affinity=0, label="⏺"),

    # Screen 1
    Group(name="4", screen_affinity=1, label="⏺", exclusive=[Match(wm_class="firefox")]), #
    Group(name="5", screen_affinity=1, label="⏺"),
    Group(name="6", screen_affinity=1, label="⏺"),

    # Screen 2
    Group(name="7", screen_affinity=2, label="⏺", matches=[Match(wm_class="discord")]),  
    Group(name="8", screen_affinity=2, label="⏺"),
    Group(name="9", screen_affinity=2, label="⏺", matches=[Match(title="win10 on QEMU/KVM")]),
    
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

groups.append(
    ScratchPad(
        'scratchpad',
        [
            DropDown(
                'term',
                terminal,
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.25,
                opacity=1
            ),
            DropDown(
                'mixer',
                'pavucontrol-qt',
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.2,
                opacity=1
            ),
            DropDown(
                'files',
                filemanager,
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.2,
                opacity=1
            ),
            DropDown(
                'yt',
                'youtube-music',
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.2,
                opacity=1
            ),
            DropDown(
                'calc',
                'qalculate-qt',
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.2,
                opacity=1
            ),
        ]
    )
)


