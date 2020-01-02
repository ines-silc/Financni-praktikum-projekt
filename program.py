import time #Za primerjavo časovne zahtevnosti
import networkx as nx #Za definiranje grafov
import matplotlib.pyplot as mpl #Za risanje grafov

g = nx.MultiGraph()
niz = 'abcdefgh'
g.add_nodes_from(niz)

a = 0
for i in niz:
    a += 1
    for j in niz:
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
