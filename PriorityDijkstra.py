class Street:
    def __init__(self,par,arr,peso):
        self.par = par
        self.arr = arr
        self.peso = peso


class Elem:
    def __init__(self,value):
        self.value = value
        self.fath = None
        self.son = None

class Tree:
    def __init__(self):
        self.elem = None

    def addElem(self,padre,figlio):
        padre = Elem(padre)
        figlio = Elem(figlio)
        if self.elem == None:
            self.elem = [figlio]
        else:
            padre.son = figlio
            figlio.fath = padre
            self.elem.append(figlio)





def dijkstra(G,rad,arr):
    graph = G
    state = dict()
    state[rad] = 0
    rad = Elem(rad)
    arr = Elem(arr)
    tree = Tree()
    tree.addElem(rad,rad)
    while arr not in tree.elem:
        eligible = []
        for elem in tree.elem:
            if graph.streets[elem.value] != []:
                for archi in graph.streets[elem.value.value]:
                    if archi not in eligible:
                        eligible.append(archi)
        cheapest = minus(eligible)
        #print "Eligible is: " + str(eligible)
        tree.addElem(cheapest.par,cheapest.arr)
        eligible.remove(cheapest)
        graph.streets[cheapest.par].remove(cheapest)
    return tree.elem


def minus(elements):
    min = Street(0,0,6860)
    for elem in elements:
        if elem.peso < min.peso:
            min = elem
    return min








