# -*- coding: utf-8 -*-
#import networkx as nx
#import matplotlib.pyplot as plt
#from PriorityDijkstra import dijkstra2,dijkstra
from time import time           # Importazione libreria time per la misurazione il tempo

import BellmanFord              # Importazione file BellmanFord.py sul quale è presente l'algoritmo risolutivo del grafo


class Node:                     # Inizializzazione classe Node
    def __init__(self, value, weight):       # Definizione attributi e variabili formali
        self.value = value                   # value indica l'indice del nodo
        self.weight = weight                 # weight indica la concentrazione media di polveri sottili presenti nel nodo


class Arc:                     # Inizializzazione classe Arc
    def __init__(self, dep, arr, weight):           # Definizione attributi e variabili formali
        self.dep = dep                              # dep, departure, indica il nodo di partenza dell'arco
        self.arr = arr                              # arr, arrival, indica il nodo di arrivo dell'arco
        self.weight = weight                        # weight indica il costo di percorrenza dell'arco


class Graph:                   # Inizializzazione classe Graph
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
    Funzione principale del programma : provvede alla chiamata della funzoine reading per la letture del file,
    crea un grafo per ogni caso di test (aggiungendo nodi ed archi allo stesso) per poi invocare la funzione BellmanFord
    per la risoluzione del caso di test
    @param file: fileobject; tipo di dato file con indirizzo relativo alla posizione del file di input
    """
    result = reading(file)

    for i in range(0, len(result)):         # Inizializzazione del grafo G come elemento della classe Graph per ogni caso di test
        G = Graph()
        for j in range(len(result[i][1])):  #TODO commentare
            G.insertNode(j + 1, result[i][1][j])

        for elem in result[i][2]:            #TODO commentare
            G.insertArc(int(elem[0]), int(elem[1]))
        print "\nCaso " + str(i + 1) + ":"
        BellmanFord.BellmanFord(G, result[i][3]) #TODO commentare


def reading(file): #TODO finire di commentare

    x = file.readlines()
    Total = []           # Creazione della lista Total
    numbcase = x[0]      # Assegnazione di variabile : alla variabile "numbcase" viene assegnato il valore di x[0] il quale, per com'è costruito il file di input, indica sempre il numero di test da effettuare
    i = 1                # Assegnazione di variabile : la variabile "i" viene assegnato il valore 1. La variabile i servirà nel cilo while successivo per determinare quando si sarà letto tutto il file
    while i < len(x) - 1: # Ciclo che legge tutto il file, basandosi sul contatore i
        if x[i] == "\n":  # Se x[i] == "\n" allora alla riga successiva inizierà un nuovo caso

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