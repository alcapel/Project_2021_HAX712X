from download import download
import pandas as pd
import folium
import osmnx as ox
from openrouteservice import convert
import openrouteservice
import json
from ipywidgets import interact

url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/main/asltam/data/data_geo2.csv'
path = os.path.join(os.getcwd(), 'data_geo2.csv')
download(url, path, replace=False)
geo = pd.read_csv('./data_geo2.csv')
geo = geo.rename(columns={' Nom gare ':'gare'})

url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/main/asltam/data/data_dist.csv'
path = os.path.join(os.getcwd(), 'data_dist.csv')
download(url, path, replace=False)
dist = pd.read_csv('./data_dist.csv',index_col=' Nom gare ')

url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/main/asltam/data/price_dataf2.csv'
path = os.path.join(os.getcwd(), 'price_dataf2.csv')
download(url, path, replace=False)
price = pd.read_csv('./price_dataf2.csv')


# Crée une liste qui contient le nom de toutes les villes
villes = sorted(geo.gare.unique())


def trajet(DEPART, ARRIVEE):
    i=geo.loc[geo['gare'] == DEPART].index[0]
    j=geo.loc[geo['gare'] == ARRIVEE].index[0]
    
    # Résolution du problème de la distance différente entre
    # l'aller et le retour avec une boucle
    if i < j:

        x = [geo['Long'][i], 
             geo['Latt'][i]]
        
        y = [geo['Long'][j], 
             geo['Latt'][j]]

        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')  # Specify your personal API key

        m = folium.Map(
                        location=[43.1837661, 3.0042121],
                        zoom_start=10,
                        control_scale=True)

        for i in range(0, len(coor)-1):
            coord = coor[i], coor[i+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> Distance du trajet :&nbsp" + "<strong>"+str(dist[DEPART][j])+" Km </strong>" +"</h4></b>" 
                price_txt = "<h4> Coût du trajet :&nbsp" + "<strong>"+str(price[DEPART][j])+" € </strong>" +"</h4></b>" 
                moy_txt="<h4> Coût au kilométre :&nbsp" + "<strong>"+str(round(price[DEPART][j]/dist[DEPART][j],4))+" €/Km </strong>" +"</h4></b>"
                
                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+price_txt+moy_txt,max_width = 300)).add_to(m)

                folium.Marker(
                            coord[0][::-1],
                            popup=DEPART,
                            icon=folium.Icon(color='red', icon='car', prefix='fa')
                             ).add_to(m)

                folium.Marker(
                            coord[1][::-1],
                            popup=ARRIVEE,
                            icon=folium.Icon(color='red', icon='car', prefix='fa')
                             ).add_to(m)
        return m

    elif i > j:

        y = [geo['Long'][i],
             geo['Latt'][i]]
        
        x = [geo['Long'][j],
             geo['Latt'][j]]

        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')
        m = folium.Map(
                        location=[43.1837661, 3.0042121],
                        zoom_start=10,
                        control_scale=True)

        for i in range(0, len(coor)-1):
            coord = coor[i], coor[i+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> Distance du trajet :&nbsp" + "<strong>"+str(dist[DEPART][j])+" Km </strong>" +"</h4></b>" 
                price_txt = "<h4> Coût du trajet :&nbsp" + "<strong>"+str(price[DEPART][j])+" € </strong>" +"</h4></b>" 
                moy_txt="<h4> Coût au kilométre :&nbsp" + "<strong>"+str(round(price[DEPART][j]/dist[DEPART][j],4))+" €/Km </strong>" +"</h4></b>" 

                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+price_txt+moy_txt,max_width = 300)).add_to(m)

                folium.Marker(
                            coord[0][::-1],
                            popup=DEPART,
                            icon=folium.Icon(color='red', icon='car', prefix='fa')
                             ).add_to(m)

                folium.Marker(
                            coord[1][::-1],
                            popup=ARRIVEE,
                            icon=folium.Icon(color='red', icon='car', prefix='fa')
                             ).add_to(m)
        return m
    
    else :
        print("Veuilliez entrer deux villes différentes")  

interact(trajet, DEPART = villes, ARRIVEE = villes)
