import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyproj import Proj, transform

# Pour transformer en coordonnées GPS
inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')

# fichier csv originel
gare = pd.read_csv("gares-peage-2019.csv", sep=';', usecols=["route","x", "y",' Nom gare '], index_col = ' Nom gare ',decimal=",")
#gare = gare.stack().str.replace(',','.').unstack()
# On prend les colonnes dont on a besoin
gare_2= gare[(gare['route']== 'A0009') | (gare['route']== 'A0061') | (gare['route']== 'A0062') |  (gare['route']== 'A0075')] 

# Pour exporter en csv
gare_2.to_csv('dataframe.csv')

# le dropna ne sert à rien
gare_2_2 = gare_2.dropna()

# transformation coordonnées GPS
coord = pd.read_csv("dataframe.csv", sep=',')


