__author__ = 'Federico'

from generatore2 import Generatore
from main import maint

def main():
    print "Progetto Numero 1: Inquinopoli\n\tdi Fabrizio Tafani e Federico Vagnoni"
    print "\n Avvio generazione e risoluzione casi:"
    input_filename = raw_input("Inserisca il nome del file di input: ")
    output_filename = raw_input("Inserisca il nome del file di output: ")
    input_file = open(input_filename,"w")
    Generatore(input_file)
    input_file.close()
    input_file = open(input_filename,"r")
    maint(input_file,output_filename)
    print "\n Risoluzione completata"
    print "\n Fine del test"


main()