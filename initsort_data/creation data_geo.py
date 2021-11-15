import pandas as pd
import os
from download import download
from pyproj import Proj, transform

# Pour transformer en coordonnées GPS
inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')

# fichier csv originel avec sélection des données qui nous intéresse 
# (coordonnées GPS, nom des gares de péage)
url = 'https://static.data.gouv.fr/resources/gares-de-peage-du-reseau-routier-national-concede/20210224-175626/gares-peage-2019.csv'
path = os.path.join(os.getcwd(), 'gares-peage-2019.csv')
download(url, path, replace=False)

gare = pd.read_csv("./gares-peage-2019.csv", sep=';',
                   usecols=["route", "x", "y", ' Nom gare '],
                   index_col=' Nom gare ', decimal=",")

# On prend les lignes dont on a besoin
coord = gare[(gare['route'] == 'A0009') | (gare['route'] == 'A0061') |
             (gare['route'] == 'A0062') | (gare['route'] == 'A0075') | 
             (gare['route'] == 'A0066')] 


# Transformation en coordonées GPS 
x=coord['x'].tolist()
y=coord['y'].tolist()
coord['Long'], coord['Latt'] = transform(inProj, outProj, x, y)
del coord['x'], coord['y']
coord.to_csv('data_geo.csv')
