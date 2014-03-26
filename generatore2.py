__author__ = 'Fabrizio' # generatore definitivo !

from random import randrange

def generatore(): # questo generatore crea grafi ottimali per provare l'algoritmo
    n=10
    m=n*(n-1)
    nodelist=[]
    archlist=[]
    for i in range(1,n+1):
        pol=randrange(1,20)
        node=[i,pol]
        nodelist.append(node)
    for x in range(1,n+1):
        for y in range(1,n+1):
            if x!=y:
                arch=[x,y]
                archlist.append(arch)
    print nodelist
    return archlist


print generatore()



