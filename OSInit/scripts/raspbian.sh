#== Michael Neises
#== 18 november 18
#== set the system up so that it isn't totally ugly

#get zsh and set it as the default shell
##we do this here so that all password requests are grouped at the beginning
sudo apt-get -y install zsh
chsh -s $(which zsh)

#do some updates
sudo apt-get update && sudo apt-get upgrade
sudo apt-get -y install git vim python-pip python-rpi.gpio
sudo apt-get autoclean; sudo apt-get autoremove

#get oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

#create a projects directory
mkdir ~/Documents/projects

#clone ideal-robot into the projects directory
cd ~/Documents/projects && git clone https://github.com/neisesMike/ideal-robot.git
export ideal=$HOME/Documents/projects/ideal-robot

#copy config files
chmod o+x ${ideal}/OSInit/configFiles
cd ${ideal}/OSInit/configFiles && cp -r .gitconfig .vimrc .zshrc ~/

#output some congratulatory message

echo "  ________                 .___       "
echo " /  _____/  ____  __ __  __| _/____   "
echo "/   \  ___ /  _ \|  |  \/ __ |\__  \  "
echo "\    \_\  (  <_> )  |  / /_/ | / __ \_"
echo " \______  /\____/|____/\____ |(____  /"
echo "        \/                  \/     \/ "
echo "             __               __ "
echo "            / _)             / _)"
echo "     .-^^^-/ /        .-^^^-/ /  "
echo "  __/       /      __/       /   "
echo " <__.|_|-|_|      <__.|_|-|_|    "
echo "                                 "
echo "===================================================="
echo "Please verify the configuration options in ~/.zshrc!"
echo "===================================================="

