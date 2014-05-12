__author__ = 'Fabrizio' # generatore definitivo !

from random import randrange,seed
from time import clock,time #fuckyou

def Generatore(): # TODO troppo lento, da migliorare
    file=open("input2.txt","w")
    test=2 #randrange(1,50)
    file.write(str(test)+"\n\n")
    for i in range(0,test):
        seed(time() + i)
        n= 10#randrange(2,200)
        file.write(str(n)+"\n")
        for p in range(0,n):
            file.write(str(randrange(1,20))+" ")
        file.write("\n")
        arclist=[]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:
                    arclist.append([i,j])
        #seed(i)
        m=randrange(0,n*(n-1))
        for arc_to_delete in range(0,m):
            index=randrange(0,len(arclist))
            arclist.remove(arclist[index])
        file.write(str(len(arclist))+"\n")
        for arc in arclist:
            file.write(str(arc[0])+" "+str(arc[1])+"\n")
        #seed(i)
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

start=time()
Generatore()
print time()-start