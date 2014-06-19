__author__ = 'Fabrizio'
from main import main

def Test():
    n=raw_input("Inserisci il numero di test da effettuare")
    file=open("input2.txt","r")
    for x in range(0,int(n)):
        print "Sto eseguendo il caso numero",x+1
        main(file)
    file.close()

Test()