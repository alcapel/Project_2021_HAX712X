import asltam as atm
from ipywidgets import interact, fixed

prix = atm.load_price().save_as_price(index=' ')
dist = atm.load_dist().save_as_dist(index=' Nom gare ')


# Affichage des distributions avec interact
interact(atm.kde_gare, all = True, data_dist = fixed(dist),
         data_price = fixed(prix), start = prix.columns, 
         target = prix.columns, bw = (0.05,2,0.01))

# Recherche des trajets optimaux
g, opt = atm.kmin_cost_out(data_dist=dist, data_price=prix,
                          start = 'MONTPELLIER', target = 'CASTELNAUDARY', 
                          k = 4)
print(f"Pour avoir le trajet optimal entre {g[0]} et {g[-1]},\n",
    f"il faut sortir à {g[1:-1]}. Le coût total sera de {round(opt, 3)}€")
