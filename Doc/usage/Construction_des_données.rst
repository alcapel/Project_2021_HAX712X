Récupération des données
===========================

Les données que nous utilisons pour faire les démonstrations proviennent de données libres disponible sur internet. Pour les points géographiques (dont nous avons déduit les distances), nous avons utilisé des données libres (sous format ``.csv``) disponible sur 

https://static.data.gouv.fr/resources/gares-de-peage-du-reseau-routier-national-concede/20210224-175626/gares-peage-2019.csv.

Les prix des portions d'autoroutes ont été récupéré dans le pdf suivant 

https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf

Nos données se limiteront à la page 3.

Nettoyage des données
----------------------
Après avoir tout transformé en fichier ``.csv``, il a fallu trier les données et ne récupérer seulement celles qui nous intéressaient. En particulier, nous souhaitions nous concentrer uniquement sur des portions payantes des autoroutes disponibles à la page 3 du lien précédemment donné (à l'exception de la portion menant Toulouse à Albi). 

Pour cela, nous avons utilisé le module ``pandas`` pour nettoyer toutes ces données (les codes sont fournis dans le dossier ``./initsort_data`` du git): 

* le fichier ``clean_data_price.py`` sert à retirer les gares dont les portions de route sont gratuites ou indisponibles, à partir du fichier ``price-data.csv``, disponible sur le git dans ``./asltam/data``, construit à partir du pdf.

* le fichier ``creation_data_geo.py`` commence par sélectionner les autoroutes de notre problèmes, et transformer les coordonnées GPS dans le bon format

* on revient ensuite sur nos données géographiques nous réindexons les gares pour que leur position soit compatible avec le tableau des prix (``Creation data_geo2.py``).

* enfin, on procède à des requêtes à l'aide des modules ``requests`` et ``json`` pour pouvoir récupérer les données des distances que nous rangeons sous forme de tableau de distance compatible avec les données précédentes (``distance.py``).

Accès aux données
-------------------
Les fichiers peuvent être consultés sur le git dans le dossier ``./asltam/data``, et les données finales téléchargées à l'aide des classes ``load_dist``, ``load_price``, ou ``load_geo``.