# ATTENTION CODE LONG (à cause de fr1)
import osmnx as ox
import os
import networkx as nx
import folium

# Initialisation des données géographiques
url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/Development/asltam/data/dataframe_2.csv'
path = os.path.join(os.getcwd(), 'geo.csv')
gd = download(url, path)

# test pour A9
A9 = gd[gd['route']=='A0009']

# Initialisation du réseau routier (à améliorer)
fr1 = ox.graph_from_point([43.155636, 3.468052], dist=50000, network_type='drive')

# Extraction de ce que l'on veut
a = nx.multigraph.Multigraph()
latt = list(A9['Latt'])
long = list(A9['Long'])

for i in range(8, 18):
    point1 = [long[i], latt[i]]
    point2 = [long[i+1], latt[i+1]]
    depart = ox.get_nearest_node(fr1, point1)
    target = ox.get_nearest_node(fr1, point2)
    a = nx.disjoint_union(a, fr1.subgraph(nx.shortest_path(fr, depart, target, weight='length')))

# affichage du graphe obtenu
ox.folium.plot_graph_folium(a)


# il est presque bon... il y a des moments où le chemin sort de l'autoroute et où les get_nearest_node donne des points en dehors de l'autoroute...
# une fois cela fait pour l'autoroute A9, on pourra généraliser et faire les distances correctement

