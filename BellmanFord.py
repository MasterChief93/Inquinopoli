__author__ = 'Federico'
# -*- coding: utf-8 -*-

def BellmanFord(G, list):
    # Inizializzazione dizionari
    qcity = dict()
    Distance = dict()

    # Impostazione dei valori come None
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
    Distance[1] = 0
    for i in range(1, len(G.cities) - 1):
        for elem in archi:
            if Distance[elem.par] != float("+inf") and Distance[elem.arr] > Distance[elem.par] + elem.peso:
                Distance[elem.arr] = Distance[elem.par] + elem.peso
                if elem.arr in list and Distance[elem.arr] < 3:
                    qcity[elem.arr] = 0

    # Aggiustamento valori in qlist
    for elem in list:
        if qcity[elem] != 0:
            qcity[elem] = Distance[elem]

    # Secondo passata di Bellman/Ford
    for elem in archi:
        if Distance[elem.par] != float("+inf") and Distance[elem.arr] > Distance[elem.par] + elem.peso:
            Distance[elem.arr] = Distance[elem.par] + elem.peso
            if elem.arr in list and Distance[elem.arr] < 3:
                qcity[elem.arr] = 0

    # Restituzione dati ottenuti
    for elem in qcity:
        #print "Nodo: " + str(elem) + " --> Costo: " + str(qcity[elem])
        print qcity[elem]  if qcity[elem] >= 0 and qcity[elem] != float("+inf") else "?"
