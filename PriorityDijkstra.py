# coding=utf-8
from PQbinaryHeap import PQbinaryHeap
from linked_ds.trees import treeArrayList
class Street:
    def __init__(self, par, arr, peso):
        self.par = par
        self.arr = arr
        self.peso = peso


class Elem:
    def __init__(self, value):
        self.num = value
        self.fath = None
        self.son = None


class Tree:
    def __init__(self):
        self.elems = None

    def addElem(self, padre, figlio):
        padre = Elem(padre)
        figlio = Elem(figlio)
        if self.elems == None:
            self.elems = [figlio]
        else:
            padre.son = figlio
            figlio.fath = padre
            self.elems.append(figlio)


def dijkstra(g, rad, arr):
    costo = dict()                                              #Inizializzo un dizionario per mantenere i costi degli archi
    for elem in g.cities:
        costo[elem] = float("+inf")                             #Inizializzo tutti gli elementi con costo +infinito
    costo[rad] = 0                                              #tranne la radice che avrà costo 0
    tree = [rad]                                                #Inizializzo un array per i nodi visitati, chiamato "tree" con dentro "rad"
    while not check(g):                                     #finché non percorro ogni arco
        for citta in tree:                                  #per ogni città inserita nell'albero (all'inizio solo rad)
            if citta in g.streets:                          #esisterà un insieme di archi per cui posso uscire da quelle città
                for strade in g.streets[citta]:
                    #print strade.peso
                    newcosto = strade.peso + costo[strade.par]      #il costo per arrivare alle città collegate sarà pari al costo dell'arco
                                                                    # più quello speso per arrivare al nodo appena precedente
                    if newcosto < costo[strade.arr]:                #se questo nuovo costo è minore del costo che avrei speso per arrivare a quella città da un altro percorso
                                                                    #allora lo rimpiazzio con il nuovo costo
                        costo[strade.arr] = newcosto
                    #print "pago " + str(costo[strade.arr]) + " per andare da " + str(strade.par) + " a " + str(strade.arr)
                    g.streets[strade.par].remove(strade)            #infine rimuovo la strada percorsa
                tree.append(strade.arr)                             #appendo il nodo visitato all'albero
    return costo[arr]                                               #ritorno il costo della città d'arrivo (il migliore finora trovato)


def minus(elements):
    min = Street(0, 0, 6860)
    for elem in elements:
        if elem.peso < min.peso:
            min = elem
    return min

def check(g):
    bool = [False]*len(g.streets)               #inizializzo un array di "False" lungo quanto la quantità delle strade
    for i in range(len(g.streets)):             #per ogni lista di strade uscenti dal nodo i-esimo
        if g.streets[i+1] == []:                #se queste sono state tutte percorse (quindi rimosse dalla funzione "dijkstra")
            bool[i] = True                      #allora il valore booleano nella posizione del nodo sarà True
    if bool == [True]*len(g.streets):           #Se tutte le strade sono state percorse (tutti True per ogni nodo)
        return True                             #allora torno True
    else:
        return False

def dijkstra2(g,root):
    costo = dict()                                              #Inizializzo un dizionario per mantenere i costi degli archi
    for elem in g.cities:
        costo[elem] = float("+inf")
    T = treeArrayList              #Inizializzazione alberello
    S = PQbinaryHeap()                 #e coda con priorità
    costo[root] = 0
    S.insert(root,0)
    while (not S.isEmpty()):
        u = S.deleteMin()
        for street in g.streets[u]:
            if costo[street.arr] == float("+inf"):
                S.insert(street.arr,costo[u] + street.peso)
                costo[street.arr] = costo[u] + street.peso
                T.insert(u,street.arr)
            elif costo[u] + street.peso < costo[street.arr]:
                S.decreaseKey(street.arr,costo[street.arr] - (costo[u] + street.peso))
                costo[street.arr] = costo[u] + street.peso
                T.insert(u,street.arr)
    return T





