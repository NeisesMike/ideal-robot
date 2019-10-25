# grab a list of all the installed programs
sudo apt-key add ~/Repo.keys
sudo cp -R ~/sources.list* /etc/apt/
sudo apt-get update
sudo apt-get install dselect
sudo dselect update

## ensure dpkg is updated
apt-cache dumpavail > ~/temp_avail
sudo dpkg --merge-avail ~/temp_avail
rm ~/temp_avail

sudo dpkg --set-selections < ~/Package.list
sudo apt-get dselect-upgrade -y

# copy the entire home directory away
rsync -r --progress /home/michael /media/michael/My\ Passport

