# Set the directory we want to store zinit and plugins
# for documentation see https://github.com/zdharma-continuum/zinit
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download Zinit, if it´s not there yet
[ ! -d $ZINIT_HOME ] && mkdir -p "$(dirname $ZINIT_HOME)"
[ ! -d $ZINIT_HOME/.git ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"

# Source/Load zinit
source "${ZINIT_HOME}/zinit.zsh"

# Oh-My_Posh promt
# For documentation see https://github.com/jandedobbeleer/oh-my-posh
eval "$(oh-my-posh init zsh --config ~/.config/ohmyposh/omp.toml)"


# Keybindings
bindkey -e
bindkey '^p' history-search-backward
bindkey '^n' history-search-forward


# Shell integrations
eval "$(fzf --zsh)"


# Add in zsh plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# Add in snippets
zinit snippet OMZP::command-not-found


# Load completions
autoload -U compinit && compinit

zinit cdreplay -q

# Completion styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'


# History 
HISTSIZE=50000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups


# Aliases
alias ls='ls -hl --color'
alias lsa='ls -ahl --color'
alias pacinst='sudo pacman -S'
alias pacup='sudo pacman -Syu'
alias deinst='yay -Rns'
alias ..='cd ..'
alias h='cd ~'
alias yayup='yay -Syu'
alias yayin='yay -S'
alias update='yay -Syu && sudo flatpak update'
alias mv='mv -i'
alias rm='rm -i'
alias gadd='git add'
alias gcom='git commit -m'
alias gp='git push'
alias gfet='git fetch'
alias tree='tree -C'


