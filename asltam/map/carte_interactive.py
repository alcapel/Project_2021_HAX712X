import folium
from openrouteservice import convert
import openrouteservice
import json
import time
import requests
from asltam.io.pricedist import get_index

start = time.time()

def trajet(DEPART, ARRIVEE, geo, price, dist):
    i = get_index(geo, DEPART)
    j = get_index(geo, ARRIVEE)    
    # Résolution du problème de la distance différente entre
    # l'aller et le retour avec une boucle
    if i < j:
        x = list(geo.iloc[i])[::-1]
        y = list(geo.iloc[j])[::-1]
        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')  # Specify your personal API key

        m = folium.Map(
                        location=[43.1837661, 3.0042121],
                        zoom_start=10,
                        control_scale=True)

        for k in range(0, len(coor)-1):
            coord = coor[k], coor[k+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> Distance du trajet :&nbsp" + "<strong>"+str(dist.iloc[i][j])+" Km </strong>" +"</h4></b>" 
                price_txt = "<h4> Coût du trajet :&nbsp" + "<strong>"+str(price.iloc[i][j])+" € </strong>" +"</h4></b>" 
                moy_txt="<h4> Coût au kilométre :&nbsp" + "<strong>"+str(round(price.iloc[i][j]/dist.iloc[i][j],4))+" €/Km </strong>" +"</h4></b>"
                
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
        y = list(geo.iloc[i])[::-1]
        x = list(geo.iloc[j])[::-1]
        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')
        m = folium.Map(
                        location=[43.1837661, 3.0042121],
                        zoom_start=10,
                        control_scale=True)

        for k in range(0, len(coor)-1):
            coord = coor[k], coor[k+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> Distance du trajet :&nbsp" + "<strong>"+str(dist.iloc[i][j])+" Km </strong>" +"</h4></b>" 
                price_txt = "<h4> Coût du trajet :&nbsp" + "<strong>"+str(price.iloc[i][j])+" € </strong>" +"</h4></b>" 
                moy_txt="<h4> Coût au kilométre :&nbsp" + "<strong>"+str(round(price.iloc[i][j]/dist.iloc[i][j],4))+" €/Km </strong>" +"</h4></b>" 

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
end = time.time()
print("Temps passé pour exécuter trajet: {0:.5f} s.".format(end - start))
