import time 
import networkx as nx 
import matplotlib.pyplot as mpl 
import random
import itertools

def vse_kombinacije_3(n):
    return ((i, j, k)
        for i in range(1,n)
        for j in range(i + 1, n)
        for k in range(j + 1, n + (i > 0)))

def vse_kombinacije_2(n):
    return ((i, j)
        for i in range(1,n)
        for j in range(i + 2, n))

def zamenjaj_tri(graf, pot, i, j, k):
    A, B, C, D, E, F = pot[i-1], pot[i], pot[j-1], pot[j], pot[k-1], pot[k % len(pot)]
    d0 = graf[A][B] + graf[C][D] + graf[E][F]
    d1 = graf[A][C] + graf[B][E] + graf[D][F]
    d2 = graf[A][E] + graf[B][D] + graf[C][F]
    d3 = graf[A][D] + graf[E][B] + graf[C][F]
    m = [d1, d2, d3]
    ind = m.index(min(m)) # indeks najkrajše poti
    if d0 > min(m):
        if ind == 0:
            a = pot[j-1:i-1:-1] + pot[k-1:j-1:-1]
            pot[i:k] = a
            return d1 - d0
        if ind == 1:
            a = pot[k-1:j-1:-1] + pot[i:j]
            pot[i:k] = a
            return d2 - d0
        if ind == 2:
            a = pot[j:k] + pot[i:j]
            pot[i:k] = a
            return d3 - d0
    return 0


def zamenjaj_dve(graf, pot, i, j):
    A, B, C, D = pot[i-1], pot[i], pot[j-1], pot[j % len(pot)]
    d0 = graf[A][B] + graf[C][D]
    d1 = graf[A][C] + graf[B][D]
    if d0 > d1:
        pot[i:j] = pot[j-1:i-1:-1]
        return d1- d0
    return 0


def Lin_Kernighan(graf, zacetna_pot):
    pot = zacetna_pot
    r = 2
    while True:
        if r == 2:
            c = 0
            for (i,j) in vse_kombinacije_2(len(pot)):
                if zamenjaj_dve(graf, pot, i, j) > 0:
                        c += zamenjaj_dve(graf, pot, i, j)
            if c == 0:
                r += 1
        if r == 3:
            d = 0
            for (i, j, k) in vse_kombinacije_3(len(pot)):
                d += zamenjaj_tri(graf, pot, i, j, k)
            
            if d == 0:
                break
            else:
                r = 2
    return pot
                
                        
testna_matrika2 = [[0, 2, 3, 4, 1000],
                 [2, 0, 8, 9, 10],
                 [3, 8, 0, 14, 15],
                 [4, 9, 14, 0, 20],
                 [1000, 10, 15, 20, 0]]

testna_pot = [0, 2, 1, 3, 4]
       
                
resitev = Lin_Kernighan(testna_matrika2, testna_pot)
print('Rešitev je', resitev)
cikel = resitev
cikel.append(resitev[0])

def cena_poti(graf, pot):
    cena = 0
    for i in range(len(pot)-1):
        cena = cena + graf[pot[i]][pot[i+1]]
    return cena

print('Cikel je', cikel, ', in njegova cena je', cena_poti(testna_matrika2, cikel))

            
                
                    
                
                
                
            


























    












    
