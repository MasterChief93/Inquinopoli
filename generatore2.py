__author__ = 'Fabrizio' # generatore definitivo !

from random import randrange


def Generatore():
    file=open("input2.txt","w")
    n=randrange(2,200)
    file.write(str(n)+"\n")
    for p in range(0,n):
        file.write(str(randrange(1,20))+" ")
    file.write("\n")
    arclist=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j:
                arclist.append([i,j])
    m=randrange(0,n*(n-1))
    for arc_to_delete in range(0,m):
        index=randrange(0,len(arclist))
        arclist.remove(arclist[index])
    file.write(str(len(arclist))+"\n")
    for arc in arclist:
        file.write(str(arc[0])+" "+str(arc[1])+"\n")
    file.close()
