import numpy as np
import pandas as pd
import os
from download import download
import requests
import json
import time


start = time.time()
def distance():
    '''
    Cette fonction nous sert à créer le dataframe des distances
    '''
    # Chargement des données géographiques
    url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/main/asltam/data/data_geo2.csv'
    path = os.path.join(os.getcwd(), 'data_geo2.csv')
    download(url, path, replace=False)
    geo = pd.read_csv('./data_geo2.csv')

    # Initialisation des coordonnées
    latt = list(geo['Latt'])
    long = list(geo['Long'])
    coor = []
    n = len(long)
    for i in range(n):
        coor.append([long[i], latt[i]])

    # Création de la matrice des distances
    D = np.zeros((n, n))

    for i in range(n):
        # La matrice est diagonale
        # On ne construit donc que la diagonale supérieure
        x, y = coor[i]
        for j in range(i, n):
            # On calcule les deux sens car la requête suit
            # le sens de la route : on prend la distance la plus petite,
            # qui sera la plus vraisemblable
            x1, y1 = coor[j]
            r1 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")
            routes_1 = json.loads(r1.content)
            route_1 = routes_1.get("routes")[0]
            r2 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x1},{y1};{x},{y}?overview=false""")
            routes_2 = json.loads(r2.content)
            route_2 = routes_2.get("routes")[0]
            D[i, j] = min(round(route_1['distance']/1000),
                          round(route_2['distance']/1000))

    # On symétrise la matrice pour avoir le tableau de données complet
    Df = D + D.T

    # Création du dataframe
    dist = pd.DataFrame(Df)
    dist.rename(columns=geo[' Nom gare '], inplace=True)
    dist.set_index(geo[' Nom gare '], inplace=True)

    dist.to_csv('./data_dist.csv')

end = time.time()
print("Temps passé pour exécuter distance: {0:.5f} s.".format(end - start))
