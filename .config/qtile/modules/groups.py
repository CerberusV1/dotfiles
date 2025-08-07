from libqtile.config import Group, Key, Match, re, DropDown, ScratchPad
from libqtile.lazy import lazy
from modules.keys import keys, mod

groups = [
    Group(
        name="0",
        label="󰓓",
        matches=[
            Match(wm_class=re.compile(r"^(steam)")),
            Match(wm_class=re.compile(r"^(Minecraft*)")),
        ],
    ),
    Group(name="1", label="󰲡"),
    Group(name="2", label="󰲣"),
    Group(name="3", label="󰲥"),
    Group(name="4", label="󰲧"),
    Group(name="5", label="󰲩"),
    Group(name="6", label="󰲫"),
    Group(name="7", label="󰲭"),
    Group(name="8", label="󰲯"),
    Group(name="9", label="󰲱"),
    # Groups on function-keys
    Group(
        name="f1",
        label="",
        matches=[Match(wm_class=re.compile(r"^(firefox)$"))],
    ),
    Group(
        name="f2",
        label="",
        matches=[Match(wm_class="discord")],
    ),
    Group(
        name="f3",
        label="",
        matches=[Match(wm_class=re.compile(r"^(joplin)$"))],
    ),
    Group(
        name="f4",
        label=" ",
        matches=[Match(wm_class=re.compile(r"^(com.github.th_ch.youtube_music)$"))],
    ),
    Group(
        name="f5",
        label="󱦹",
        matches=[Match(wm_class="rnote")],
    ),
    Group(
        name="f6",
        label="󰟵",
        matches=[Match(wm_class="bitwarden")],
    ),
    Group(
        name="f7",
        label=" 󰣀",
        matches=[Match(wm_class=re.compile(r"^(XPipe)$"))],
    ),
    Group(name="f8", label="󱊲"),
    Group(name="f9", label="󱊳"),
    Group(name="f10", label="󱊴"),
    Group(name="f11", label="󱊵"),
    Group(name="f12", label="󱊶"),
]

group_screen_map = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 2,
    "5": 2,
    "6": 2,
    "7": 1,
    "8": 1,
    "9": 1,
    "f1": 2,
    "f2": 1,
    "f3": 2,
    "f4": 1,
    "f5": 1,
    "f6": 1,
    "f7": 2,
    "f8": 0,
    "f9": 0,
    "f10": 0,
    "f11": 0,
    "f12": 0,
}


def go_to_group(name: str):
    def _inner(qtile):
        screen = group_screen_map.get(name, 0)
        if len(qtile.screens) <= 2:
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(screen)
            qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))


def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        screen = group_screen_map.get(name, 0)
        if len(qtile.screens) <= 2:
            qtile.current_window.togroup(name, switch_group=False)
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(screen)
            qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.append(
        Key([mod, "shift"], i.name, lazy.function(go_to_group_and_move_window(i.name)))
    )

for i in range(1, 12):
    group_name = f"f{i}"
    key = f"F{i}"
    keys.append

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty",
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.25,
                opacity=1,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "calc",
                "qalculate-gtk",
                width=0.3,
                height=0.6,
                x=0.35,
                y=0.2,
                opacity=1,
                on_focus_lost_hide=False,
            ),
        ],
    )
)
