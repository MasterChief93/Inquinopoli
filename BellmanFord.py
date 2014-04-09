__author__ = 'Federico'
# -*- coding: utf-8 -*-

# def bellmanford(G, arr):
#     Distance = dict()
#     citta = G.cities
#     Hit = dict()
#     for strade in citta:
#         Distance[strade] = float("+inf")
#         Hit[strade] = 0
#     Distance[1] = 0
#     print Distance
#
#     for city in G.streets:
#         for street in G.streets[city]:
#             if Distance[street.par] != float("+inf") and Distance[street.par] + street.peso <= Distance[street.arr]:
#                 Hit[street.par] += 1
#                 Hit[street.arr] += 1
#                 old = Distance[street.arr]
#                 Distance[street.arr] = Distance[street.par] + street.peso
#                 if Hit[street.arr] > 1 and Distance[street.arr] <= old:
#                     if street.arr in G.streets:
#                         for extra_street in G.streets[street.arr]:
#                             Distance[extra_street.arr] = Distance[extra_street.par] + extra_street.peso
#     print Hit
#     if Distance[arr] < 3:
#         print 0
#     elif Distance[arr] == float("+inf"):
#         print "?"
#     else:
#         print Distance[arr]


def bellmanford2(G, arr):
    Distance = dict()
    citta = G.cities
    #Hit = dict()
    for strade in citta:
        Distance[strade] = float("+inf")
    Distance[1] = 0

    for city in G.streets:
        for street in G.streets[city]:
            if Distance[street.par] != float("+inf") and Distance[street.par] + street.peso <= Distance[street.arr]:
                Distance[street.arr] = Distance[street.par] + street.peso
    #print Distance

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


def Dfs(G,arr):
    revarch = []
    nodelist = []
    archlist = []
    for city in G.streets:
        for street in G.streets[city]:
            archlist.append([street.par,street.arr,street.peso])
    for city in G.cities:
        nodelist.append(city)
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

    print revarch
    Distance = dict()
    for strade in G.cities:
        Distance[strade] = float("+inf")
    Distance[1] = 0
    current = [1]
    future = []
    while len(current) != 0:

        for elem in current:

            if elem in G.streets:

                for street in G.streets[elem]:

                    if Distance[street.par] != float("+inf") and Distance[street.arr] > Distance[street.par] + street.peso:


                        if ([street.par,street.arr,street.peso] in revarch) and (Distance[street.par] + street.peso < Distance[street.arr]):
                            Distance[street.arr] = Distance[street.par] = float("-inf")
                        else:
                            Distance[street.arr] = Distance[street.par] + street.peso
                        print Distance
                        if street.arr not in future:
                            future.append(street.arr)
        current = future
        future = []


    print Distance

    if Distance[arr] < 3:
        return 0
    elif Distance[arr] == float("+inf"):
        return "?"
    else:
        return Distance[arr]


#print bellmanford2() #TODO dajeeee










