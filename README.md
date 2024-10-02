# Arch Linux Qtile Desktop

Thats my very first full desktop configuration of Arch Linux. With this I learned how to  set everything I need up.

So this repo kind of is my journey of exploring my needs and preferences which i will make clear, also i try to make it as noob friendly as possible and explain over time how my dotfiles work.

My biggest issues were the handling with multiple monitors which is why i wont ever make this repo in a single screen config!
Maybe somebody can just copy my config and learn from it even if im by far no programmer so some solutions might be not as good as someone with more experience might suggests. Maybe someday someone will find this useful.

## Qtile

Well i have looked through some window managers and finally decided to use qtile. 

**Why?** Look at the [documentation](https://docs.qtile.org/en/latest/) yourself it is incredible! I also looked into Distro Tubes Qtile videos which helped me a lot to understand how it works. It is super configurable out of the box but has a huge expansion with [qtile-extras](https://qtile-extras.readthedocs.io/en/latest/) which i also used to make this beautiful desktop for myself.

**How** I devided my configuration in seperate files. The main configuration lives in the very top. Thats the file where everything gets imported into at one point. 

In the first directory named "helper" I put everything I need, from autostart over the script to display keybindings.

The second directory contains everything qtile related and its different sections like screens, keys, groups and hooks. 

I made this out of preference like this, I don´t like to scroll for ages to find a section. Because if you take a look into the screens.py you will see that this file is already pretty long. So to enable me to find everything easily I splitted my configuration. Something I recommend.

### Applications

For GUI-Apps I opt for Qt based once since I simply like it.

I choose dunst for notifications and picom as a compositor, basically the default for almost everyone...

I use nitrogen to set the wallpaper and soon setting a wallpaper also changes the color scheme of the desktop.

As shell i use zsh, based on [this](https://youtu.be/y6XCebnB9gs?si=tkho-EFBMfcOKPEu) video with minor tweaks. I also used his [ohmyposh video](https://youtu.be/9U8LCjuQzdc?si=nkDru-NK5QHiGTo3) and for now just copied his configuration. I also seperated the aliases into an .aliases file for the reason below...

*Some day I will upload a dedicated zsh repo for remote ssh machines.*  

Under the hood works pywal to change the theme of the terminal. In my case alacritty where I tested it and it works. *Maybe I will add verification about other terminals too.*


