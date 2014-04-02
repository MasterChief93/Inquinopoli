__author__ = 'Federico'
# -*- coding: utf-8 -*-

def bellmanford(G, arr):
    Distance = dict()
    citta = G.cities
    Hit = dict()
    for strade in citta:
        Distance[strade] = float("+inf")
        Hit[strade] = 0
    Distance[1] = 0
    print Distance

    for city in G.streets:
        for street in G.streets[city]:
            if Distance[street.par] != float("+inf") and Distance[street.par] + street.peso <= Distance[street.arr]:
                Hit[street.par] += 1
                Hit[street.arr] += 1
                old = Distance[street.arr]
                Distance[street.arr] = Distance[street.par] + street.peso
                if Hit[street.arr] > 1 and Distance[street.arr] <= old:
                    if street.arr in G.streets:
                        for extra_street in G.streets[street.arr]:
                            Distance[extra_street.arr] = Distance[extra_street.par] + extra_street.peso
    print Hit
    if Distance[arr] < 3:
        print 0
    elif Distance[arr] == float("+inf"):
        print "?"
    else:
        print Distance[arr]

def bellmanford2(G, arr):
    Distance = dict()
    citta = G.cities
    Hit = dict()
    for strade in citta:
        Distance[strade] = float("+inf")
        Hit[strade] = 0
    Distance[1] = 0
    for city in G.streets:
        for street in G.streets[city]:
            if Distance[street.par] != float("+inf") and Distance[street.par] + street.peso <= Distance[street.arr]:
                Distance[street.arr] = Distance[street.par] + street.peso
    print Distance
    if Distance[arr] < 3:
        return 0
    elif Distance[arr] == float("+inf"):
        return "?"
    # if G.streets[arr] > 0:
    #     for street in G.streets[arr]:
    #         for strada in G.streets[street.arr]:
    #             if Distance[strada.par] + strada.peso <= Distance[strada.arr]:
    #                 Distance[strada.arr] = Distance[strada.par] + strada.peso
    #



def dfscyclerec(G,root):
    state = dict()                      #stesso funzionamento della visita generica
    for elem in G.cities:                     #ma al posto del set uso una lista e invece dell'add uso un insert alla posizione 0
        state[elem] = -1
    state[root] = 1
    Explored = []
    other = []
    s = [root]
    i = 0
    while len(s) > 0:
        elem = s.pop(0)
        Explored.append(elem)
        print s
        for street in G.streets[elem]:
            #state[street.arr] = 0
            if state[street.arr] != 1:
                state[street.arr] = 1
                s.append(street.arr)

            else:
                if street.arr in Explored and street.par in Explored and Explored.index(street.par) < Explored.index(street.arr):
                    other.append([street.par,street.arr])
    print other
    print Explored



