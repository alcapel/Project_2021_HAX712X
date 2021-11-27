import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from asltam.io.load_dist import load_dist
from asltam.io.load_price import load_price
from asltam.graph.graph import get_way
from asltam.io.pricedist import average_cost_list


def get_index(data, name):
    """
    Retourne la valeur de la position de la gare de péage dans le DataFrame

    Attributs :
    -----------
    data : pd.DataFrame, dont les colonnes porte le nom des péages
    name : str ou list, nom(s) d'une gare de péage de data
    """
    if type(name) == str:
        try:
            data[name] + 0 == 1
            i = 0
            while i < len(data) and name != data.columns[i]:
                i += 1
            return i
        except Exception as a:
            print(f"Attention ! {a} n'appartient pas à la base de donnée.")
    elif type(name) == list:
        ind = []
        try:
            data[name] + 0 == 1
            for j in range(len(name)):
                i = 0
                while i < len(data) and name[j] != data.columns[i]:
                    i += 1
                ind.append(i)
            return ind
        except Exception as a:
            print(f"Attention ! {a} n'appartient pas à la base de donnée.")


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
                f"\nLe trajet coûte {data_price.iloc[i][j]/data_dist.iloc[i][j]:f}€/km")
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
