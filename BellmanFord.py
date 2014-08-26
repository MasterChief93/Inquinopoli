# -*- coding: utf-8 -*-
from time import time


def BellmanFord(G, list, casenumb):
    """
    Funzone atta a calcolare i costi dei percorsi dal primo nodo ai nodi presenti nella query. Il grafo, i nodi e gli
    archi sono inizializzati come classi, mentre i costi relativi ai nodi e le query sono inizializzati come dizionari.
    Il calcolo viene svolto tramite l'algoritmo di Bellman-Ford, al quale viene aggiunta un'ulteriore passata per ovviare
    al problema dei cicli negativi. La funzione restituisce infine i costi dei nodi presenti nel dizionario qcity.
    @param casenumb: int; numero del caso in esame
    @param G: istanza della classe Graph
    @param list: list; lista di interi rappresentanti le query
    @return: outlist: list; lista contenente il numero del caso in esame e i costi delle relative query
    """

    # Inizializzazione dizionari

    global tot,bel1,bel2
    tot=0
    bel1=0
    bel2=0
    bellstart=time()
    qcity = dict()        # dizionario contenente le query
    Distance = dict()     # dizionario contenente i costi di tutti i nodi del grafo a partire dal nodo di indice 1

    # Assegnazione del valore None agli elementi di qcity

    for elem in list:
        qcity[elem] = None

    # Inizializzazione lista "arcs", contenente tutti gli archi del grafo, e inizializzazione di tutte le distanze a +∞

    arcs = []
    for node in G.nodes:
        Distance[node] = float("+inf")
        if node in G.arcs:
            for arc in G.arcs[node]:
                arcs.append(arc)

    # Prima passata di Bellman-Ford

    belford_first = time()
    Distance[1] = 0              # Partendo sempre dal nodo di indice 1 il suo costo sarà sempre uguale a 0

    # Classico Bellman-Ford

    algtime=time()
    for node in G.nodes:
        for elem in arcs:
            if Distance[elem.dep] != float("+inf") and Distance[elem.arr] > Distance[elem.dep] + elem.weight:
                Distance[elem.arr] = Distance[elem.dep] + elem.weight
                if elem.arr in list and Distance[elem.arr] < 3:
                    qcity[elem.arr] = 0
    bel1 += time() - belford_first
    #print "Prima passata Bellman/Ford in: ", time() - belford_first, "con ", len(G.arcs), "nodi e ", len(arcs), "archi"

    # Aggiustamento valori in qlist

    for elem in list:
        if qcity[elem] != 0:
            qcity[elem] = Distance[elem]

    # Secondo passata di Bellman/Ford
    belford_sec = time()
    for elem in arcs:
        if Distance[elem.dep] != float("+inf") and Distance[elem.arr] > Distance[elem.dep] + elem.weight:
            Distance[elem.arr] = Distance[elem.dep] + elem.weight
            if elem.arr in list and Distance[elem.arr] < 3:
                qcity[elem.arr] = 0
    global bubba
    bubba=time()-algtime
    print "Esplorato e Risolto in",bubba,"s"
    bel2+= time() - belford_sec
    #print "Seconda passata Bellman/Ford in: ", time() - belford_sec

    # Restituzione dati ottenuti
    #print Distance
    outlist=[casenumb]         # Inizializzazione lista "outlist": tale lista tiene in memoria i dai da stampare successivamente per ogni caso di test
    for elem in qcity:         # Ciclo che popola la lista "outlist" con le query del caso
        #print qcity[elem] if qcity[elem] >= 0 and qcity[elem] != float("+inf") else "?"
        if qcity[elem] == float("+inf"):
            qcity[elem] = "?"
        outlist.append(qcity[elem])
    tot+= time() - bellstart
    #print "Tempo totale : ", time() - bellstart
    return outlist
