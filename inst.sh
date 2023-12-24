#!/bin/bash


# Scelgo nome e location della directory d'installazione e la creo.
# Volendo installare l'applicazione a livello di sistema qui è stato scelto di creare la nuova cartella in /usr/local/bin, questo richiede privilegi root, per questo i comandi sono preceduti da sudo.

INSTALL_DIR="/usr/local/bin/nemo_inst"

sudo mkdir -p $INSTALL_DIR

# Copio il programma e lo script di esecuzione nella nuova cartella e attribuisco i permessi di esecuzione.

sudo cp nemo_2.py $INSTALL_DIR
sudo cp start.sh $INSTALL_DIR

sudo chmod +x $INSTALL_DIR/nemo_2.py
sudo chmod +x $INSTALL_DIR/start.sh


# Aggiungo la cartella d'installazione al PATH e al PYTHONPATH e applico le modifiche a partire dalla shell corrente.

echo "export PATH=\$PATH:$INSTALL_DIR" | sudo tee -a /etc/profile
echo "export PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR" | sudo tee -a /etc/profile

source /etc/profile
source ~/.bashrc

echo "Installazione completata. Per lanciare l'applicazione è sufficiente dare il comando start.sh da qualunque location del terminale."

