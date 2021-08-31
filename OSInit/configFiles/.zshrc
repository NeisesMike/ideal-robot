
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH="$HOME/.local/bin:$HOME/bin:$PATH"

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

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="dd.mm.yyyy"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

source ~/.zsh_aliases

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

eval "$(ssh-agent -s)" > /dev/null

# disable beep
# why would anyone ever want this
unsetopt BEEP


