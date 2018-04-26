#== Michael Neises
#== 25/4/18
#== set my system up so that it isn't totally ugly

#do some updates
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install cmus git i3 vim zsh

#get oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

#set zsh as the default shell
chsh -s $(which zsh)

#create a projects directory
mkdir ~/Documents/projects

#clone ideal-robot into the projects directory
cd ~/Documents/projects && git clone https://github.com/neisesMike/ideal-robot.git
export ideal=$HOME/Documents/projects/ideal-robot

#copy config files
chmod o+x ${ideal}/OSInit/configFiles
cd ${ideal}/OSInit/configFiles && cp -r .gitconfig .i3 .vimrc .zshrc ~/

#copy music
cd ${ideal}/OSInit/tunes && cp -r * ~/Music/

#
echo "===================================================="
echo "Please verify the configuration options in ~/.zshrc!"
echo "===================================================="
echo ""
echo "===================================================="
echo "A reboot is necessary to load the window manager i3."
echo "===================================================="


