#!/bin/sh
xrandr --newmode "2560x1440"  808.75  2560 2792 3072 3584  1440 1443 1448 1568 -hsync +vsync

xrandr --addmode DisplayPort-0 "2560x1440"

xrandr --output DisplayPort-0 --primary --mode 2560x1440 --pos 1920x0 --rotate normal --output DisplayPort-1 --mode 1920x1080 --pos 4480x180 --rotate normal --output DisplayPort-2 --off --output HDMI-A-0 --mode 1920x1080 --pos 0x180 --rotate normal
