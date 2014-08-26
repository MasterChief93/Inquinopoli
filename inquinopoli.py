# -*- coding: utf-8 -*-

from generatore2 import Generatore
from main import maint
from time import time
import os

def main():
    print "--------------------------------------------------------------------------"
    print "                     Progetto Numero 1: Inquinopoli\n" \
          "                                 Autori\n" \
          "                Fabrizio Tafani   -  \n" \
          "                Federico Vagnoni  -  fede93.vagnoni@gmail.com"
    print "--------------------------------------------------------------------------\n"
    choice = raw_input("Si vuole usare il generatore (0) o inserire un file di input esistente (1) ? ")
    if int(choice) == 1:
        input_filename = raw_input("Inserisca il nome e il percorso del file di input: ")
        while not os.path.exists(input_filename) :
            print "Il file specificato non esiste\n"
            input_filename = raw_input("Inserisca il nome e il percorso del file di input: ")
        output_filename = raw_input("Inserisca il nome e il percorso del file di output: ")

    else:
        input_filename = raw_input("Inserisca il nome e il percorso del file di input: ")
        output_filename = raw_input("Inserisca il nome e il percorso del file di output: ")
        btest = raw_input("Inserisca 0 se vuole un numero random di test, altrimenti il numero desiderato (tra 1 e 50): ")
        btest = int(btest)
        if btest == 1 :
            bnode = raw_input("Inserisca 0 se vuole un numero random di nodi, altrimenti il numero desiderato (tra 2 e 200): ")
            bnode = int(bnode)
            barch = raw_input("Inserisca 0 se vuole un numero random di archi, altrimenti il numero desiderato (tra 0 e " + str(bnode*(bnode - 1)) +"): ")
            barch = int(barch)
            percentage = 100
        else:
            percentage = raw_input("E' possibile definire una densita' degli archi nel grafo: (da 1 percento a 100 percento ): ")
            percentage = int(percentage)
            bnode = 0
            barch = 0

    start = time()
    print "\nAvvio risoluzione casi"
    if int(choice) == 0:
        input_file = open(input_filename,"w")
        Generatore(input_file,btest,bnode,barch,percentage)
        print "\nGenerazione casi completata"
        input_file.close()

    input_file = open(input_filename,"r")
    maint(input_file,output_filename)
    input_file.close()

    print "\n Risoluzione completata in",time() - start, "secondi"
    print "\nFine del test"


main()