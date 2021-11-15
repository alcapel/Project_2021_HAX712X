import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
price = pd.read_csv("price-data.csv", sep=';')
price.info()

#%%
#Suppression
del price['Vendargues']
del price['Montpellier est']
del price['Montpellier sud']
del price['Le Boulou (peage sys ouvert)']
del price['Montpellier ouest']
del price['St-Jean-de-Vedas']
del price['La Croix Daurade']
del price['Borderouge']
del price['Les lzards']
del price['Sesquieres']
del price['Montaudran']
del price['Lasbordes']
del price['Soupetrad']
del price['La Roseraie']
del price['Pamiers nord']
del price['Pamiers sud']
price=price.drop(index=[0,1,2,3,4,18,29,30,35,36,37,38,39,40,41,42])

#%%
price=price.fillna(0)
#%%
price.to_csv('price_data2.csv')
