__author__ = 'Federico'
from random import randrange
from time import time

def generator():
    file = open('input.txt','w')
    numbtest = randrange(1,20)
    stringonona = ''
    for y in range(numbtest):
        nodes = randrange(1,200)
        stringpm20 = ''
        for x in range(nodes):
            pm20 = randrange(1,20)
            if x != nodes - 1:
                stringpm20 += str(pm20) + ' '
            else:
                stringpm20 += str(pm20) + '\n'
        numbstr = randrange(nodes,nodes**2)
        lista = []
        lista.append([1,randrange(1,nodes)])
        while len(lista) < numbstr:
            x = randrange(2,nodes)
            y = randrange(2,nodes)
            if x != y:
                elem = [x,y]
                if elem not in lista:
                    lista.append(elem)

        stringona = str(nodes) + '\n' + stringpm20 + str(numbstr) + '\n'
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
print end-start