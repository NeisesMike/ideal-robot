#!/bin/bash

#== Michael Neises
#== 26/4/18
#== set up the odroid xu4 such that it can build the sel4 kernel

#run debian.sh
source debian.sh

#install research libraries
sudo apt-get install haskell-platform python-pip

#install opam
wget https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh -O - | s h -s /user/local/bin

#install coq
opam repo add coq-released https://coq.inria.fr/opam/released
opam pin add coq 'opam show --field=version coq'
opam update
opam upgrade

#install Repo
mkdir $HOME/bin
PATH=$HOME/bin:$PATH
curl https://storage.googleapis.com/git-repo-downloads/repo > $HOME/bin/repo
chmod a+x $HOME/bin/repo

#make a sel4tuts directory
mkdir $HOME/Documents/projects/sel4tuts

#get the sel4tuts
cd $HOME/Documents/projects/sel4tuts && repo init -u https://github.com/SEL4PROJ/sel4-tutorials-manifest -m sel4-tutorials.xml && repo sync


