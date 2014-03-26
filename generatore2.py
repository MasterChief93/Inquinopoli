__author__ = 'Fabrizio' # generatore definitivo !

from random import randrange

def generatore(): # questo generatore crea grafi ottimali per provare l'algoritmo
    n=10
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
    pm20list = []
    for elem in nodelist:
        pm20list.append(elem[1])

    return [10,pm20list,archlist]


#print generatore()

def Generatore():
    n=10
    nodelist=[]
    archlist=[]
    pol=1
    for i in range(1,n+1):
        node=[i,pol]
        nodelist.append(node)
        pol+=1
    for x in range(1,n+1):
        for y in range(1,n+1):
            if x!=y:
                arch=[x,y]
                archlist.append(arch)
    pm20list = []
    for elem in nodelist:
        pm20list.append(elem[1])
    print nodelist
    return [10,pm20list,archlist]


Generatore()
