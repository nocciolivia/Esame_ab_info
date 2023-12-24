# Il programma produce i grafici richiesti suddividendo i punti in base all'età.
# Fornisco da file i limiti dei bin d'età e il programma li smista di conseguenza.
# I grafici prodotti sono 1) Diagramma colore-magnitudine, 2) Istogramma delle metallicità, 3) Metallicità in funzione della massa iniziale. I grafici 2) e 3) vengono fatti seguendo la stessa suddivisione in intervalli d'età, in generale diversa da quella utilizzata per il grafico 1).

import numpy as np
import matplotlib.pyplot as plt
import sys

colormap = plt.cm.gnuplot2
colormap1 = plt.cm.Pastel1


# --------------------- Import dei dati da file ---------------------------

# Importo i dati da file e li riordino disponendoli in modo che le età (age_parent) siano in ordine crescente, sfruttando argsort().
# Dopo aver riordinato faccio unpacking dei dati delle 5 colonne.


#data_file = "Nemo_6670.dat"
data_file = sys.argv[1]     # Per leggere il nome del file come command-line argument (così posso fornirlo dallo script).

data = np.loadtxt(data_file, delimiter = ' ' , usecols = (0,1,4,8,12), unpack = True)

data = data.T
sorted_data = data[data[:, 4].argsort()]
sorted_data = sorted_data.T


MsuH = sorted_data[0]
m_ini = sorted_data[1]
M_ass = sorted_data[2]
b_y = sorted_data[3]
age_parent = sorted_data[4]




# ----------------------------- FIGURA 1 ------------------------------------------

# Il programma indica il range d'eta in cui fornire gli intervalli, individuando le età max e min del campione e chiede il nome del file su cui sono scritti gli intervalli.


max_age = np.max(age_parent)
min_age = np.min(age_parent)


print('')
print('---------- FIGURA 1 - Diagramma colore-magnitudine ----------')
print('')
print('Inserire il nome del file contenente i limiti per i bin di età per la prima figura. I valori min = {0:.2f} e max = {1:.2f} del campione devono essere inclusi.' .format(min_age, max_age))
bin_data_1 = input()
print('-------------------------------------------------------------')


age1 = np.loadtxt(bin_data_1, unpack=True)




# Per ognuno degli intervalli scelti il programma produce il grafico di M_ass vs. b-y con colore e label diversa per ogni intervallo.
# Aver riordinato i dati all'inizio permette di evitare un secondo ciclo for (sugli indici di M_ass e b-y associati alle età che rientrano in ciascun intervallo), questo permette di risparmiare diversi secondi.

# Con un ciclo for sul numero degli intervalli si cercano con np.where i punti che ricadano nello specifico intervallo, creando un'array di indici (che sono consecutivi perchè i dati sono stati riordinati per età). Per ogni set di indici individuato (cioè per ogni set di punti in un determinato intervallo d'età) si produce il grafico richiesto. Tutti i plot vengono stampati sullo stesso grafico.
# Dato che i punti sono ordinati, per produrre il grafico posso semplicemente dire di graficare i punti dal primo indice contenuto in index1 all'ultimo, evitando un ciclo for sugli indici contenuti in index1.


f1 = plt.figure(1)

num_int = len(age1) - 1

for i in range(1,len(age1)):
    
    s1 = age1[i] - age1[i-1]
    
    index1 = np.where((age1[i]-age_parent >= 0) & (age1[i]-age_parent < s1))[0]
    
    if(len(index1) == 0):
        print('Nessun punto nell intervallo {0:.2f} Gyr - {1:.2f} Gyr' .format(age1[i-1], age1[i]))
        print('-------------------------------------------------------------')
        
    else:
    
        plt.scatter(b_y[index1[0]:index1[-1]], M_ass[index1[0]:index1[-1]], marker = '.', s = 1, color = colormap(i/len(age1)), label = '{0:.2f} Gyr - {1:.2f} Gyr' .format(age1[i-1], age1[i]))



# Altre caratteristiche del grafico.

plt.ylim(8.7,-4)
plt.xlim(-0.1,1.0)
plt.xlabel('b-y')
plt.ylabel('M_v')
plt.rc("legend", fontsize=5)
plt.legend(markerscale = 5.0)




#-------------------------------- FIGURA 2 --------------------------------

# Il programma indica il range d'eta in cui fornire gli intervalli, individuando le età max e min del campione e chiede il nome del file su cui sono scritti gli intervalli.


print('')
print('---------- FIGURA 2 - Istogramma della metallicità e metallicità vs. massa iniziale ----------')
print('')

print('Inserire il nome del file contenente i limiti per i bin di età per la seconda figura (i due grafici vengono fatti sulla stessa suddivisione per età). I valori min = {0:.2f} e max = {1:.2f} del campione devono essere inclusi.' .format(min_age, max_age))
bin_data_2 = input()


age2 = np.loadtxt(bin_data_2, unpack=True)

n_bins = 10                  # Qui viene scelto il numero di bin per ciascun istogramma.



f2 = plt.figure(2)

kwargs = dict(alpha=0.5)


# Gli intervalli in età vengono individuati come per il primo grafico e vengono graficati tutti i punti nello stesso intervallo. Qui una volta individuato l'intervallo vengono fatti sia l'istogramma delle metallicità, sia il grafico della metallicità in funzione della massa iniziale, con colore diverso per ognuna delle popolazioni nei diversi bin d'età.
# I grafici sono separati (come due subplot della stessa figura) ma fatti sullo stesso campione (con la stessa divisione negli intervalli di età).


for j in range(1,len(age2)):
    
    s2 = age2[j] - age2[j-1]
    index2 = np.where((age2[j]-age_parent >= 0) & (age2[j]-age_parent < s2))[0]
    
    if(len(index2) == 0):
        print('Nessun punto nell intervallo {0:.2f} Gyr - {1:.2f} Gyr' .format(age2[j-1], age2[j]))
        print('-------------------------------------------------------------')
        
    else:
    
        mean = np.mean(MsuH[index2[0]:index2[-1]])
        median = np.median(MsuH[index2[0]:index2[-1]])
        
        plt.subplot(1,2,1)   # Istogramma delle metallicità
        
        plt.hist(MsuH[index2[0]:index2[-1]], histtype = 'bar', color = colormap(j/len(age2)), label = '{0:.2f} Gyr - {1:.2f} Gyr' .format(age2[j-1], age2[j]), **kwargs)
        plt.axvline(mean, color = colormap(j/len(age2)), linestyle = 'solid', **kwargs)
        plt.axvline(median, color = colormap(j/len(age2)), linestyle = 'dashed', **kwargs)


        plt.subplot(1,2,2)   # Grafico metallicità vs. massa iniziale
        
        plt.scatter(m_ini[index2[0]:index2[-1]], MsuH[index2[0]:index2[-1]], marker ='.', s=3, color = colormap(j/len(age2)), label = '{0:.2f} Gyr - {1:.2f} Gyr' .format(age2[j-1], age2[j]))



# Altre caratteristiche della figura due, per ognuno dei due subplot.

plt.tight_layout()


plt.subplot(1,2,1)

plt.plot([], [], ' ', label=' Solid line = mean\n Dashed line = median')

plt.xlabel('MsuH')
plt.ylabel('counts')
plt.rc("legend", fontsize=5)
plt.legend(markerscale = 5.0)


plt.subplot(1,2,2)

plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
plt.xlabel('m_ini')
plt.ylabel('MsuH')
plt.rc("legend", fontsize=5)
plt.legend(markerscale = 5.0)



plt.show()
