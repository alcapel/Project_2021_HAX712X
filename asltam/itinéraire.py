import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import folium
import openrouteservice
from openrouteservice import convert

geo = pd.read_csv('data_geo2.csv',index_col=' Nom gare ')

#Initialisent les coordonnées du point de départ et d'arrivée
coor_depart = [geo.loc['MONTPELLIER'][2],geo.loc['MONTPELLIER'][3]]
coor_arrivee = [geo.loc['TOULOUSE SUD-OUEST (SORTIE)'][2],geo.loc['TOULOUSE SUD-OUEST (SORTIE)'][3]]
#Ajoutez un marqueur au point de départ et au point d'arriver
m = folium.Map(location=[43.610769, 3.876716],
               zoom_start=10,
               control_scale=True,
               tiles="cartodbpositron")
folium.Marker([coor_depart[1],coor_depart[0]], 
              popup="Départ").add_to(m)
folium.Marker([coor_arrivee[1], coor_arrivee[0]], 
              popup="Arrivée").add_to(m)

coords = (coor_depart,coor_arrivee)
client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405') 

geometry = client.directions(coords)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

folium.GeoJson(decoded).add_to(m)
m
