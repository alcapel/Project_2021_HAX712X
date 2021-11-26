import pandas as pd
import networkx as nx


def plus_court_chemin(depart, arrivee):
    ''' 
    Cette fonction calcule le plus court chemin entre le départ et l'arrivée
    '''
    price = pd.read_csv('price_data2.csv', index_col=' ')
    graphe = nx.Graph(incoming_graph_data = price)
    chemin = nx.shortest_path(graphe, depart, arrivee, weight='weight')
    print(chemin)


price = pd.read_csv('price_data2.csv', index_col=' ')
graphe = nx.Graph(incoming_graph_data = price)
b = nx.minimum_spanning_tree(graphe, weight='weight')
nx.draw(b, with_labels = True)
