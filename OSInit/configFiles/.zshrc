# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH="$HOME/bin:$PATH"

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
    common-aliases
    git
    history
    #httpie
    last-working-dir
    pip
    sudo
    wd
)

# load zsh
source $ZSH/oh-my-zsh.sh

# sel4 exports
#export SEL4_COMMON=$HOME/Documents/projects/sel4tuts/projects/tools/common-tool
#export SOURCE_DIR=$HOME/Documents/projects/sel4tuts
#export srctree=$HOME/Documents/projects/sel4tuts

#export sel4 common path

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

