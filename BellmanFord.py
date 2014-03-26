__author__ = 'Federico'


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
                    for extra_street in G.streets[street.arr]:
                        Distance[extra_street.arr] = Distance[extra_street.par] + extra_street.peso
    if Distance[arr] < 3:
        print 0
    elif Distance[arr] == float("+inf"):
        print "?"
    else:
        print Distance[arr]

    print Distance







