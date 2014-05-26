# -*- coding: utf-8 -*-
from random import randrange, seed, sample
from time import time


def Generatore():
    """
    Funzione atta a scrivere un file di input sotto le opportune condizioni richeste dal progetto stesso
    """

    file = open("input2.txt", "w") # Apertura del file
    test = randrange(1, 50)        # Generazione casuale del numero di test da effettuare mediante la funzione randrange della libreria random di Python
    file.write(str(test) + "\n\n") # Scrittura sul file di input : la prima riga conterrà sempre il numero di test da effettuare, seguita da una riga vuota

    for i in range(0, test):       # Ciclo che scrive sul file di input un caso random per ogni test

        seed(time() + i)           # Randomizzazione del seed per la libreria random
        n = randrange(2, 200)      # Generazione casuale del numero di nodi presenti nel grafo del singolo caso in esame
        file.write(str(n) + "\n")  # Scrittura del numero di nodi sul file di input e successivo cambo di riga

        for p in range(0, n):      # Ciclo che assegna ad ogni nodo un relativo tasso di inquinamento

            randpol = randrange(1, 20) # Generazione casuale del tasso di inquinamento. randpol : Random Pollution
            file.write(str(randpol) + " ") # Scrittura dei tassi di inquinamento sul file di input

        file.write("\n") # Finito di scrivere la riga dei tassi di inquinamento si passa alla riga successiva
        arclist = []     # Inizializzazione lista : arclist conterrà tutti gli archi possibili del grafo del singolo caso in esame

        for i in range(1, n + 1):                   # Popolamento della lista arclist mediante due cicli for
            for j in range(1, n + 1):
                if i != j:
                    arclist.append([i, j])

        m = randrange(0, n * (n - 1))               # Generazione casuale del numero di archi presenti nel grafo del singolo caso in esame
        final_arclist = sample(arclist, m)          # La lista final_arclist viene popolata con m elementi casuali della lista arclist grazie alla funzione sample della libreria random di Python
        file.write(str(len(arclist)) + "\n")        # Scrittura sul file di input del numero di archi presenti nel grafo del caso in esame

        for arc in arclist:                         # Ciclo che scrive sul file di input tutti gli archi del grafo del caso in esame
            file.write(str(arc[0]) + " " + str(arc[1]) + "\n")

        q = randrange(1, n)                         # Generazione casuale del numero q di query del caso in esame
        file.write(str(q) + "\n")                   # Scrittura sul file di input del numero di query del caso in esame
        qlist = []                                  # Creazione della lista qlist, lista atta a contenere le query del caso in esame

        while len(qlist) < q:                       # Ciclo che popola la lista qlist con q elementi di valore intero qn

            qn = randrange(2, n)                    # Il nodo 1 non fa mai parte della lista delle query essendo il nodo di partenza, 2 < "qn" < n
            if qn not in qlist:                     # Se qn, rappresentante l'indice del nodo da aggiungere alla lista delle query, non è già presente in qlist, la lista delle query, allora viene aggiunto
                file.write(str(qn) + "\n")          # Scrittura sul file di input della query generata casualmente
                qlist.append(qn)                    # Inserimento di qn nella lista qlist, necessario per poter uscire dal ciclo while

        file.write("\n")                            # Finite di scrivere le query sul file di input si passa alla riga successiva per scrivere, se presente, il caso successivo
    file.close()                                    # Finito di scrivere il file di input questo verrà chiusto per poi essere riaperto dalla funzione main()

if __name__ == "__main__":                          # Controllo atto a verificare se lo script viene eseguito direttamente o tramite importazione
    start=time()
    Generatore()
    print "Il generatore ha generato i casi di test in ",time()-start

