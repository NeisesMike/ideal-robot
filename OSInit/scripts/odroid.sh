#!/bin/bash

#==
#==
#==

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


