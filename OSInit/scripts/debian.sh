#do some updates
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install cmus git i3 vim zsh

#get oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

#set zsh as the default shell
chsh -s $(which zsh)

#create a projects directory
mkdir ~/Documents/projects && cd ~/Documents/projects

#clone ideal-robot into the projects directory
git clone https://github.com/neisesMike/ideal-robot.git
export ideal=~/Documents/projects/ideal

#copy config files
cd ${ideal}'/OSInit/configFiles' && cp -r .gitconfig .i3 .vimrc .zshrc ~/

#copy music
cd ${ideal}'/OSInit/tunes' && cp -r * ~/Music/

#get summa dat yung reboot action
#sudo reboot
