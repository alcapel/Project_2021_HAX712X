import networkx as nx
from itertools import combinations
from asltam.io.load_price import load_price
from asltam.io.pricedist import get_index, get_way
import time


start = time.time()


def get_subgraph_under_k(data, k):
    """
    Renvoie une liste contenant tous les 
    sous-graphes induits par data, de taille 
    inférieure ou égal à k.

    :param DataFrame or Array data:

    :param int k : Déterminant la taille maximale des 
    sous-graphes.

    :return list L: Une liste de graphe.
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
    Calcule le trajet de frais minimum avec la 
    contrainte d'au maximum k entrées/sorties 
    d'autoroute. Renvoie le prix, et les gares
    de sortie. Attention les tableaux de prix et de
    distances doivent être compatibles.

    Paramètres
    ----------
    :param DataFrame data_price: Tableau des prix.

    :param DataFrame data_dist: Tableau des distances.

    :param str start: Gare d'entrée.

    :param str target: Gare de sortie.

    :param int k: Nombre maximum d'entrées/sorties.

    :returns list L: La liste des sorties à prendre.
    :returns float opt: Renvoie le coût totaldu trajet.
    
    :examples:
    .. code:: python
    
        >>> import asltam as atm
        >>> prix = atm.load_price().save_as_price(index=' ')
        >>> dist = atm.load_dist().save_as_dist(index=' Nom gare ')
        >>> start = 'MONTPELLIER'
        >>> target = 'LEUCATE'
        >>> g, opt = atm.kmin_cost_out(prix, dist, start, target, 4)
        >>> print(g, opt)
        ['MONTPELLIER', 'SETE', 'AGDE', 'BEZIERS OUEST', 'LEUCATE'] 9.0
        
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
