# -*- coding: utf-8 -*-
from time import time           # Importazione della funzione time della libreria time per la misurazione il tempo

import generatore2              # Importazione dello script contenente la funzione Generatore
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
    generatore2.Generatore()
    result = reading(file)
    total_outlist=[]

    for i in range(0, len(result)):         # Inizializzazione del grafo G come elemento della classe Graph per ogni caso di test
        G = Graph()
        for j in range(len(result[i][1])):  # Per ogni caso di test l'elemento 1 contiene tutti i valore di pm20 dei nodi
            G.insertNode(j + 1, result[i][1][j])  # Questi perciò saranno aggiunti con indici pari a j + 1 (da 1 a n) e peso pari al pm20 letto

        for elem in result[i][2]:            # Ciclo che, tramite la funzione insertArc, inserisce nel grafo tutti gli archi letti dal file di input
            G.insertArc(int(elem[0]), int(elem[1]))
        print "\nCaso " + str(i + 1) + ":"

        outlist = BellmanFord.BellmanFord(G, result[i][3], i + 1) # Invocazione della funzione BellmanFord dall'omonimo file per il calcolo dei costi del grafo
        total_outlist.append(outlist)
    outfile=open("output.txt","w")
    for case in total_outlist:
        outfile.write("Caso "+str(case[0])+":\n")
        for i in range(1,len(case)):
            outfile.write(str(case[i]) + "\n")
    outfile.close()

def reading(file):
    """
    Funzione atta a leggere tutti i casi di test del file di input
    @param file: file object; file di input
    @return: Total: list; lista di liste i cui elementi rappresentano i singoli casi di test
    """
    data = file.readlines() # Assegnazione di variabile : a "data" viene assegnato il contenuto dell'intero file
    Total = []           # Creazione della lista Total
    numbcase = data[0]      # Assegnazione di variabile : a "numbcase" viene assegnato il valore di data[0] il quale, per com'è costruito il file di input, indica sempre il numero di test da effettuare
    i = 1                # Assegnazione di variabile : ad "i" viene assegnato il valore 1. La variabile i servirà nel cilo while successivo per determinare quando si sarà letto tutto il file
    while i < len(data) - 1: # Ciclo che legge tutto il file, basandosi sul contatore i
        if data[i] == "\n":  # Se data[i] == "\n" allora alla riga successiva inizierà un nuovo caso

            # Assegnazione di variabili ed inizializzazione liste

            numbnode = data[i + 1].strip()                         # a "numbnode" viene assegnato data[i + 1], ovvero il numero di nodi presenti nel grafo
            pm20list = data[i + 2].strip().split(' ')              # "pm20list" è una lista contenente le concentrazioni medie di polveri sottili presenti nei nodi del grafo
            numbarc = data[i + 3].strip()                          # a "numbarc" viene assegnato data[i + 3], ovvero il numero di archi presenti nel grafo
            arcs = []
            len_arcs = i + 3 + int(numbarc) + 1                    # "len_arcs" indica la lunghezza, nel file, delle righe di coppie di archi; serve a sapere quando dal file di input sono state lette tutte le coppie
            for j in range(i + 4, len_arcs):                       # Ciclo che inserisce nella lista "arcs" tutte le coppie di archi presenti nel grafo
                arcs.append(data[j].strip().split(' '))
            query = []
            for j in range(len_arcs + 1, len_arcs + int(data[len_arcs]) + 1):   # Ciclo che inserisce nella lista "query" tutte le query lette dal file di input
                query.append(int(data[j].strip()))
            case = [numbnode, pm20list, arcs, query]               # la lista "case" contiene tutte le informazioni relative al singolo caso di test in esame
            Total.append(case)                                     # ogni caso è aggiunto alla lista "Total"

        i = len_arcs + int(data[len_arcs]) + 1                     # Aggiornamento del contatore "i" per passare al caso successivo, se questo sarà maggiore della lunghezza del file il ciclo while terminerà
    return Total


if __name__ == "__main__":                           # Controllo atto a verificare se lo script viene eseguito direttamente o tramite importazione
    start = time()
    file = open('input2.txt', 'r')
    main(file)
    end = time()
    print end - start