# coding=utf-8
__author__ = 'Federico'
from random import randrange, choice
from time import time


def generator(): # Federico
    file = open('input.txt', 'w')
    stringonona = ''
    nodes = randrange(1, 200)                #numero città
    stringpm10 = ''                         #stringa
    for x in range(nodes):                  #per ogni città
        pm20 = randrange(1, 20)              #creo un pm10
        if x != nodes - 1:
            stringpm10 += str(pm20) + ' '
        else:
            stringpm10 += str(pm20) + '\n'
    numbstr = randrange(nodes - 1, nodes ** 2)    #numero delle strade
    lista = []
    lista.append([1, randrange(1, nodes)])    #almeno una strada parte da 1
    while len(lista) < numbstr:             #finche la lista non contiene il numero delle strade uscito:
        x = randrange(1, nodes)
        y = randrange(1, nodes)
        if x != y:
            elem = [x, y]
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
    file = open('./input.txt', 'w')
    i = 1 # contatore che aumenta e che dà il nome al nodo : il primo nodo creato avrà i=1, il secondo i=2 e così via. Per noi i nodi saranno quindi nodo 1, nodo 2, etc.
    global cases # variabile definita globalmente per poterla printare al di fuori della funzione, comodità
    cases = randrange(1, 50) # cases è il numero di casi che il generatore deve generare, cases <= 50
    file.write(str(cases) + "\n") # la prima riga del file di input contiene il numero di casi presi in esame
    for _ in range(0, cases): # ciclo che si occupa di generare tutti i casi
        file.write("\n") # ogni caso inizia con una riga vuota
        nodelist = [] # lista atta a contenere tutti i nodi generati in questo caso
        archlist = [] # lista atta a contenere tutti gli archi generati in questo caso
        for _ in range(1, randrange(3,
                                    200)): # ciclo che si occupa della creazione dei nodi. ATTENZIONE : manca da definire il comportamento del generatore se si hanno 0 nodi
            node = [i, randrange(1,
                                 20)] # creazione del nodo con struttura lista [numero del nodo,inquinamento]; con inquinamento <= 20
            i += 1 # il contatore i aumenta per la creazione del nodo successivo
            nodelist.append(node) # il nodo appena creato viene aggiunto alla lista dei nodi
        n = len(nodelist) # n indica la lunghezza della lista dei nodi, ovvero il numero dei nodi presenti nel caso
        file.write(str(
            n) + "\n") # la terza riga del file di input contiene il numero di nodi del caso (la riga precedente era vuota)
        for node in nodelist: # ciclo che scrive sul file il tasso di inquinamento di ogni nodo presente nella lista dei nodi
            inq = str(node[
                1]) # inq è il tasso di inquinamento, essendo il nodo di persè una lista ([numero del nodo,inquinamento]) allora abbiamo inq=str(node[1]), passato come stringa dovendolo scrivere su file
            file.write(inq + " ") # scrittura del tasso di inquinamento di ogni nodo, seguita da uno spazio
        file.write(
            "\n") # il file di input, dopo aver scritto tutti i tassi di inquinamento dei nodi, prevede di passare alla riga successiva
        for i in range(1, len(
                nodelist)): # ciclo che si occupa della creazione di tutti gli archi presenti nel caso. ATTENZIONE : manca da definire il numero massimo di archi presenti nel grafo e definire il comportamento del generatore quando ci sono 0 archi
            archi = []
            for j in range(1, len(nodelist)):     # randstart indica il nodo di partenza del futuro arco
            # randend indica il nodo di arrivo del futuro arco

                if j != i:
                    arch = [i, j] # creazione dell'arco con struttura lista [partenza,arrivo]
                    archi.append(arch)
                else:
                    arch = [0]
                    archi.append(arch)
            archlist.append(archi)
            # revarch=[randend,randstart] # revarch è l'arco di senso opposto all'arco appena creato. Serve alla riga successiva per il controllo : non ci può essere più di un arvo tra due nodi.
            # if not arch in archlist and randstart!=randend and not revarch in archlist: # controllo se l'arco creato può essere aggiunto alla lista degli archi. I controlli in ordine sono : l'arco non è gia presente nella lista degli archi, l'arco non collega un nodo a se stesso, l'arco è l'unico che collega i due nodi
            #     archlist.append(arch) # superato ogni controllo, l'arco viene aggiunto alla lista deli archi presenti nel caso
        print archlist[0]
        print archlist[1]
        for i in range(0, len(archlist)):
            for j in range(0, len(archlist[i])):
                coppia = [archlist[i][j], archlist[j][i]]
                print coppia, i, j
                elem = choice(coppia)
                if elem == coppia[0]:
                    archlist[i].remove(elem)
                else:
                    archlist[j].remove(elem)
        archlist_final = []
        for i in range(0, len(archlist)):
            for j in range(0, len(archlist[i])):
                if archlist[i][j] != 0:
                    archlist_final.append(archlist[i][j])

        m = len(archlist_final) # m indica la lunghezza di archlist, ovvero il numero di archi presenti nel caso
        file.write(str(
            m) + "\n") # nel file di input si deve ora scrivere il numero di archi presenti nel caso e passare alla riga successiva
        for element in archlist_final: # ciclo che si occupa di scrivere sul file tutti gli archi presenti nel caso, uno per ogni riga, scrivendo :   nodo di partenza    nodo di arrivo
            file.write(str(element[0]) + " " + str(element[1]) + "\n") # scrittura sopra citata
    q = randrange(1, n) # q è il numero di query, indica il numero di nodi che dovranno essere raggiunte dal nodo 1
    file.write(str(q) + "\n") # scrittura di q sul file di input e cambio di riga
    for _ in range(0, q): # ciclo che si occupa di scrivere i nodi sul file di inut, uno per ogni riga
        d = randrange(1, n) # d è il nodo di destinazione, scelto random tra i vari nodi presenti nel caso
        file.write(str(d) + "\n")
    file.close()


start = time()
Generator()
end = time()
print "It took ", end - start, "to generate ", cases, "cases"

# il generatore sembra funzionare bene, con tempi di esecuzione sempre inferiori al mezzo secondo. Minchiabboh

