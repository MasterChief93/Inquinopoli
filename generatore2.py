__author__ = 'Fabrizio' # generatore definitivo !

from random import randrange,seed,sample
from time import time


def Generatore():
    file=open("input2.txt","w")
    test= randrange(1,50)
    file.write(str(test)+"\n\n")
    for i in range(0,test):
        seed(time() + i)
        n= randrange(2,200)
        file.write(str(n)+"\n")
        for p in range(0,n):
            randpol=randrange(1,20)
            file.write(str(randpol)+" ")
        file.write("\n")
        arclist=[]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:
                    arclist.append([i,j])
        m=randrange(0,n*(n-1))
        final_arclist=sample(arclist,m)
        file.write(str(len(arclist))+"\n")
        for arc in arclist:
            file.write(str(arc[0])+" "+str(arc[1])+"\n")
        q=randrange(1,n)
        file.write(str(q)+"\n")
        qlist=[]
        while len(qlist) < q:
            qn=randrange(1,n)
            if qn not in qlist:
                file.write(str(qn)+"\n")
                qlist.append(qn)
        file.write("\n")
    file.close()

#start=time()
Generatore()
#print time()-start
