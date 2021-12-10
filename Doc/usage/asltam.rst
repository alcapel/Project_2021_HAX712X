ASLTAM
=======

Il s'agit du module principal de notre programme, il contient toutes les fonctions nécessaires à l'aboutissement du projet.

Module map
------------
Le but principal de ce module est l'affichage d'une carte folium,  affichant le trajet entre deux gares, ainsi que des descriptions de la route les séparant comme le prix, ou la distance totale. La fonction principale permettant d'afficher la carte peut s'appeler directement après importation de ``asltam``.

.. automodule:: asltam.map.carte_interactive
    :members:

Module price_distribution
---------------------------

Dans ce module, des outils d'analyse sont mis à disposition pour faire de la visualisation des données. Par exemple, nous pouvons utiliser la fonction ``kde_gare`` de ce module, directement callable après importation du package, pour pouvoir faire une "kernel distribution estimation" sur la distribution des prix au kilomètre.


.. automodule:: asltam.price_distribution.distribution
    :members:


Module pricedist
-----------------
.. automodule:: asltam.io.pricedist
    :members:

Module graph
---------------

Ce dernier module s'appuie sur deux gros algorithmes issus de la théorie des graphes (i.e. Dijkstra et Kruskal) dans le but de produire un algorithme minimisant le coût d'un trajet en s'autorisant k sortie d'autoroute durant ce dernier. Le problème étant combinatoire (NP complet), il est conseillé de l'utiliser dans des conditions viables : soit avec un trajet assez court, soit avec une contrainte k très petite ou très grande.


.. automodule:: asltam.graph.graph
    :members: