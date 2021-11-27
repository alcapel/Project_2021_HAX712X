#%%
from download import download
import pandas as pd
import folium
import osmnx as ox
from openrouteservice import convert
import openrouteservice
import json 
from ipywidgets import interact

#%%
url = 'https://raw.githubusercontent.com/Eldohrim/Project_2021_HAX712X/main/asltam/data/data_geo2.csv'
path = os.path.join(os.getcwd(), 'data_geo2.csv')
download(url, path, replace=False)

geo = pd.read_csv('./data_geo2.csv')

geo=geo.rename(columns={' Nom gare ':'gare'})
#%%
depart=sorted(geo.gare.unique())
arrivee=sorted(geo.gare.unique())

def trajet(DEPART,ARRIVEE):
    if geo.loc[geo['gare']==DEPART].index[0] < geo.loc[geo['gare']==ARRIVEE].index[0] :
        x = [geo['Long'][geo.loc[geo['gare']==DEPART].index[0]], geo['Latt'][geo.loc[geo['gare']==DEPART].index[0]]]
        y = [geo['Long'][geo.loc[geo['gare']==ARRIVEE].index[0]], geo['Latt'][geo.loc[geo['gare']==ARRIVEE].index[0]]]
        coor = [x, y]
        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')# Specify your personal API key
        c = folium.Map(location=[43.1837661,3.0042121],zoom_start=10, control_scale=True)
        for i in range (0,len(coor)-1):
            coord = coor[i],coor[i+1]
            res = client.directions(coord)
            with(open('test.json','+w')) as f:
                f.write(json.dumps(res,indent=4, sort_keys=True))
                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"        

                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt,max_width=300)).add_to(c)
                folium.Marker(coord[0][::-1], popup=DEPART, tooltip = "Click me!").add_to(c)
                folium.Marker(coord[1][::-1], popup=ARRIVEE, tooltip = "Click me!").add_to(c)
        return c
    elif geo.loc[geo['gare']==DEPART].index[0] > geo.loc[geo['gare']==ARRIVEE].index[0] :
        y = [geo['Long'][geo.loc[geo['gare']==DEPART].index[0]],geo['Latt'][geo.loc[geo['gare']==DEPART].index[0]]]
        x = [geo['Long'][geo.loc[geo['gare']==ARRIVEE].index[0]],geo['Latt'][geo.loc[geo['gare']==ARRIVEE].index[0]]]
        coor = [x, y]
        m = folium.Map(location=[43.1837661,3.0042121],zoom_start=10, control_scale=True)
        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')
        for i in range (0,len(coor)-1):
            coord = coor[i],coor[i+1]
            res = client.directions(coord)
            with(open('test.json','+w')) as f:
                f.write(json.dumps(res,indent=4, sort_keys=True))
                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"        

                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt,max_width=300)).add_to(m)
                folium.Marker(coord[0][::-1], popup=DEPART, tooltip = "Click me!").add_to(m)
                folium.Marker(coord[1][::-1], popup=ARRIVEE, tooltip = "Click me!").add_to(m)
        return m
    else :
        print("Veuilliez entrer deux villes différentes")           
interact(trajet, DEPART=depart, ARRIVEE=arrivee)