import folium
from openrouteservice import convert
import openrouteservice
import json
import time
import requests
from asltam.io.pricedist import get_index

start = time.time()

def trajet(DEPART, ARRIVEE, data_geo, data_price, data_dist):
    i = get_index(data_geo, DEPART)
    j = get_index(data_geo, ARRIVEE)

    x = list(data_geo.iloc[i])[::-1]
    y = list(data_geo.iloc[j])[::-1]
    # Claculer la distance entre le point A et le point B pour pouvoir
    # prendre par la suite la distance la plus courte
    
    r1 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x[0]},{x[1]};{y[0]},{y[1]}?overview=false""")
    routes_1 = json.loads(r1.content)
    route_1 = routes_1.get("routes")[0]
    
    r2 = requests.get(f"http://router.project-osrm.org/route/v1/car/{y[0]},{y[1]};{x[0]},{x[1]}?overview=false""")
    routes_2 = json.loads(r2.content)
    route_2 = routes_2.get("routes")[0]
    
    # Distance entre le point A et le point B :
    dist1 = round(route_1['distance']/1000)
   
    # Distance entre le point B et le point A :
    dist2 = round(route_2['distance']/1000)
    
    # Résolution du problème de la distance différente entre
    # l'aller et le retour avec une boucle
    if dist1 < dist2 :

        coor = [x, y]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')

        m = folium.Map(
                        location=x[::-1],
                        zoom_start=10,
                        control_scale=True)

        for i in range(0, len(coor)-1):
            coord = coor[i], coor[i+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> Distance du trajet :&nbsp" + "<strong>" + str(data_dist.iloc[i][j]) + " Km </strong>" + "</h4></b>"
                price_txt = "<h4> Coût du trajet :&nbsp" + "<strong>" + str(data_price.iloc[i][j]) + " € </strong>" + "</h4></b>"
                moy_txt="<h4> Coût au kilométre :&nbsp" + "<strong>" + str(round(data_price.iloc[i][j]/data_dist.iloc[i][j], 4)) + " €/Km </strong>" + "</h4></b>"

                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt + price_txt + moy_txt, max_width=300)).add_to(m)

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

    elif dist1 > dist2 :

        coor = [y, x]

        client = openrouteservice.Client(key='5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405')
        m = folium.Map(
                        location=y[::-1],
                        zoom_start=10,
                        control_scale=True)

        for i in range(0, len(coor)-1):
            coord = coor[i], coor[i+1]
            res = client.directions(coord)

            with(open('test.json', '+w')) as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))

                geometry = client.directions(coord)['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance_txt = "<h4> Distance du trajet :&nbsp" + "<strong>" + str(data_dist.iloc[i][j]) + " Km </strong>" + "</h4></b>"
                price_txt = "<h4> Coût du trajet :&nbsp" + "<strong>"+str(data_price.iloc[i][j]) + " € </strong>" + "</h4></b>"
                moy_txt = "<h4> Coût au kilométre :&nbsp" + "<strong>" + str(round(data_price.iloc[i][j]/data_dist.iloc[i][j], 4)) + " €/Km </strong>" + "</h4></b>"

                folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+price_txt+moy_txt, max_width=300)).add_to(m)

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

    else:
        print("Veuilliez entrer deux villes différentes")

end = time.time()
print("Temps passé pour exécuter trajet: {0:.5f} s.".format(end - start))
