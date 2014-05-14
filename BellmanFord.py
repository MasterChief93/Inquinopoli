__author__ = 'Federico'
# -*- coding: utf-8 -*-
from time import time


def BellmanFord(G, list):
    # Inizializzazione dizionari
    qcity = dict()
    Distance = dict()

    # Impostazione dei valori come None
    init = time()
    for elem in list:
        qcity[elem] = None

    # Aggiunta di tutti gli archi in un array
    archi = []
    for citta in G.cities:
        Distance[citta] = float("+inf")
        if citta in G.streets:
            for street in G.streets[citta]:
                archi.append(street)


    # Prima passata di Bellman/Ford
    belford_first = time()
    Distance[1] = 0
    #for i in range(0, len(G.cities) - 1):
    for elem in archi:
        if Distance[elem.par] != float("+inf") and Distance[elem.arr] > Distance[elem.par] + elem.peso:
            Distance[elem.arr] = Distance[elem.par] + elem.peso
            if elem.arr in list and Distance[elem.arr] < 3:
                qcity[elem.arr] = 0
    print "Prima passata Bellman/Ford in: ", time() - belford_first, "con ", len(G.streets), "nodi e ", len(
        archi), "archi"

    # Aggiustamento valori in qlist
    for elem in list:
        if qcity[elem] != 0:
            qcity[elem] = Distance[elem]

    # Secondo passata di Bellman/Ford
    belford_sec = time()
    for elem in archi:
        if Distance[elem.par] != float("+inf") and Distance[elem.arr] > Distance[elem.par] + elem.peso:
            Distance[elem.arr] = Distance[elem.par] + elem.peso
            if elem.arr in list and Distance[elem.arr] < 3:
                qcity[elem.arr] = 0
    print "Seconda passata Bellman/Ford in: ", time() - belford_sec

    # Restituzione dati ottenuti
    print Distance
    for elem in qcity:
        #print "Nodo: " + str(elem) + " --> Costo: " + str(qcity[elem])
        #print Distance
        print qcity[elem]  if qcity[elem] >= 0 and qcity[elem] != float("+inf") else "?"

    print "Tempo totale : ", time() - init