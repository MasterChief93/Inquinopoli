__author__ = 'Fabrizio'

from random import randrange,choice

def maxarchi(N):
    n=0
    m=0
    for _ in range(0,N):
        m+=n
        n+=1
    return m

def generatore():
    n=4
    m=maxarchi(n)
    mfinal=randrange(2,m)
    archlist_final=[]
    matrice=[]
    nodelist=[]
    for _ in range(1,n+1):
        nodelist.append(_)
    for nodeP in nodelist:
        archlist=[]
        for nodeA in nodelist:
            if nodeP!=nodeA:
                archlist.append([nodeP,nodeA])
            else:
                archlist.append(0)
        matrice.append(archlist)
    for i in range(0,n):
        for j in range(0,n):
            if i!=j:
                coppia=[matrice[i][j],matrice[j][i]]
                if coppia[0]!=0 and coppia[1]!=0:
                    scelta=randrange(0,1)
                    archlist_final.append(coppia[scelta])
                    matrice[i][j]=0
                    matrice[j][i]=0
    print mfinal
    print archlist_final
    if mfinal!=len(archlist_final):
        archlist_definitive=[]
        for _ in range(0,mfinal):
            arco=choice(archlist_final)
            archlist_final.remove(arco)
            archlist_definitive.append(arco)
    print archlist_definitive


generatore()



