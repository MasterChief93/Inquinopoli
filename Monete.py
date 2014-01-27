__author__ = 'Federico'
from time import time

def distr(monete,resto):
    best = None
    bestins = len(monete)
    for i in range(len(monete)):
        ins = 0
        elig = []
        base = monete[i]
        elig.append(base)
        for j in range(i+1,len(monete)):
            if base + monete[j] <= resto:
                elig.append(monete[j])
                base += monete[j]
                ins += 1
        sum = 0
        for i in range(len(elig)):
            sum += elig[i]
        if sum == resto and ins < bestins:
            bestins = ins
            best = elig
        #print best
    return best

def distr2(mon,resto):
    best = mon
    for i in range(len(mon)):
        elig = []
        sum = 0
        sum += mon[i]
        elig.append(mon[i])
        for j in range(i,len(mon)):
            if sum + mon[j] <= resto:
                sum += mon[j]
                elig.append(mon[j])
            if sum == resto and len(elig) < len(best):
                best = elig
    return best




monete = [180,170,160,150,130,110,90,70,60,20,10]
resto = 10
def main():
    start = time()
    print distr2(monete,resto)
    end = time()
    print end-start
    start = time()
    print distr(monete,resto)
    end = time()
    print end-start

main()