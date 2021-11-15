import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyproj import Proj, transform

# Pour transformer en coordonnées GPS
inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')

# fichier csv originel avec sélection des données qui nous intéresse 
# (coordonnées GPS, nom des gares de péage)
gare = pd.read_csv("gares-peage-2019.csv", sep=';',
                   usecols=["route", "x", "y", ' Nom gare '],
                   index_col=' Nom gare ', decimal=",")
# gare = gare.stack().str.replace(',','.').unstack()

# On prend les lignes dont on a besoin
gare_2 = gare[(gare['route'] == 'A0009') | (gare['route'] == 'A0061') |
              (gare['route'] == 'A0062') | (gare['route'] == 'A0075') | (gare['route'] == 'A0066')] 

# le dropna ne sert à rien
coord = gare_2.dropna()

# Transformation en coordonées GPS 
x=coord['x'].tolist()
y=coord['y'].tolist()
coord['Long'], coord['Latt'] = transform(inProj, outProj, x,y)
del coord['x'], coord['y']
coord.to_csv('data_geo.csv')
