import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def get_index(data, name):
    """ 
    Retourne la valeur de la position de la gare de péage dans le DataFrame.

    Attributs
    ---------
    data : pd.DataFrame, dont les colonnes portent le nom des péages.
    name : str, nom d'une gare de péage de data.
    """
    try:
        data[name] + 0 == 1
        i = 0
        while i<len(data) and name != data.columns[i]:
            i += 1
        return i
    except Exception as a :
        print(f"Attention ! Vérifiez que le nom des colonnes soient bien définis ou que {a} appartient à la base de donnée.")  
        
def kde_gare(all, 
            data_price, 
            data_dist, 
            name1, 
            name2, 
            bw):
    """
    Affiche la distribution des prix au kilomètre entre deux gares de péages sur un trajet donné.
    Attention, les données de distance et de prix doivent être rangé dans le même ordre dans les tableaux de données.

    Attributs
    ---------
    all : Bool, Si True affiche la distribution sur le DataFrame entier.
    data_price : DataFrame, tableaux de données de prix entre les gares de péage.
    data_dist : DataFrame, tableaux de données des distances entre les gares de péage.
    name1 : str, nom de la première gare.
    name2 : str, nom de la seconde gare.
    bw : à modifier il ne fonctionne pas trop
    """
    if all:
        m = np.array(data_price)/(np.array(data_dist)+np.diag(np.ones(len(data_dist))))
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
        sns.kdeplot(m[np.triu_indices(len(m), k=1)], shade=True, cut=0, bw_adjust=bw)
        plt.ylabel("Densité")
        plt.title("KDE pour le prix au kilomètre")
        plt.tight_layout()
        plt.show()

    elif name1 == name2 : 
        print("Ce sont les mêmes gares : il n'y a rien à afficher.")
        
    else:
        i = min(get_index(data_price, name1), get_index(data_price, name2))
        j = max(get_index(data_price, name1), get_index(data_price, name2))

        # ici il faudra changer et trouver un moyen de n'avoir que les gares du trajet.
        p = data_price.iloc[i:j+1][data_price.columns[i:j+1]]
        d = data_dist.iloc[i:j+1][data_dist.columns[i:j+1]]

        m = np.array(p)/(np.array(d)+np.diag(np.ones(len(d))))
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
        sns.kdeplot(m[np.triu_indices(len(m), k=1)], shade=True, cut=0, bw_adjust=bw)
        plt.ylabel("Densité")
        plt.title(f"KDE pour le prix au kilomètre \n entre {name1} et {name2}")
        plt.tight_layout()
        plt.show()
