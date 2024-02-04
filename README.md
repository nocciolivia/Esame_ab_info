
----- INSTALLAZIONE ED ESECUZIONE -----

Copiare la repository sul dispositivo con

    git clone https://github.com/nocciolivia/Esame_ab_info.git
  
Entrare nella directory 'Esame_ab_info' e lanciare lo script di installazione con

    source inst.sh

in modo che le modifiche vengano applicate alla shell corrente.
Seguire eventuali istruzioni a schermo (potrebbe essere richiesta la password dell'utente dato che con l'installazione viene modificato il path di sistema).
A fine installazione verrà visualizzato il messaggio 'Installazione completata', insieme al comando da utilizzare per lanciare l'applicazione.

Dopo l'installazione l'applicazione potrà essere lanciata da ogni location del terminale tramite il comando start.sh.
Per il programma seguire le informazioni a schermo e vedere 'Descrizione dell'applicazione'.



----- DESCRIZIONE DELL'APPLICAZIONE -----

L'applicazione è costituita dal programma python 'nemo_2.py' e dal suo script di esecuzione 'start.sh'.

-------------------------------------------------------------------

'nemo_2.py' ---> INPUT: File di testo contenenti gli estremi per la suddivisione in intervalli di età (vedi dopo);
                 OUTPUT: Figure 1,2 (vedi dopo).

'nemo_2.py' legge i dati necessari dal file 'Nemo_6670.dat' e realizza due figure:

    FIGURA 1 - Contiene il diagramma colore-magnitudine;
    FIGURA 2 - Contiene l'istogramma delle metallicità e il grafico della metallicità in funzione della massa iniziale come due subplot della stessa figura.

I dati usati per i tre grafici vengono inoltre suddivisi in intervalli d'età; i punti associati a ciascun intervallo sono colorati ed etichettati in modo diverso.

Gli estremi degli intervalli per realizzare questa suddivisione devono essere scritti in un file di testo, il cui nome viene richiesto in input dal programma.
Il programma permette di utilizzare due file di testo separati (e quindi due suddivisioni diverse in bin d'età) per realizzare le figure 1 e 2.
I due grafici della figura 2 vengono realizzati sulla stessa suddivisione in età.

Le figure così prodotte vengono infine mostrate a schermo.

----------------------------
NOTA: Se necessario possono essere scaricati i file di testo 'bin.txt' e 'bin1.txt', che contengono degli intervalli in età pre-preparati e che possono essere modificati all'occorrenza (si consiglia in particolare di utilizzare 'bin.txt' per la figura 1 e 'bin1.txt' per la figura 2). Questi sono disponibili ai link

  https://github.com/nocciolivia/Age_bins/blob/main/bin.txt
  
  https://github.com/nocciolivia/Age_bins/blob/main/bin1.txt
  
----------------------------

Lo script 'start.sh' scarica il file 'Nemo_6670.dat' da github (salvandolo nella directory corrente) e questo viene passato al programma 'nemo_2.py'; dopodichè esegue 'nemo_2.py'.

----------------------------

Per ulteriori dettagli sul funzionamento si può fare riferimento direttamente agli script.
