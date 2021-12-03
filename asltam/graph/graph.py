import networkx as nx
from itertools import combinations
from asltam.io.load_price import load_price
from asltam.io.pricedist import get_index, get_way
import time


start = time.time()


def get_subgraph_under_k(data, k):
    """
    Renvoie une liste contenant tous les sous-graphes induits par data, de taille inférieure ou égal à k.
    Attributs
    ---------
    data : DataFrame ou array,
    k : int, déterminant la taille maximale des sous-graphes.

    """
    n = len(data)
    graphes = []
    for j in range(k+1):
        for i in combinations(range(1, n-1), j):
            sub = [0] + list(i) + [n-1]
            g = load_price.subdata_price(data, sub)
            graphes.append(nx.Graph(incoming_graph_data=g))
    return graphes

end = time.time()
print("Temps passé pour exécuter get_subgraph_under_k : {0:.5f} s.".format(end - start))


start = time.time()


def kmin_cost_out(data_price, data_dist, start, target, k):
    """
    Calcule le trajet de frais minimum avec la contrainte d'au maximum k entrées/sorties d'autoroute. Renvoie le prix, et les gares de sortie.
    Attributs
    ---------
    data_price : DataFrame, tableau des prix.
    data_dist : DataFrame, tableau des distances.
    start : str, gare d'entrée.
    target : str, gare de sortie.
    k : int, nombre maximum d'entrées/sorties.

    """
    a = get_way(data_dist, start, target)
    road = load_price.subdata_price(data_price, get_index(data_dist, a))
    opt = nx.Graph(incoming_graph_data=road).size(weight='weight')
    graphes = get_subgraph_under_k(road, k)
    i_opt = 0
    for i in range(len(graphes)):
        path = nx.minimum_spanning_tree(graphes[i], weight='weight')
        pds = path.size(weight='weight')
        if pds < opt:
            i_opt = i
            opt = pds
    g = list(graphes[i_opt].nodes)
    return g, opt

end = time.time()
print("Temps passé pour exécuter kmin_cost_out: {0:.5f} s.".format(end - start))
