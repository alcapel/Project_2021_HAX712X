import networkx as nx

def get_way(data_dist, start, target):
    """
    Renvoie une liste contenant les péages entre start et target. Notre méthode se
    base sur le fait que l'algorithme de Kruskal nous fournit un graphe du réseau routier 
    avec seulement des arêtes entre deux gares successives dont on déduit facilement la liste
    avec un algorithme du plus court chemin (ici Dijkstra).
    
    Attributs
    ---------
    data_dist : DataFrame, tableau de données sous forme de matrice de distance entre toutes les gares.
    start : str, la gare de départ (doit être une élément de data_dist.columns).
    target : str, la gare d'arrivée (doit être une élément de data_dist.columns).
    """
    G = nx.Graph(incoming_graph_data=data_dist)
    a = nx.minimum_spanning_tree(G, weight='weight')
    return nx.shortest_path(a, start, target, weight='weight')
  
