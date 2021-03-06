
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH="$HOME/.local/bin:$HOME/bin:$PATH"
#export PYTHONHOME=/home/michael/.miniconda3

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
#ZSH_THEME="robbyrussell"
ZSH_THEME="wedisagree"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
    common-aliases
    emoji
    git
    #globalias
    history
    last-working-dir
    nmap
    pip
    sudo
    wd
)

# load zsh
source $ZSH/oh-my-zsh.sh

#lenovo ideapad y500 -> enable tap = mouse click
#synclient TapButton1=1 TapButton2=3 TapButton3=2

# OPAM configuration
. /home/$USER/.opam/opam-init/init.zsh > /dev/null 2> /dev/null || true

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="dd.mm.yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

source ~/.zsh_aliases

#eval $(thefuck --alias)

# connect to home wifi
#sudo ifconfig wlp4s0 up
#sudo dhclient wlp4s0

sshpi(){
    ssh pi@192.168.1."$1"
}

sshpireset(){
    ssh-keygen -f "/home/michael/.ssh/known_hosts" -R 192.168.1."$1"
    sshpi "$1"
}

# find a way to put this back into .profile
synclient TapButton1=1 TapButton2=3 TapButton3=2

eval "$(ssh-agent -s)" > /dev/null

# conda into path
export PATH="$PATH:$HOME/.miniconda3/bin"

# disable beep
# why would anyone ever want this
unsetopt BEEP

# cross compiler for odroid xu4
export CROSS_COMPILE="arm-linux-gnueabi-"

# Hol and cake into path
export PATH="$PATH:$HOME/Documents/projects/cake_hol_poly/HOL/bin"
export PATH="$PATH:$HOME/Documents/projects/cake_hol_poly/"
export CAKEML_DIR="$HOME/Documents/projects/cake_hol_poly/cakeml"

