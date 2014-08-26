__author__ = 'Federico'

from generatore2 import Generatore
from main import maint
from time import time

def main():
    print "Progetto Numero 1: Inquinopoli\n\tdi Fabrizio Tafani e Federico Vagnoni"
    print "\n Avvio generazione e risoluzione casi:"
    input_filename = raw_input("Inserisca il nome del file di input: ")
    output_filename = raw_input("Inserisca il nome del file di output: ")
    btest = raw_input("Inserisca 0 se vuole un numero random di test, altrimenti il numero desiderato (tra 1 e 50): ")
    btest = int(btest)
    if btest == 1 :
        bnode = raw_input("Inserisca 0 se vuole un numero random di nodi, altrimenti il numero desiderato (tra 2 e 200): ")
        bnode = int(bnode)
        barch = raw_input("Inserisca 0 se vuole un numero random di archi, altrimenti il numero desiderato (tra 0 e " + str(bnode*(bnode - 1)) +"): ")
        barch = int(barch)
    else:
        bnode = 0
        barch = 0
    tempotot = 0
    for _ in range(100) :
        start = time()
        input_file = open(input_filename,"w")
        Generatore(input_file,btest,bnode,barch)
        input_file.close()
        input_file = open(input_filename,"r")
        maint(input_file,output_filename)
        input_file.close()
        end = time()
        tempo = end - start
        tempotot += tempo
    print tempotot/100
    print "\n Risoluzione completata"
    print "\n Fine del test"


main()