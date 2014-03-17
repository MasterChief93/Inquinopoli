# coding=utf-8
__author__ = 'Federico'
from random import randrange
from time import time

def generator():
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

start = time()
generator()
end = time()
print "done in: ", end-start