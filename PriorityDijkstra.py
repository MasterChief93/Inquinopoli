class Street:
    def __init__(self,par,arr,peso):
        self.par = par
        self.arr = arr
        self.peso = peso


class Node:
    def __init__(self,value):
        self.value = value
        self.fath = None
        self.son = None

class Tree:
    def __init__(self):
        self.elems = None

    def addElem(self,padre,figlio):
        padre = Node(padre)
        figlio = Node(figlio)
        if self.elems == None:
            self.elems = [figlio]
        else:
            padre.son = figlio
            figlio.fath = padre
            self.elems.append(figlio)





def dijkstra(G,rad,arr):
    graph = G
    state = dict()
    state[rad] = 0
    rad = Node(rad)
    arr = Node(arr)
    tree = Tree()
    tree.addElem(rad,rad)
    print tree.elems[0].value
    while arr not in tree.elems:
        eligible = []
        for elem in tree.elems:
            for archi in graph.streets[elem.value]:
                if archi not in eligible:
                    eligible.append(archi)
        cheapest = minus(eligible)
        tree.addElem(cheapest.par,cheapest.arr)
        print cheapest.par, cheapest.arr
        #eligible.pop(eligible.index(cheapest))
        graph.streets[cheapest.par].remove(cheapest)
    return tree.elems


def minus(elements):
    min = Street(0,0,6860)
    for elem in elements:
        if elem.peso < min.peso:
            min = elem
    return min








