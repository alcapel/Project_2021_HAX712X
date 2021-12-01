import numpy as np
import pandas as pd


def average_cost(data_price, data_dist):
    """
    Retourne la matrice des prix moyens.
    """
    n = len(data_price)
    p = np.array(data_price)
    d = np.array(data_dist)
    return p/d


def average_cost_list(data_price, data_dist):
    """
    Retourne la liste des prix moyens.
    """
    n = len(data_price)
    p = np.array(data_price)[np.triu_indices(n, k=1)]
    d = np.array(data_dist)[np.triu_indices(n, k=1)]
    return p/d
  
def get_index(data, name):
    """
    Retourne la valeur de la position de la gare de péage dans le DataFrame

    Attributs :
    -----------
    data : pd.DataFrame, dont les colonnes porte le nom des péages
    name : str ou list, nom(s) d'une gare de péage de data
    """
    if type(name) == str:
        try:
            data[name] + 0 == 1
            i = 0
            while i < len(data) and name != data.columns[i]:
                i += 1
            return i
        except Exception as a:
            print(f"Attention ! {a} n'appartient pas à la base de donnée.")
    elif type(name) == list:
        ind = []
        try:
            data[name] + 0 == 1
            for j in range(len(name)):
                i = 0
                while i < len(data) and name[j] != data.columns[i]:
                    i += 1
                ind.append(i)
            return ind
        except Exception as a:
            print(f"Attention ! {a} n'appartient pas à la base de donnée.")

def get_way(data_dist, start, target):
    """
    Renvoie une liste contenant les péages entre start et target.
    Notre méthode se base sur le fait que l'algorithme de Kruskal nous
    fournit un graphe du réseau routier avec seulement des arêtes
    entre deux gares successives dont on déduit facilement la liste
    avec un algorithme du plus court chemin (ici Dijkstra).
    Attributs
    ---------
    data_dist : DataFrame, tableau de données sous forme de matrice de distance entre toutes les gares.
    start : str, la gare de départ (doit être une élément de data_dist.columns).
    target : str, la gare d'arrivée (doit être une élément de data_dist.columns).
    """
    G = nx.Graph(incoming_graph_data=data_dist)
    a = nx.minimum_spanning_tree(G, weight='weight')
    return nx.shortest_path(a, start, target, weight = 'weight')
