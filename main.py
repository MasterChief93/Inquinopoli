class City:
    def __init__(self,value,peso):
	    self.value = value                  #Inizializzazione della classe città:
	    self.peso = peso                    #ognuna contiene valore (numero della città)
	    self.frow = []                      #peso (PM20) e lista delle città dalle quali si può giungere a questa (probabilmente da rimuove!!)

class Grafo:
    def __init__(self):
        self.cities = None                  #Inizializzazione del grafo: dizionario delle città e array delle strade
        self.streets = None

    def insertCity(self,value,peso):
        newCity = City(value,peso)       #Creazione di un elemento di classe città
        if self.cities == None:             #Se non sono state MAI aggiunte città allora inizializzo il dizionario con la nuova città
            self.cities = {value: newCity}
        else:
            self.cities[value] = newCity    #Altrimenti metto la nuova città nella posizione value ------>
        return newCity                      #------> Vantaggio dei dizionari = Se l'elemento di nome/posizione value non esiste allora lo crea da solo

    def insertStreet(self,par,arr):
        if (par.value in self.cities) and (arr.value in self.cities):   #Innanzitutto devo esistere entrambe le città per poter essere creata la strada
            if self.streets == None:                                    #Se non ci sono strade allora inizializzo la lista di liste delle strade
                self.streets = [[par.value,arr.value]]
            else:                                                       #altrimenti appendo semplicemente la nuova strada
                self.streets.append([par.value,arr.value])
            arr.frow.append(par.value)

    def deleteStreet(self,par,arr):
        if [par.value,arr.value] in self.streets:           #La strada innanzitutto deve essere nella lista delle strade
            self.streets.remove([par.value,arr.value])      #Uso il comando "remove" per trovare ed eliminare automaticamente l'elemento
            arr.frow.remove(par.value)                      #Rimuovo inoltre la città di partenza dalla lista "frow" della città di arrivo
            print self.streets                              #Print tanto per...
            print arr.frow

    def visit(self,root):#visita generica
        state = dict()                      #inizializzo un dizionario per tener conto delle città visitate
        state[root.value] = 1               #la radice viene visitata
        Explored = []                       #Mantengo la lista degli elementi visitati
        s = set()                           #Il set è una semplice lista alla fine...
        s.add(root.value)                   #Aggiungo la radice al set
        while len(s) > 0:                   #finché non lo svuoto
            now = s.pop()                   #poppo il primo elemento
            state[now] == 1                 #dico che l'ho visitato
            Explored.append(now)            #e lo metto tra gli esplorati
            for elem in self.streets:
                if elem[0] == now:          #per tutte le strade che partono dall'elemento poppato
                    new = elem[1]           #prendo la città di arrivo
                    if not new in state or state[now] == 1:    #se non è già stata visitata
                        state[new] = 0                         #la imposto come vista
                        s.add(new)                             #e la aggiungo al set
        print Explored

    def visitDFS(self,root):
        state = dict()                  #stesso funzionamento della visita generica
        state[root.value] = 1           #ma al posto del set uso una lista e invece dell'add uso un insert alla posizione 0
        Explored = []
        s = []
        s.insert(0,root.value)
        while len(s) > 0:
            now = s.pop(0)              #e il pop del primo elemento. è semplicemente una pila
            state[now] == 1
            Explored.append(now)
            for elem in self.streets:
                if elem[0] == now:
                    new = elem[1]
                    if not new in state or state[now] == 1:
                        state[new] = 0
                        s.insert(0,new)
        print Explored

    def visitBFS(self,root):
        state = dict()                  #stessa cosa dei precedenti. Uso s come una lista
        state[root.value] = 1
        Explored = []
        s = []
        s.append(root.value)            #invece dell'insert uso un append
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



def main():
    G = Grafo()               #E' il secondo esempio del file input nel progetto
    city1 = G.insertCity(1,9)               #piccolo test di un grafo
    city2 = G.insertCity(2,10)              #Aggiungo le città numerate con i relativi pesi
    city3 = G.insertCity(3,6)
    city4 = G.insertCity(4,1)
    city5 = G.insertCity(5,4)
    city6 = G.insertCity(6,8)
    city7 = G.insertCity(7,13)
    G.insertStreet(city1,city2)             #Aggiungo le strade
    G.insertStreet(city2,city3)
    G.insertStreet(city3,city4)
    G.insertStreet(city4,city5)
    G.insertStreet(city5,city6)
    G.insertStreet(city6,city2)
    G.insertStreet(city2,city7)
    G.visit(city1)
    G.visitBFS(city1)                       #Faccio delle visite
    G.visitDFS(city1)

main()