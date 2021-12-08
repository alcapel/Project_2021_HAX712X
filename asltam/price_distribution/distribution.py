import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import seaborn as sns
import time
from asltam.io.load_dist import load_dist
from asltam.io.load_price import load_price
from asltam.io.pricedist import average_cost_list, get_index, get_way


start = time.time()
def kde_gare(
            all,
            data_price,
            data_dist,
            start,
            target,
            bw):
    """
    Affiche la distribution des prix au kilomètre entre deux 
    gares de péages sur un trajet donné (ou sur tout le 
    réseau). 
    
    .. warning:: 
            Attention, les données de distance et de prix 
            doivent être compatible pour pouvoir avoir 
            des résultats cohérents. 
            
            Voir la documentation pour la compatibilité.

    :param bool all: Si True affiche la distribution sur le DataFrame entier.
    
    :param DataFrame data_price: Tableaux de données de prix entre les gares de péage.
    
    :param DataFrame data_dist: Tableaux de données des distances entre les gares de péage.
    
    :param str start: Nom de la première gare.
    
    :param str target: Nom de la seconde gare.
    
    :param float bw: Voir doc bw_adjust de seaborn.
    
    :returns:
    None.
    
    :examples:
    .. code:: python
    	
            >>> import asltam as atm
            >>> prix = atm.load_price().save_as_price(index=' ')
            >>> dist = atm.load_dist().save_as_dist(index=' Nom gare ')
    	>>> atm.kde_gare(True, prix, dist, 1)
    """
    if all:
        m = average_cost_list(data_price, data_dist)
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
        sns.kdeplot(m, shade=True, cut=0, bw_adjust=bw)
        plt.ylabel("Density level")
        plt.title("KDE pour le prix au kilomètre")
        plt.tight_layout()
        plt.show()

    elif start == target:
        print("Ce sont les mêmes gares : il n'y a rien à afficher.")
    else:
        i = get_index(data_price, start)
        j = get_index(data_price, target)
        route = get_way(data_dist, data_dist.columns[i], data_dist.columns[j])
        route_ind = get_index(data_dist, route)

        if len(route_ind) == 2:
            print(
                "Il n'y a qu'un seul trajet ",
                f"possible entre \n{data_price.columns[i]} et ",
                data_price.columns[j], ".",
                f"\nLe trajet coûte {round(data_price.iloc[i][j]/data_dist.iloc[i][j], 3)}€/km")
        else:
            p = load_price.subdata_price(data_price, route_ind)
            d = load_dist.subdata_dist(data_dist, route_ind)
            m = average_cost_list(p, d)
            fig, ax = plt.subplots(1, 1, figsize=(5, 5))
            sns.kdeplot(m, shade=True, cut=0, bw_adjust=bw)
            plt.ylabel("Density level")
            plt.title(f"KDE pour le prix au kilomètre \n entre {start} et {target}")
            plt.tight_layout()
            plt.show()

end = time.time()
print("Temps passé pour exécuter kde_gare : {0:.5f} s.".format(end - start))

def mean_gare(data):
    """
    Affiche le barycentre des données.

    :param DataFrame data: Tableau de données numériques.

    :return:
        **b** (*pd.core.Series.Series*) Le vecteur aux coordonnées moyennes.

    :example:  
        .. code:: python

                >>> import asltam as atm
                >>> # affichons les prix moyens par gare
                >>> prix = atm.load_price().save_as_price(index=' ')
                >>> print(atm.mean_gare(prix))

        MONTPELLIER                    13.339130\n
        SETE                           11.247826\n
        AGDE                            9.239130\n
        BEZIERS CABRIALS (SORTIE)       8.430435\n
        BEZIERS OUEST                   7.704348\n
        NARBONNE EST                    6.878261\n
        NARBONNE SUD                    6.339130\n
        SIGEAN                          7.108696\n
        LEUCATE                         7.543478\n
        PERPIGNAN NORD                  9.391304\n
        PERPIGNAN SUD                   9.830435\n
        BOULOU (FERME)                 11.600000\n
        LE PERTHUS-LE BOULOU           12.708696\n
        LEZIGNAN                        6.408696\n
        CARCASSONNE EST                 7.521739\n
        CARCASSONNE OUEST               7.660870\n
        BRAM                            8.608696\n
        CASTELNAUDARY                   9.086957\n
        VILLEFRANCHE DE LAURAGAIS      10.213043\n
        NAILLOUX                       10.843478\n
        MAZERES                        12.152174\n
        PAMIER                         12.969565\n
        TOULOUSE SUD-OUEST (SORTIE)    12.660870\n
        dtype: float64
    """
    return data.mean()


def swarm_gare_price(data_price, name):
    """
    Affiche le swarmplot des prix par gare inscrite dans name.

    :param DataFrame data_price: Tableau de données des prix.

    :param list name: Liste d'index de data_price.
    
    :return: None.

    :examples:
        .. code:: python
        
                >>> import asltam as atm
                >>> prix = atm.load_price().save_as_price(index=' ')
                >>> atm.swarm_gare_price(prix, ['MONTPELLIER', 'BRAM', 'CASTELNAUDARY'])
    
    """
    name_ind = get_index(name)
    p = data_price[data_price.columns[name_ind]]
    sen = ' '
    for i in range(len(name)):
        sen+= name[i] + ', '

    fig = px.strip(p, orientation='h', hover_name=p.index, 
                        labels = { "value" : "Prix (en €)",
                                    "variable" :"Villes"}, 
                        title =f"Swarmplot des prix entre {sen}")
    fig.show()


