Structure des données
=====================

Ici, nous présentons la forme que doivent avoir les données pour que les algorithmes puissent fonctionner convenablement.

La plupart des fonctions et algorithmes de ``asltam`` utilisent des variables de type DataFrame ``pandas`` qui ont une structure bien particulière pour bien fonctionner.

Format des données géographiques
----------------------------------
Dans le module ``map``, on utilise des données géographiques pour pouvoir afficher les cartes. Cependant, il est nécessaire d'avoir le bon format
pour pouvoir utiliser convenablement les fonctions. Ainsi, les coordonnées doivent être en WGS84 (epsg:4326) et doivent commencer d'abord par la lattitude et ensuite la longitude.
Voici un exemple de tableau sous le bon format : 

========================= ================== ==================
Gares de péage            Lattitude          Longitude
========================= ================== ==================
Montpellier               43.56321197997598  3.832152851175532 
Sete                      43.48122735717297  3.683459688948031
Agde                      43.37686025015689  3.4158808248192942
Beziers Cabrials (Sortie) 43.34325721988552  3.2885692228136043
Beziers Ouest             43.303664399696856 3.2229492234270127
========================= ================== ==================

Si vos coordonnées sont en lambert93 (epsg:2154), vous pouvez transformer ces dernières en coordonnées WGS84 (epsg:4326) en suivant le tutoriel `suivant <https://moonbooks.org/Articles/Convertir-des-coordonnees-Lambert-93-en-longitude-et-latitude-avec-python-3/>`_.

Enfin, la classe ``load_geo`` est disponible dans ``asltam`` pour pouvoir charger vos données géographiques avec ``pandas``.

Matrice des distances/prix
---------------------------

Comme pour les données géographiques, il va falloir fixer un certain vocabulaire dans les tableaux de données qui traitent des prix et des distances.
Elles auront une structure assez simple, et on appellera matrice des distances/prix, un tableau de données symétrique à coefficients positifs, de diagonale nulle.

======== ===== ===== ==== ====
 \       x1    x2    ...  xn
======== ===== ===== ==== ====
x1       0     a1 2  ...  a1 n
x2       a1 2  0     ...  a2 n
...      ...   ...   ...  ...
xn       a1 n  a2 n  ...  0
======== ===== ===== ==== ====


Ces conditions sont assez légitime pour pouvoir faire un tableau croisé des prix (ou des distances). Par exemple, voici un extrait du tableau des prix de notre base de données :

========================= =========== ==== ==== ========================= =============
Prix                      Montpellier Sete Agde Beziers Cabrials (Sortie) Beziers Ouest
========================= =========== ==== ==== ========================= =============
Montpellier               0.0         1.6  3.6  4.7                       5.6
Sete                      1.6         0.0  1.9  3.3                       3.6
Agde                      3.6         1.9  0.0  1.0                       1.4
Beziers Cabrials (Sortie) 4.7         3.3  1.0  0.0                       0.7
Beziers Ouest             5.6         3.6  1.4  0.7                       0.0
========================= =========== ==== ==== ========================= =============


Il sera donc nécessaire avant d'utiliser les fonctions du package, de veiller à ce que les données utilisées soient rangées de cette manière. Il existe deux classes
pour pouvoir charger les données de distances ou de prix qui se nomment respectivement ``load_dist`` et ``load_price``. Une méthode pour vérifier si ce sont bien des matrices de
distances/prix est disponible.

Compatibilité
--------------
Pour pouvoir avoir des résultats interprétables, il faudra enfin veiller à ce que les données soit rangées dans le même ordre : c'est que nous appelerons "données compatibles".
Considérons le tableaux des distances suivants :

========================= =========== ==== ==== ========================= =============
Distances                 Montpellier Sete Agde Beziers Cabrials (Sortie) Beziers Ouest
========================= =========== ==== ==== ========================= =============
Montpellier               0.0         17.0 41.0 57.0                      59.0
Sete                      17.0        0.0  26.0 39.0                      44.0
Agde                      41.0        26.0 0.0  16.0                      18.0
Beziers Cabrials (Sortie) 57.0        39.0 16.0 0.0                       8.0
Beziers Ouest             59.0        44.0 18.0 8.0                       0.0
========================= =========== ==== ==== ========================= =============

Alors, ce-dernier, et ceux des sections précédentes, sont compatibles (on voit que les noms de gare sont dans le même ordre sur le tableau).

