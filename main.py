# -*- coding: utf-8 -*-
#import networkx as nx
#import matplotlib.pyplot as plt
#from PriorityDijkstra import dijkstra2,dijkstra
from time import time           # Importazione libreria time per la misurazione il tempo

import BellmanFord              # Importazione file BellmanFord.py sul quale è presente l'algoritmo risolutivo del grafo


class Node:                     # Inizializione classe Node
    def __init__(self, value, weight):       # Definizione attributi e variabili formali
        self.value = value                   # value indica l'indice del nodo
        self.weight = weight                 # weight indica la concentrazione media di polveri sottili presenti nel nodo


class Arc:                     # Inizializazione classe Arc
    def __init__(self, dep, arr, weight):           # Definizione attributi e variabili formali
        self.dep = dep                              # dep, departure, indica il nodo di partenza dell'arco
        self.arr = arr                              # arr, arrival, indica il nodo di arrivo dell'arco
        self.weight = weight                        # weight indica il costo di percorrenza dell'arco


class Graph:                  # Inizializzazione classe Graph
    def __init__(self):                    # Definizione attributi di Graph
        self.nodes = None                  # self.nodes conterrà tutti i nodi di Graph
        self.arcs = None                   # self.arcs conterrà tutti gli archi di Graph

    def insertNode(self, value, weight):
        """
        Il metodo insertNode inserisce un nodo in Graph con i relativi attributi
        @param value: int; indice del nodo (corrisponderà all'attributo value della classe Node)
        @param weight: int; concentrazione media di polveri sottili presenti nel nodo (corrisponderà all'attributo weight della classe Node)
        @return: newNode: Node instance; istanza della classe Node di attributi "value" e "weight"
        """
        newNode = Node(value, weight)          # Creazione di un elemento di classe Node
        if self.nodes == None:             # Se non sono state MAI aggiunti nodi allora inizializzo il dizionario con il nuovo nodo
            self.nodes = {value: newNode}
        else:
            self.nodes[value] = newNode    # Altrimenti inserisco il nuovo nodo nella posizione "value" ------>
        return newNode                      # ------> Vantaggio dei dizionari : se l'elemento di nome/posizione value non esiste allora lo crea da solo

    def insertArc(self, dep, arr):
        """
        Il metodo insertArc inserisce un nuovo arco in Graph (lo aggiunge al dizionario self.arcs)
        @param dep: int; indice del nodo di partenza dell'arco (attributo "dep" della classe Arch)
        @param arr: int; indice del nodo di arrivo dell'arco   (attributo "arr" della classe Arch)
        """
        if dep in self.nodes and arr in self.nodes:                 # Controllo atto a verificare la presenza dei nodi corrispondenti agli indici dep ed arr nel dizionario self.nodes
            weight = (int(self.nodes[arr].weight) - int(self.nodes[dep].weight)) ** 3   # Calcolo peso dell'arco basato sull'attributo "weight" dei nodi
            if self.arcs == None:                                    # Se non ci sono strade allora inizializzo un dizionario di liste delle strade
                self.arcs = {dep: [Arc(dep, arr, weight)]}           # ogni elemento avrà come chiave l'indice del nodo di partenza e come valore la lista di archi uscenti da tale nodo
            else:
                if dep in self.arcs:                                 # Se il dizionario non è vuoto verrà inserita una nuova coppia chiave-valore
                    self.arcs[dep].append(Arc(dep, arr, weight))     # se il nodo di partenza era già presente nel dizionario, aggiungerò il nuovo arco alla sua lista di archi uscenti
                else:
                    self.arcs[dep] = [Arc(dep, arr, weight)]          # altrimenti verrà inserita una nuova coppia chiave-valore


def main(file):
    """

    @param file:
    """
    result = reading(file)

    for i in range(0, len(result)):
        G = Graph()
        for j in range(len(result[i][1])):
            G.insertNode(j + 1, result[i][1][j])

        for elem in result[i][2]:
            G.insertArc(int(elem[0]), int(elem[1]))
        print "\nCaso " + str(i + 1) + ":"
        BellmanFord.BellmanFord(G, result[i][3])


def reading(file):
    x = file.readlines()
    Total = []
    numbcase = x[0]
    i = 1
    while i < len(x) - 1:
        if x[i] == "\n":
            numbnode = x[i + 1].strip()
            pm20list = x[i + 2].strip().split(' ')
            numbarc = x[i + 3].strip()
            arcs = []
            len_arcs = i + 3 + int(numbarc) + 1
            for j in range(i + 4, len_arcs):
                arcs.append(x[j].strip().split(' '))
            query = []
            for j in range(len_arcs + 1, len_arcs + int(x[len_arcs]) + 1):
                query.append(int(x[j].strip()))
            case = [numbnode, pm20list, arcs, query]
            Total.append(case)
        i = len_arcs + int(x[len_arcs]) + 1
    return Total


if __name__ == "__main__":
    start = time()
    file = open('input2.txt', 'r')
    main(file)
    end = time()
    print end - start