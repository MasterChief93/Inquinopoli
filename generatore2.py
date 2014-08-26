# -*- coding: utf-8 -*-
from random import randrange, seed, sample
from time import time


def Generatore(file,btest,bnode,barch,percentage):
    """
    Funzione atta a scrivere un file di input sotto le opportune condizioni richeste dal progetto stesso
    """

    test = randrange(1, 50) if btest == 0 else btest    # Generazione casuale del numero di test da effettuare mediante la funzione randrange della libreria random di Python
    print "Saranno generati e risolti " + str(test) + " casi di test"
    file.write(str(test) + "\n\n") # Scrittura sul file di input : la prima riga conterrà sempre il numero di test da effettuare, seguita da una riga vuota
    polav=0
    totalarcav=0
    arcstartav=0
    arcwriteav=0
    qav=0

    #for abdula in range(0,200):
    #    print "Sto eseguendo il gruppo di test numero ",abdula+1 abdulatrallallero
    for casetest in range(0, test):       # Ciclo che scrive sul file di input un caso random per ogni test


        seed(time() + casetest)           # Randomizzazione del seed per la libreria random
        n = randrange(2, 200) if bnode == 0 else bnode     # Generazione casuale del numero di nodi presenti nel grafo del singolo caso in esame
        file.write(str(n) + "\n")  # Scrittura del numero di nodi sul file di input e successivo cambo di riga

        #polstart=time()
        for p in range(0, n):      # Ciclo che assegna ad ogni nodo un relativo tasso di inquinamento

            randpol = randrange(1, 20) # Generazione casuale del tasso di inquinamento. randpol : Random Pollution
            file.write(str(randpol) + " ") # Scrittura dei tassi di inquinamento sul file di input
        #polav+=time()-polstart

        file.write("\n") # Finito di scrivere la riga dei tassi di inquinamento si passa alla riga successiva
        arclist = []     # Inizializzazione lista : arclist conterrà tutti gli archi possibili del grafo del singolo caso in esame

        #totalarcstaart=time()
        for i in range(1, n + 1):                   # Popolamento della lista arclist mediante due cicli for
            for j in range(1, n + 1):
                if i != j:
                    arclist.append([i, j])
        #totalarcav=time()-totalarcstaart

        #arcsstart=time()
        m = randrange(0, n * (n - 1)) if barch == 0 else barch      # Generazione casuale del numero di archi presenti nel grafo del singolo caso in esame
        density = m * (float(percentage)/100)
        density = density + 1 if density == 0 else density
        final_arclist = sample(arclist, int(density))          # La lista final_arclist viene popolata con m elementi casuali della lista arclist grazie alla funzione sample della libreria random di Python
        file.write(str(len(final_arclist)) + "\n")        # Scrittura sul file di input del numero di archi presenti nel grafo del caso in esame
        #arcstartav+=time()-arcsstart

        #arcwritestart=time()
        for arc in final_arclist:                         # Ciclo che scrive sul file di input tutti gli archi del grafo del caso in esame
            file.write(str(arc[0]) + " " + str(arc[1]) + "\n")
        #arcwriteav+=time()-arcwritestart

        if n==2:
            q=1
            file.write(str(q) + "\n")                   # Scrittura sul file di input del numero di query del caso in esame
            file.write("2"+"\n")
        else:
            q = randrange(1, n-1)                         # Generazione casuale del numero q di query del caso in esame
            file.write(str(q) + "\n")                   # Scrittura sul file di input del numero di query del caso in esame

        qlist = []                                  # Creazione della lista qlist, lista atta a contenere le query del caso in esame

        #qstart=time()
        if not n==2:

            while len(qlist) < q:                       # Ciclo che popola la lista qlist con q elementi di valore intero qn

                qn = randrange(2, n)                    # Il nodo 1 non fa mai parte della lista delle query essendo il nodo di partenza, 2 < "qn" < n
                if qn not in qlist:
                    if len(qlist) == q - 1 and casetest + 1 == test:
                        file.write(str(qn))          # Scrittura sul file di input della query generata casualmente
                    else:
                        file.write(str(qn) + "\n")
                    qlist.append(qn)                    # Inserimento di qn nella lista qlist, necessario per poter uscire dal ciclo while
            #qav+=time()-qstart

        #else:
        #    qlist=[2]
        if not casetest == test - 1:
            file.write("\n")                            # Finite di scrivere le query sul file di input si passa alla riga successiva per scrivere, se presente, il caso successivo

if __name__ == "__main__":                          # Controllo atto a verificare se lo script viene eseguito direttamente o tramite importazione
    start=time()
    Generatore()
    #print "Il generatore ha generato i casi di test in ",time()-start

