#!/bin/bash

sed -n '/Key(/p' ~/dotfiles/.config/qtile/keys.py | \
sed -E 's/Key\(\[(.*)\], "(.*)", lazy\..*, desc="(.*)"\)/\1 + \2 -> \3/' | \
sed -E 's/\[//g; s/\]//g; s/, / + /g' | \
grep -v '# ' | \
sed -e 's/"//g' -e 's/,//g'



read -p "Press [Enter] to exit..."
