import numpy as np
import matplotlib.pyplot as plt
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
    Affiche la distribution des prix au kilomètre entre deux gares de péages sur un trajet donné.
    Attention, les données de distance et de prix doivent être rangé dans le même ordre dans les tableaux de données.

    Attributs
    ---------
    all : Bool, Si True affiche la distribution sur le DataFrame entier.
    data_price : DataFrame, tableaux de données de prix entre les gares de péage.
    data_dist : DataFrame, tableaux de données des distances entre les gares de péage.
    start : str, nom de la première gare.
    target : str, nom de la seconde gare.
    bw : voir doc bw_adjust de seaborn.
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
