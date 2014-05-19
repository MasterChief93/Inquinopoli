__author__ = 'Federico & Fabrizio'
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
    arcs = []
    for node in G.nodes:
        Distance[node] = float("+inf")
        if node in G.arcs:
            for arc in G.arcs[node]:
                arcs.append(arc)


    # Prima passata di Bellman/Ford
    belford_first = time()
    Distance[1] = 0
    #for i in range(0, len(G.cities) - 1):
    for elem in arcs:
        if Distance[elem.dep] != float("+inf") and Distance[elem.arr] > Distance[elem.dep] + elem.weight:
            Distance[elem.arr] = Distance[elem.dep] + elem.weight
            if elem.arr in list and Distance[elem.arr] < 3:
                qcity[elem.arr] = 0
    print "Prima passata Bellman/Ford in: ", time() - belford_first, "con ", len(G.arcs), "nodi e ", len(arcs), "archi"

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
    print "Seconda passata Bellman/Ford in: ", time() - belford_sec

    # Restituzione dati ottenuti
    print Distance
    for elem in qcity:
        #print "Nodo: " + str(elem) + " --> Costo: " + str(qcity[elem])
        #print Distance
        print qcity[elem] if qcity[elem] >= 0 and qcity[elem] != float("+inf") else "?"

    print "Tempo totale : ", time() - init
