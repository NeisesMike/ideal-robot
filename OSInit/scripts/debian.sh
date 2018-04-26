#== Michael Neises
#== 25/4/18
#== set the system up so that it isn't totally ugly

#get zsh and set it as the default shell
##we do this here so that all password requests are grouped at the beginning
sudo apt-get install zsh
chsh -s $(which zsh)

#do some updates
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install cmus git i3 vim
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
cd ${ideal}/OSInit/configFiles && cp -r .gitconfig .i3 .vimrc .zshrc ~/

#copy music
cd ${ideal}/OSInit/tunes && cp -r * ~/Music/

#output some congratulatory message

echo "              __ "
echo "             / _)"        
echo "      .-^^^-/ /  "       
echo "   __/       /   "          
echo "  <__.|_|-|_|    "         
echo "                 "
echo "===================================================="
echo "Please verify the configuration options in ~/.zshrc!"
echo "===================================================="
echo ""
echo "===================================================="
echo "A reboot is necessary to load the window manager i3."
echo "===================================================="


