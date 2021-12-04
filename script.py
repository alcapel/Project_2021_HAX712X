import asltam as atm
from ipywidgets import interact, fixed

prix = atm.load_price().save_as_price(index=' ')
dist = atm.load_dist().save_as_dist(index=' Nom gare ')
geo = atm.load_geo().save_as_geo(index=' Nom gare ')
geo = geo[['Latt', 'Long']]

#%% Construction de la carte intéractive
interact(atm.trajet, DEPART=list(geo.index), ARRIVEE=list(geo.index), 
         data_geo=fixed(geo), data_price=fixed(prix), data_dist=fixed(dist))

#%% Affichage des distributions avec interact
interact(atm.kde_gare, all = True, data_dist = fixed(dist),
         data_price = fixed(prix), start = prix.columns, 
         target = prix.columns, bw = (0.05,2,0.01))

#%% Recherche des trajets optimaux
start = input(f"Donnez une gare de départ parmi les gares suivantes : {list(prix.index)}.")
target = input(f"Donnez une gare d'arrivée parmi les gares suivantes : {list(prix.index)}.")
n = input("Rentrez le nombre de sortie que vous vous accordez :")

g, opt = atm.kmin_cost_out(data_dist=dist, data_price=prix,
                          start = start, target = target, 
                          k = int(n))
print(f"Pour avoir le trajet optimal entre {g[0]} et {g[-1]},\n",
    f"il faut sortir à {g[1:-1]}. Le coût total sera de {round(opt, 3)}€")
