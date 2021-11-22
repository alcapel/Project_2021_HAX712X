# Nous commençons par importer la bibliothèque "pyroutelib3"
# qui nous permettra de calculer le trajet

from pyroutelib3 import Router
import folium


coor_depart = [43.56321197997598, 3.832152851175532]
coor_arrivee = [43.17658759196942, 3.034479741724844]


def trajet(coord_depart, coord_arrivee):
    """
    Cette fonction affiche une carte avec le trajet souhaité !
    """
    # Les 3 lignes suivantes initialisent les coordonnées
    # du point de départ et du point d'arrivée.
    c = folium.Map(location=[43.610769, 3.876716], zoom_start=15)

    # Ajoute un marqueur au point de départ et au point d'arrivée.
    folium.Marker(coor_depart, popup="Départ").add_to(c)
    folium.Marker(coor_arrivee, popup="Arrivée").add_to(c)

    # Définir le véhicule qui sera utilisé pour effectuer le trajet.
    # Dans notre cas, nous utilisons une voiture ("car").
    router = Router("car")

    # Les 2 lignes suivantes recherchent
    # le point de départ et le point d'arrivée.
    depart = router.findNode(coor_depart[0], coor_depart[1])
    arrivee = router.findNode(coor_arrivee[0], coor_arrivee[1])

    # Cette ligne permet d'effectuer le calcul de l'itinéraire.
    status, route = router.doRoute(depart, arrivee)

    # La dernière ligne est exécutée uniquement
    # si le calcul est mené à son terme.
    if status == 'success':
        routeLatLons = list(map(router.nodeLatLon, route))

    # Afficher une ligne bleu sur la route.
    folium.PolyLine(routeLatLons, color="blue", weight=2.5, opacity=1).add_to(c)

    return c
