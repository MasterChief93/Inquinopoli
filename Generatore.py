__author__ = 'Federico'
from random import randrange

def generator():
    file = open('input.txt','w')
    numbnod = randrange(1,20)
    stringonona = ''
    for y in range(numbnod):
        nodes = randrange(1,200)
        stringpm20 = ''
        for x in range(nodes):
            pm20 = randrange(1,20)
            stringpm20 += ' ' + str(pm20)
        nombstr = randrange(numbnod,numbnod**2)
        lista = []
        par = randrange(nodes)
        arr = randrange(nodes)
        while len(lista) < nombstr:
            elem = [randrange(1,nodes),randrange(1,nodes)]
            if elem not in lista:
                lista.append(elem)

        stringona = str(nodes) + '\n' + stringpm20 + '\n' + str(nombstr) + '\n'
        stringa = ''
        for elem in lista:
            stringa += str(elem[0]) + ' ' + str(elem[1]) + '\n'
        stringona += stringa
    stringonona += stringona
    file.write(stringonona)
    file.close()


generator()
