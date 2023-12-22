#!/bin/bash

# Scarico il file con wget dal link fornito e estraggo il nome con basename.

file_url="https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat"

file_name=$(basename "$file_url")

wget "$file_url" -O "$file_name"

# Controllo che il download sia avvenuto correttamente.

if [ $? -eq 0 ]
  then
    echo "Download successful. File saved as $file_name."
  else
    echo "Download not succesfull."
fi

# Lancio il programma python Nemo_2.py dandogli il input il nome del file da cui estrarre i dati. Allo stesso modo potrei far leggere in questo modo anche i file degli intervalli d'età.

python3 nemo_2.py "$file_name"




################## Add helpppppppp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




######  Posso aggiungere che lo salvi nella directory in cui si trova il file python oppure posso fare si che il file python lo vada a ppescare cercandolo fra le cartelle




pwd

echo$? 
$? = Return status


read envireonmental variable to acquire the path and make the application indipendent from location
