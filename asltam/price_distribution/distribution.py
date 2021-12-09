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

    .. warning:: Attention, les données de distance et de prix
            doivent être compatible pour pouvoir avoir des résultats cohérents. 
            Voir la documentation pour la :ref:`Compatibilité`.

    :param bool all: Si True affiche la distribution sur le DataFrame entier.

    :param DataFrame data_price: Tableaux de données de prix entre les gares de péage.

    :param DataFrame data_dist: Tableaux de données des distances entre les gares de péage.

    :param str start: Nom de la première gare.

    :param str target: Nom de la seconde gare.

    :param float bw: Voir doc bw_adjust de seaborn.

    :returns: None.

    :examples: .. code:: python
                    >>> import asltam as atm
                    >>> prix = load_price().save_as_price(index=' ')
                    >>> dist = load_dist().save_as_dist(index=' Nom gare ')
                    >>> atm.kde_gare(True, prix, dist, 1)
    """
    if all:
        # Cas où l'on veut  afficher la distribution
        # avec tous le tableau de données.

        # Création de la liste des prix moyens.
        m = average_cost_list(data_price, data_dist)

        # Affichage du KDE avec ces données.
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
        sns.kdeplot(m, shade=True, cut=0, bw_adjust=bw)
        plt.ylabel("Density level")
        plt.title("KDE pour le prix au kilomètre")
        plt.tight_layout()
        plt.show()

    elif start == target:
        print("Ce sont les mêmes gares : il n'y a rien à afficher.")
    else:
        # Calcul des numéros d'index (utile pour utiliser avec d'autres données)
        i = get_index(data_price, start)
        j = get_index(data_price, target)

        # pour avoir juste les gares qui nous intéresse,
        # il nous faut le nom des gare du trajet.
        route = get_way(data_dist, data_dist.columns[i], data_dist.columns[j])
        route_ind = get_index(data_dist, route)

        if len(route_ind) == 2:
            # c'est le cas où il n'y a qu'un seul trajet possible.
            print(
                "Il n'y a qu'un seul trajet ",
                f"possible entre \n{data_price.columns[i]} et ",
                data_price.columns[j], ".",
                f"\nLe trajet coûte {round(data_price.iloc[i][j]/data_dist.iloc[i][j], 3)}€/km")
        else:
            # on crée des sous tableaux sur la portion qui nous intéresse
            # et on refait ce que l'on a fait dans le cas all=True.
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

    :return: * **b** (*pd.core.Series.Series*) - Le vecteur aux coordonnées moyennes.

    :example: .. code:: python
                    >>> import asltam as atm
                    >>> # affichons les prix moyens par gare
                    >>> prix = atm.load_price().save_as_price(index=' ')
                    >>> print(atm.mean_gare(prix))
    """
    return data.mean()


def swarm_gare_price(data_price, name):
    """
    Affiche le swarmplot des prix par gare inscrite dans name.

    :param DataFrame data_price: Tableau de données des prix.

    :param list name: Liste d'index de data_price.

    :return: None.

    :examples: .. code:: python 
                >>> import asltam as atm
                >>> prix = atm.load_price().save_as_price(index=' ')
                >>> atm.swarm_gare_price(prix, ['MONTPELLIER', 'BRAM', 'CASTELNAUDARY'])
    """
    # Calcul des numéros d'index (utile pour utiliser avec d'autres données).
    name_ind = get_index(data_price, name)
    p = data_price[data_price.columns[name_ind]]
    sen = ' '

    for i in range(len(name)):
        # Pour le titre du graphique.
        sen+= name[i] + ', '

    # Affichage du swarmplot.
    fig = px.strip(p, orientation='h', hover_name=p.index, 
                        labels = { "value" : "Prix (en €)",
                                    "variable" :"Villes"}, 
                        title =f"Swarmplot des prix entre {sen}")
    fig.show()
