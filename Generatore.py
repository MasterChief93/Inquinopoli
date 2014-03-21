# coding=utf-8
__author__ = 'Federico'
from random import randrange
from time import time

def generator(): # Federico
    file = open('input.txt','w')
    stringonona = ''
    nodes = randrange(1,200)                #numero città
    stringpm10 = ''                         #stringa
    for x in range(nodes):                  #per ogni città
        pm20 = randrange(1,20)              #creo un pm10
        if x != nodes - 1:
            stringpm10 += str(pm20) + ' '
        else:
            stringpm10 += str(pm20) + '\n'
    numbstr = randrange(nodes-1,nodes**2)    #numero delle strade
    lista = []
    lista.append([1,randrange(1,nodes)])    #almeno una strada parte da 1
    while len(lista) < numbstr:             #finche la lista non contiene il numero delle strade uscito:
        x = randrange(1,nodes)
        y = randrange(1,nodes)
        if x != y:
            elem = [x,y]
            if elem not in lista:
                lista.append(elem)
    stringona = str(nodes) + '\n' + stringpm10 + str(numbstr) + '\n'
    stringa = ''
    for elem in lista:
        stringa += str(elem[0]) + ' ' + str(elem[1]) + '\n'
    stringona += stringa
    stringonona += stringona
    file.write(stringonona)
    file.close()

#start = time()
#generator()
#end = time()
#print "done in: ", end-start

def Generator(): # Fabrizio
    file = open('./input.txt','w')
    i=1
    cases=randrange(1,50)
    file.write(str(cases)+"\n\n")
    for _ in range(0,1):
        nodelist=[]
        archlist=[]
        for _ in range(1,randrange(3,200)):
            node=[i,randrange(1,20)]
            i+=1
            nodelist.append(node)
        n=len(nodelist)
        file.write(str(n)+"\n")
        for node in nodelist:
            inq=str(node[1])
            file.write(inq+" ")
        for _ in range(1,randrange(2,200)):
            randstart=randrange(1,n)
            randend=randrange(1,n)
            arch=[randstart,randend]
            revarch=[randend,randstart]
            if not arch in archlist and randstart!=randend and not revarch in archlist:
                archlist.append(arch)
    #print nodelist
    #print archlist
    #print [len(nodelist),len(archlist)]
    file.close()
    print cases

start = time()
Generator()
end = time()
print "done in: ", end-start

