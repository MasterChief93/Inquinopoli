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
    costo = dict()
    for elem in g.cities:
        costo[elem] = float("+inf")
    costo[rad] = 0
    tree = [rad]
    while not check(g):
        for citta in tree:
            if citta in g.streets:
                for strade in g.streets[citta]:
                    #print strade.peso
                    newcosto = strade.peso + costo[strade.par]
                    if newcosto < costo[strade.arr]:
                        costo[strade.arr] = newcosto
                    #print "pago " + str(costo[strade.arr]) + " per andare da " + str(strade.par) + " a " + str(strade.arr)
                    g.streets[strade.par].remove(strade)
                tree.append(strade.arr)
    return costo[arr]


def minus(elements):
    min = Street(0, 0, 6860)
    for elem in elements:
        if elem.peso < min.peso:
            min = elem
    return min

def check(g):
    bool = [False]*len(g.streets)
    for i in range(len(g.streets)):
        if g.streets[i+1] == []:
            bool[i] = True
    if bool == [True]*len(g.streets):
        return True
    else:
        return False





