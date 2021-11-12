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
              (gare['route'] == 'A0062') | (gare['route'] == 'A0075')]

# Pour exporter en csv
gare_2.to_csv('dataframe.csv')

# le dropna ne sert à rien
gare_2_2 = gare_2.dropna()

# transformation coordonnées GPS
coord = pd.read_csv("dataframe.csv", sep=',')

coord_x = list(coord['x'])
coord_y = list(coord['y'])
coord_gps = []

for i in range(len(coord_x)):
    coord_gps.append(transform(inProj,outProj,coord['x'][i],coord['y'][i]))

coord_gps_x = []
coord_gps_y = []

for i in range(len(coord_gps)):
    coord_gps_x.append(coord_gps[i][0])
    coord_gps_y.append(coord_gps[i][1])

# Création dataframe des coordonnées gps

for i in range(len(coord_gps_x)):
    coord['x'] = np.where(coord['x'] == coord['x'][i], coord_gps_x[i] , coord['x'] )

for i in range(len(coord_gps_y)):
    coord['y'] = np.where(coord['y'] == coord['y'][i], coord_gps_y[i] , coord['y'] )

coord.to_csv('dataframe_2.csv')
