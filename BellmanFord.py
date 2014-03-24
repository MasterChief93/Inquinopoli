__author__ = 'Federico'


def bellmanford(G, arr):
    Distance = dict()
    citta = G.cities
    for strade in citta:
        Distance[strade] = float("+inf")
    Distance[1] = 0
    Strade = []
    for partenze in G.streets:
        for strade in G.streets[partenze]:
            Strade.append(strade)

    while i < len(Strade):
        blabla = G.streets[1]
        for strade in blabla:
            if Distance[strade.par] != float("+inf") and Distance[strade.par] + strade.peso < Distance[strade.arr]:
                Distance[strade.arr] = Distance[strade.par] + strade.peso
        blabla = G.streets[2]


    if Distance[arr] < 3:
        print 0
    else:
        print Distance[arr]








