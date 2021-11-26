def get_way(data_dist, start, target):
    """
    Renvoie une liste contenant les péages entre départ et arrivee.
    """
    G = nx.Graph(incoming_graph_data=data_dist)
    a = nx.minimum_spanning_tree(G, weight='weight')
    return nx.shortest_path(a, start, target, weight = 'weight')
  
