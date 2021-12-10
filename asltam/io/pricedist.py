import numpy as np
import pandas as pd
import time
import networkx as nx


start = time.time()

def average_cost(data_price, data_dist):
    """
    Calcul de la matrice du prix moyen au kilomètre.

    :param DataFrame data_price: Tableau des prix.
    
    :param DataFrame data_dist: Tableau des distances.
    
    :return: * **M** (*array*) - Retourne la matrice des prix moyens.
    """
    n = len(data_price)
    p = np.array(data_price)
    d = np.array(data_dist) + np.diag(np.ones(n))
    return p/d

end = time.time()
print("Temps passé pour exécuter average_cost: {0:.5f} s.".format(end - start))


start = time.time()

def average_cost_list(data_price, data_dist):
    """
    Calcul de la liste du prix moyen au kilomètre.

    :param DataFrame data_price: Tableau des prix.
    
    :param DataFrame data_dist:	Tableau des distances.
    
    :return: * **L** (*list*) - Retourne la partie diagonale inférieure (ou supérieure par symétrie) de la matrice des prix moyens sous forme de liste.
    """
    n = len(data_price)
    p = np.array(data_price)[np.triu_indices(n, k=1)]
    d = np.array(data_dist)[np.triu_indices(n, k=1)]
    # le np.triu_indices permet de sélectionner juste ce
    # qu'il y a en dessous de la diagonale de la matrice
    return p/d

end = time.time()
print("Temps passé pour exécuter average_cost_list: {0:.5f} s.".format(end - start))


start = time.time()


def get_index(data, name):
    """
    Retourne la valeur de la position de name en tant qu'index.
    
    :param DateFrame data: Un tableau de données.
    
    :param str or list name: Nom(s) d'index du tableau de données data.
    
    :return: * **I** (*int or list*) - Donne la/les positions(s) de name dans l'index de data.
    """
    if type(name) == str:
        #  dans le cas où l'on veut qu'un seul index.
        i = 0
        while i < len(data) and name != data.index[i]:
            i += 1
        return i
    elif type(name) == list:
        # dans le cas où on veut une liste de plusieurs index.
        ind = []
        for j in range(len(name)):
            i = 0
            while i < len(data) and name[j] != data.index[i]:
                i += 1
            ind.append(i)
        return ind
    
end = time.time()
print("Temps passé pour exécuter get_index: {0:.5f} s.".format(end - start))


start = time.time()

def get_way(data_dist, start, target):
    """
    Renvoie une liste contenant les péages entre start et target.
    Notre méthode se base sur le fait que l'algorithme de Kruskal nous
    fournit un graphe du réseau routier avec seulement des arêtes
    entre deux gares successives dont on déduit trivialement la liste
    avec un algorithme du plus court chemin (ici Dijkstra).
    
    :param DataFrame data_dist: Tableau de données sous forme de matrice de distances entre toutes les gares.
    
    :param str start: La gare de départ (doit être une élément de data_dist.columns).
    
    :param str target: La gare d'arrivée (doit être une élément de data_dist.columns).
    
    :return: * **L** (*list*) - Liste des péages situés sur le trajet autoroutier le plus court de start à target.
    """
    G = nx.Graph(incoming_graph_data=data_dist)
    a = nx.minimum_spanning_tree(G, weight='weight')
    return nx.shortest_path(a, start, target, weight='weight')

end = time.time()
print("Temps passé pour exécuter get_way : {0:.5f} s.".format(end - start))
