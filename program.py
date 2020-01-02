import time #Za primerjavo časovne zahtevnosti
import networkx as nx #Za definiranje grafov
import matplotlib.pyplot as mpl #Za risanje grafov
import random

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
##nx.draw(g, pos = nx.circular_layout(g))
##nx.draw_networkx_edge_labels(g, pos = nx.circular_layout(g), labels = nx.get_edge_attributes(g, 'weight').values())
##mpl.show()

##Kaj bomo potrebovali pri algoritmu:
##Vsaka pot trgovca bo morala imeti vsa vozlišča zato vedno preverimo:

## pot.order() == originalen_graf.order()

##Vsaka pot trgovca bo morala imeti točno toliko povezav kot vozlišč:

## pot.size(weight = None) == pot.order()

##Dolžina poti: pot.size()

##Pretvorimo graf v matriko, za izvajanje algoritma:

gm = nx.attr_matrix(g, edge_attr = 'weight')[0]

##Pretvorimo matriko v graf:

def pretvori_matriko_v_graf(matrika):
    slovar = dict()
    for i in range(len(matrika[0])):
        for j in range(len(matrika)):
            if i == j:
                pass
            else:
                slovar[i] = {j: {'weight' : matrika[i][j]}}
    graf = nx.from_dict_of_dicts(slovar)
    return graf





