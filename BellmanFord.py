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


def dfscyclerec(G, root):
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
                if street.arr in Explored and street.par in Explored and Explored.index(street.par) < Explored.index(
                        street.arr):
                    other.append([street.par, street.arr])
    print other
    print Explored


def Dfs():
    revarch = []
    nodelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    archlist = [[1,2],[1,3],[1,4],[2,3],[3,4],[2,5],[2,6],[2,1],[3,7],[7,6],[6,8],[5,8],[3,4],[4,8],[5,9],[9,10],[10,5],[10,9],[10,1]]
    Dict = dict()
    level=dict()
    ext1=[1]
    ext2=[]
    level[1]=0
    i=1
    for node in nodelist:
        Dict[node] = -1
    while len(ext1) !=0:
        for elem in ext1:
            for arch in archlist:
                if arch[0]==elem and arch[1] not in level:
                    ext2.append(arch[1])
                    level[arch[1]]=i
        ext1=ext2
        ext2=[]
        i+=1
    T = []
    P = []
    Dict[1] = 0
    P.insert(0, 1)
    while len(P) > 0:
        u = P.pop(0)
        T.append(u)
        for arch in archlist:
            if arch[0] == u:
                if Dict[arch[1]] == -1:
                    P.insert(0, arch[1])
                    Dict[arch[1]] = 0
                else:
                    if level[arch[1]]<level[arch[0]]:
                        revarch.append(arch)
    return revarch


print Dfs() #dajeeee










