def zamenjaj(graf, pot, i, j, k):
    A, B, C, D, E, F = pot[i-1], pot[i], pot[j-1], pot[j], pot[k-1], pot[k % len(pot)]
    d0 = graf[A][B] + graf[C][D] + graf[E][F]
    d1 = graf[A][C] + graf[B][D] + graf[E][F]
    d2 = graf[A][B] + graf[C][E] + graf[D][F]
    d3 = graf[A][D] + graf[E][B] + graf[C][F]
    d4 = graf[F][B] + graf[C][D] + graf[E][A]

    if d0 > d1:
        pot[i:j] = reversed(pot[i:j])
        return -d0 + d1
    elif d0 > d2:
        pot[j:k] = reversed(pot[j:k])
        return -d0 + d2
    elif d0 > d4:
        pot[i:k] = reversed(pot[i:k])
        return -d0 + d4
    elif d0 > d3:
        a = pot[j:k] + pot[i:j]
        pot[i:k] = a
        return -d0 + d3
    return 0

def tri_opt(graf, pot):
    while True:
        delta = 0
        for (i, j, k) in vse_kombinacije(len(pot)):
            delta += zamenjaj(graf, pot, i, j, k)
        if delta >= 0:
            break
    return pot

def vse_kombinacije(n):
    return ((i, j, k)
        for i in range(n)
        for j in range(i + 2, n)
        for k in range(j + 2, n + (i > 0)))

testna_matrika2 = [[0, 2, 3, 4, 1000],
                 [2, 0, 8, 9, 10],
                 [3, 8, 0, 14, 15],
                 [4, 9, 14, 0, 20],
                 [1000, 10, 15, 20, 0]]

testna_pot = [0, 2, 1, 3, 4]

resitev = tri_opt(testna_matrika2, testna_pot)
print('Rešitev je', resitev)
cikel = resitev
cikel.append(resitev[0])

def cena_poti(graf, pot):
    cena = 0
    for i in range(len(pot)-1):
        cena = cena + graf[pot[i]][pot[i+1]]
    return cena

print('Cikel je', cikel, ', in njegova cena je', cena_poti(testna_matrika2, cikel))
