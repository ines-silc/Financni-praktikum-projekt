import time #Za primerjavo časovne zahtevnosti
import networkx as nx #Za definiranje grafov
import matplotlib.pyplot as mpl #Za risanje grafov
import random
import itertools

g = nx.MultiGraph()
sez = [1, 2, 3, 4, 5, 6, 7, 8]
g.add_nodes_from(sez)

a = 0
for i in sez:
    a += 1
    for j in sez:
        a += 1
        if i == j:
            pass
        else:        
            g.add_weighted_edges_from([(i, j, a)])
        
h = nx.complete_graph(8)

##Primer risanja grafa:
##nx.draw(g, pos = nx.circular_layout(g), , with_labels = True)
##nx.draw_networkx_edge_labels(g, pos = nx.circular_layout(g), labels = nx.get_edge_attributes(g, 'weight').values())
##mpl.show()

##Kaj bomo potrebovali pri algoritmu:
##Vsaka pot trgovca bo morala imeti vsa vozlišča zato vedno preverimo:

## pot.order() == originalen_graf.order()

##Vsaka pot trgovca bo morala imeti točno toliko povezav kot vozlišč:

## pot.size(weight = None) == pot.order()

##Dolžina poti: pot.size()

##Pretvorimo graf v matriko, za izvajanje algoritma:
##Še ni čisto ok naslednji funkcija !!!!!!!!!!
def pretvori_graf_v_matriko(graf):
    m = nx.attr_matrix(graf, edge_attr = 'weight')[0]
    gm = []
    for i in range(len(m[0])-1):
        for j in range(len(m)-1):
            gm[i][j]= m[i, j]
    return gm

##Pretvorimo matriko v graf:

def pretvori_matriko_v_graf(matrika):
    g = nx.MultiGraph()
    for i in range(len(matrika[0])):
        for j in range(len(matrika)):
            if i == j:
                g.add_edge(i, j)
            else:
                if matrika[i][j] == 0:
                    pass
                else:
                    g.add_weighted_edges_from([(i, j, matrika[i][j])])
    return g

#V nadaljevanju bo algoritem osnovan na delu z matriko

def cena_poti(graf, pot):
    cena = 0
    for i in range(len(pot)-1):
        cena = cena + graf[pot[i]][pot[i+1]]
    return cena

def dva_opt(graf, pot):
    najboljsa_pot = pot
    cena = cena_poti(graf, pot)
    print('Prvotna pot je', pot)
    print('Cena prvotne poti je', cena)
    izboljsanje = True
    while izboljsanje:
        izboljsanje = False
        for i in range(1,len(pot) - 2):
            #print('delam prvo')
            for j in range(i + 1, len(pot)):
                #print('delam drugo')
                if j - i == 1: continue
                nova_pot = pot[:]
                nova_pot[i:j] = pot[j - 1:i - 1:-1]
                nova_cena = cena_poti(graf, nova_pot) # popravi samo glede na spremenjene povezave
                #print('cena nove poti je', cena_poti(graf, nova_pot))
                if nova_cena < cena:
                    najboljsa_pot = nova_pot[:]
                    cena = nova_cena
                    #print(najboljsa_pot)
                    #print('cena najboljše poti je', cena_poti(graf, najboljsa_pot))
                    #print(izboljsanje)
                    izboljsanje = True
        pot = najboljsa_pot
        print('Najboljša pot je', pot, 'in njena dolžina je', cena_poti(graf, pot))
    return (pot, cena)

##testna_matrika2 = [[0, 2, 3, 4, 1000],
##                 [2, 0, 8, 9, 10],
##                 [3, 8, 0, 14, 15],
##                 [4, 9, 14, 0, 20],
##                 [1000, 10, 15, 20, 0]]
##
##poti_in_cene = []
##for i in range(0, len(list(itertools.permutations(range(5)))), 30):
##    prvotna_pot = list(list(itertools.permutations(range(5)))[i])
##    izhodisce = prvotna_pot[0]
##    prvotna_pot.append(izhodisce)   
##    (a, b) = dva_opt(testna_matrika2, prvotna_pot)
##    poti_in_cene.append((a, b))
##
##poti_in_cene.sort(key=lambda elem: elem[1])
##print('Vse poti so', poti_in_cene)
##print('Najboljša rešitev je', poti_in_cene[0])
##
##tg2 = pretvori_matriko_v_graf(testna_matrika2)
##nx.draw(tg2, pos = nx.circular_layout(tg2), with_labels = True)
##nx.draw_networkx_edge_labels(tg2, pos = nx.circular_layout(tg2), labels = nx.get_edge_attributes(tg2, 'weight').values())
##mpl.show()
##
##najboljsa_pot = poti_in_cene[0][0]

def pretvori_resitev_v_matriko(najboljsa_pot, graf):
    matrika = [[0 for col in range(len(graf))] for row in range(len(graf))]
    for i in range(len(najboljsa_pot)-1):
        print('Na mesto', najboljsa_pot[i], najboljsa_pot[i+1], 'dodajam element', graf[najboljsa_pot[i]][najboljsa_pot[i+1]])
        matrika[najboljsa_pot[i]][najboljsa_pot[i+1]] = graf[najboljsa_pot[i]][najboljsa_pot[i+1]]
    print('Matrika rešitve je', matrika)
    return matrika



