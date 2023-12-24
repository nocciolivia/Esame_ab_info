#!/bin/bash

# Scarico il file con wget dal link fornito e estraggo il nome con basename.

file_url="https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat"

file_name=$(basename "$file_url")

wget "$file_url" -O "$file_name"

# Controllo che il download sia avvenuto correttamente.

if [ $? -eq 0 ]
  then
    echo "Download avvenuto correttamente. File salvato come $file_name."
  else
    echo "Download non avvenuto correttamente."
fi

# Lancio il programma python nemo_2.py dandogli il input il nome del file da cui estrarre i dati.

#python3 ./nemo_2.py "$file_name"
python /usr/local/bin/nemo_inst/nemo_2.py "$file_name"  # Il programma python si trova nella cartella d'installazione in /usr/local/bin.
