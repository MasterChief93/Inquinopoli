__author__ = 'Federico'

def bellmanford(G,arr):
    H = dict()
    citta = G.cities
    for elem in citta:
        H[elem] = float("+inf")
    H[1] = 0
    for partenze in G.streets:
        for elem in G.streets[partenze]:
            if H[elem.par] != float("+inf") and H[elem.par] + elem.peso < H[elem.arr]:
                H[elem.arr] = H[elem.par] + elem.peso
    if H[arr] < 3:
        print 0
    else:
        print H[arr]