# -*- coding: utf-8 -*-
#import networkx as nx
#import matplotlib.pyplot as plt
#from PriorityDijkstra import dijkstra2,dijkstra
import BellmanFord
from generatore2 import Generatore
from time import time           #from graph_tool.all import *

class City:
    def __init__(self,value,peso):
        self.value = value                   #Inizializzazione della classe città:
        self.peso = peso                     #ognuna contiene valore (numero della città)
        #self.frow = []                      #peso (PM20) e lista delle città dalle quali si può giungere a questa (probabilmente da rimuove!!)

class Street:
    def __init__(self,par,arr,peso):
        self.par = par
        self.arr = arr
        self.peso = peso

class Grafo:
    def __init__(self):
        self.cities = None                  #Inizializzazione del grafo: dizionario delle città e array delle strade
        self.streets = None

    def insertCity(self,value,peso):
        newCity = City(value,peso)          #Creazione di un elemento di classe città
        if self.cities == None:             #Se non sono state MAI aggiunte città allora inizializzo il dizionario con la nuova città
            self.cities = {value: newCity}
        else:
            self.cities[value] = newCity    #Altrimenti metto la nuova città nella posizione value ------>
        return newCity                      #------> Vantaggio dei dizionari = Se l'elemento di nome/posizione value non esiste allora lo crea da solo

    def insertStreet(self,par,arr):
        if par in self.cities and arr in self.cities:
            peso = (int(self.cities[arr].peso) - int(self.cities[par].peso))**3                                                    #Innanzitutto devo esistere entrambe le città per poter essere creata la strada
            if self.streets == None:                                    #Se non ci sono strade allora inizializzo la lista di liste delle strade
                self.streets = {par: [Street(par,arr,peso)]}            #par.value e arr.value
            else:                                                       #altrimenti appendo semplicemente la nuova strada
                if par in self.streets:
                    self.streets[par].append(Street(par,arr,peso))
                else:
                    self.streets[par] = [Street(par,arr,peso)]          #idem

    def deleteStreet(self,par,arr):
        if [par.value,arr.value] in self.streets:           #La strada innanzitutto deve essere nella lista delle strade
            self.streets.remove([par.value,arr.value])      #Uso il comando "remove" per trovare ed eliminare automaticamente l'elemento
            arr.frow.remove(par.value)                      #Rimuovo inoltre la città di partenza dalla lista "frow" della città di arrivo
            print self.streets                              #Print tanto per...
            print arr.frow

    def visit(self,root):#visita generica
        state = dict()                      #inizializzo un dizionario per tener conto delle città visitate
        state[root] = 1                     #la radice viene visitata
        Explored = []                       #Mantengo la lista degli elementi visitati
        s = set()                           #Il set è una semplice lista alla fine...
        s.add(root)                         #Aggiungo la radice al set
        while len(s) > 0:                   #finché non lo svuoto
            now = s.pop()                   #poppo il primo elemento
            state[now] == 1                 #dico che l'ho visitato
            Explored.append(now)            #e lo metto tra gli esplorati
            for elem in self.streets:
                if elem == now:                                #per tutte le strade che partono dall'elemento poppato
                    new = elem[1]                              #prendo la città di arrivo
                    if not new in state or state[now] == 1:    #se non è già stata visitata
                        state[new] = 0                         #la imposto come vista
                        s.add(new)                             #e la aggiungo al set
        print Explored

    def visitDFS(self,root):
        state = dict()                      #stesso funzionamento della visita generica
        state[root] = 1                     #ma al posto del set uso una lista e invece dell'add uso un insert alla posizione 0
        Explored = []
        s = []
        s.insert(0,root)
        while len(s) > 0:
            now = s.pop(0)              #e il pop del primo elemento. è semplicemente una pila
            state[now] == 1
            Explored.append(now)
            print self.streets
            for elem in self.streets:
                if self.streets[elem] == now:
                    new = elem[1]
                    if not new in state or state[now] == 1:
                        state[new] = 0
                        s.insert(0,new)
        print Explored

    def visitBFS(self,root):
        state = dict()                  #stessa cosa dei precedenti. Uso s come una lista
        state[root] = 1
        Explored = []
        s = []
        s.append(root)            #invece dell'insert uso un append
        while len(s) > 0:
            now = s.pop(0)              #e il pop del primo elemento. Esattamente come una coda
            state[now] == 1
            Explored.append(now)
            for elem in self.streets:
                if elem[0] == now:
                    new = elem[1]
                    if not new in state or state[now] == 1:
                        state[new] = 0
                        s.append(new)
        print Explored



def main(file):
    result = lettura(file)#Generatore()
    for i in range(0,len(result)):
        G = Grafo()
        #Gr = nx.DiGraph()
              #E' il secondo esempio del file input nel progetto
        for j in range(len(result[i][1])):
            G.insertCity(j+1,result[i][1][j])
            #Gr.add_node(i+1)

        for elem in result[i][2]:
            G.insertStreet(int(elem[0]),int(elem[1]))
            #Gr.add_edge(int(elem[0]),int(elem[1]))

        #print G.streets[6]
        #dijkstra2(G,1,7)
        BellmanFord.Bel3(G,result[i][3])
        #nx.draw(Gr)
        #plt.savefig("path.png")

def lettura(file):
    x = file.readlines()
    Total = []
    numbcase = x[0]
    i = 1
    while i != len(x) - 1:
        if x[i] == "\n":
            numbnode = x[i+1].strip()
            pm20list = x[i+2].strip().split(' ')
            numbarch = x[i+3].strip()
            archi = []
            len_archi = i + 3 + int(numbarch) + 1
            for j in range(i + 4 , len_archi):
                archi.append(x[j].strip().split(' '))
            query = []
            for j in range(len_archi + 1 , len_archi + int(x[len_archi]) + 1):
                query.append(int(x[j].strip()))
            case = [numbnode,pm20list,archi,query]
            #print case
            Total.append(case)
        i = len_archi + int(x[len_archi]) + 1
    #print Total
    return Total
    #exit(Total)
    #return total

start = time()
file = open('input2.txt','r')
main(file)
end = time()
print end-start