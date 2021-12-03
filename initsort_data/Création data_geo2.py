#Importation des packages 
import numpy as np
import pandas as pd
from download import download
import os

# chargement des données géographiques
url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/main/asltam/data/data_geo.csv'
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

geo.to_csv('data_geo2.csv')
