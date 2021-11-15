import numpy as np
import pandas as pd
import os
from download import download
import requests
import json

# chargement des données géographiques
url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/Development/asltam/data/data_geo.csv'
path = os.path.join(os.getcwd(),'data_geo.csv')
download(url, path, replace=False)
geo = pd.read_csv('./data_geo.csv')

# on réindexe pour avoir les données dans l'ordre
geo = geo.drop(index=[0, 1, 2, 3, 4, 5, 6, 7, 20, 21, 29, 30, 
                      31, 32, 33, 34, 35, 36, 37, 38, 39, 
                      40, 41, 42, 43, 44, 45, 46, 50, 52])

geo = geo.reset_index()
del geo['index']
geo = geo.reindex([0, 1, 2, 22, 3, 4, 5, 6, 7, 8,
                   9, 11, 10, 18, 17, 16, 15, 14, 
                   13, 19, 20, 21, 12])

geo = geo.reset_index()
del geo['index']

# Initialisation des coordonnées
latt = list(geo['Latt'])
long = list(geo['Long'])
coor = []
n = len(long)
for i in range(n):
    coor.append([long[i],latt[i]])
    
# Création de la matrice des distances

D = np.zeros((n, n))

for i in range(n):
    # On ne construit que la diagonale supérieure car la matrice est diagonale
    x, y = coor[i]
    for j in range(i, n):
        # On calcule les deux sens car la requête suit 
        #le sens de la route : on prend la distance la plus petite qui sera la plus vraisemblable
        x1, y1 = coor[j]
        r1 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")
        routes_1 = json.loads(r1.content)
        route_1 = routes_1.get("routes")[0]
        r2 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x1},{y1};{x},{y}?overview=false""")
        routes_2 = json.loads(r2.content)
        route_2 = routes_2.get("routes")[0]
        D[i, j] = min(round(route_1['distance']/1000),round(route_2['distance']/1000))

# On symétrise la matrice pour avoir le tableau de données complet
Df = D + D.T

# Création du dataframe
dist = pd.DataFrame(Df)
dist.rename(columns=geo[' Nom gare '], inplace=True)
dist.set_index(geo[' Nom gare '], inplace=True)

dist.to_csv('./data_dist.csv')
