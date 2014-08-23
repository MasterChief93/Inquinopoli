__author__ = 'Fabrizio'
from main import maint
from generatore2 import Generatore

def Test():
    #n=raw_input("Inserisci il numero di test da effettuare")
    for x in range(0,50):
        print "Sto eseguendo il caso numero",x+1
        file=open("input2.txt","w")
        Generatore(file)
        file.close()
        file=open("input2.txt","r")
        maint(file,"output.txt")
        file.close()
    file.close()

Test()