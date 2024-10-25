# Arch Linux Qtile Desktop

Thats my very first full desktop configuration of Arch Linux. With this I learned how to  set everything I need up.

So this repo kind of is my journey of exploring my needs and preferences in applications I want to use.
I had trouble to find dotfiles, where multiple monitors are already configured. So here is one...


## Qtile

Well i have looked through some window managers and finally decided to use qtile. 

**Why?** Look at the [documentation](https://docs.qtile.org/en/latest/) yourself it is incredible! It is super configurable out of the box but has a huge expansion with [qtile-extras](https://qtile-extras.readthedocs.io/en/latest/).

**How** I divided my configuration in separate files. The main configuration lives in the very top. Thats the file where everything gets imported into. 

In the first directory "`helper`" I put every helper script.

The second directory, "`modules`" contains everything qtile related and its different sections like screens, keys, groups and hooks. 


### Applications

I try to only install GUI apps which are based on Qt. I just like it more than GTK based applications. 

