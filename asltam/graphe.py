import pandas as pd
import networkx as nx

price = pd.read_csv('price_data2.csv', index_col=' ')

graphe = nx.Graph(incoming_graph_data = price)
a = nx.shortest_path(graphe, 'Peage de Montpellier St-Jean', 'Bram', weight='weight')