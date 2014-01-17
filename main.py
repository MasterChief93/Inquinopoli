__author__ = 'Federico'
__author__ = 'Federico'

class City:
    def __init__(self,value,peso):
	    self.value = value
	    self.peso = peso
	    self.frow = []

class Grafo:

    def __init__(self):
	        self.cities = None
	        self.streets = None


    def insertCity(self,value,peso):
        newCity = City(value,peso)
	    if self.cities == None:
	        self.cities = {value : newCity}
        else:
	        self.cities[value] = newCity
	    return newCity


	def insertStreet(self,par,arr):
	    if (par.value in self.cities) and (arr.value in self.cities):
	        if self.streets == None:
	            self.streets = [[par.value,arr.value]]
	        else:
	            self.streets.append([par.value,arr.value])
	        arr.frow.append(par.value)

    def deleteStreet(self,par,arr):
	    if [par.value,arr.value] in self.streets:
	        self.streets.remove([par.value,arr.value])
	        arr.frow.remove(par.value)
	        print self.streets
	        print arr.frow

	def visit(self,root):
	        #assert root.value == 1
	        state = dict() # -1 unexplore , 0 added to the froniter, 1 explored
	        state[root.value] = 1

	        Explored = []

	        s = set()
	        s.add(root.value)

	        while len(s) > 0:
	            now = s.pop()
	            state[now] == 1
	            Explored.append(now)
	            for elem in self.streets:
	                if elem[0] == now:
	                    new = elem[1]
	                    if not new in state or state[now] == 1:
	                        state[new] = 0
	                        s.add(new)
	        print Explored
	def visitBFS(self,root):
	    state = dict() # -1 unexplore , 0 added to the froniter, 1 explored
	    state[root.value] = 1
        Explored = []
	    s = []
	    s.append(root.value)
	    while len(s) > 0:
	        now = s.pop(0)
	        state[now] == 1
	        Explored.append(now)
	        for elem in self.streets:
	            if elem[0] == now:
	                new = elem[1]
	                if not new in state or state[now] == 1:
	                    state[new] = 0
	                    s.append(new)
	        print Explored

	def visitDFS(self,root):
	        state = dict() # -1 unexplore , 0 added to the froniter, 1 explored
	       state[root.value] = 1

	        Explored = []
	        s = []
	        s.insert(0,root.value)
	        while len(s) > 0:
	           now = s.pop(0)
	            state[now] == 1
	            Explored.append(now)
            for elem in self.streets:
	                if elem[0] == now:
	                    new = elem[1]
	                    if not new in state or state[now] == 1:
	                       state[new] = 0
	                        s.insert(0,new)
	        print Explored

	def reverseSearch(self,end):
	        if end.value == 1:
	            return end.value
	        else:
	            while len(end.frow) > 0:
	                next = end.frow.pop(0)
	                if next == 1:
	                    print next
	                #    return self.reverseSearch(self.cities[next])
	                else:
	                    print next
	                    self.reverseSearch(self.cities[next])

	##############################
	##############################







def main():
	G = Grafo()
	city1 = G.insertCity(1,6)
	city2 = G.insertCity(2,7)
	city3 = G.insertCity(3,8)
	city4 = G.insertCity(4,9)
	city5 = G.insertCity(5,10)
	city6 = G.insertCity(6,11)
	city7 = G.insertCity(7,12)
	G.insertStreet(city1,city2)
	G.insertStreet(city2,city3)
	G.insertStreet(city3,city4)
	G.insertStreet(city4,city5)
	G.insertStreet(city5,city6)
	G.insertStreet(city6,city2)
    G.insertStreet(city2,city7)
	#G.deleteStreet(city4,city5)
	print G.cities
	print G.streets
	print city1.frow
	print city2.frow
	print city3.frow
	print city4.frow
	print city5.frow
	G.visit(city1)
	G.visitBFS(city1)
	G.visitDFS(city1)
    G.reverseSearch(city6)
main()
