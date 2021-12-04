.. ASLTAM documentation master file, created by
   sphinx-quickstart on Sun Nov 21 12:21:22 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation du programme ASLTAM
==================================

Bienvenu dans la documentation du programme ASLTAM !  

Introduction
=============
Le nom ``asltam`` provient de l'acronyme ASL (une mauvaise lecture de ASF, pour Autoroute du Sud de la France) et des premières lettres des créateurs du package : Thomas CARVAILLO, Alexandre CAPEL et Abdelmalk BOUARROUDJI (appelé aussi Malek). Ce module python a été conçu pour répondre à une problématique sur l'étude de la politique des prix de la compagnie Vinci, en particulier dans la région Occitanie.

Procédure d'installation
=========================
Pour utiliser pleinement ``asltam``, il faut faire plusieurs installations intermédiaires. Vous pourriez par exemple commencer par créer un environnement anaconda qui contiendra tous les modules nécessaire au bon fonctionnement du package, avec la commande :

.. code:: bash

         $ conda create --name atm_env

dans un terminal python (sous Windows, installer Anaconda3 si ce n'est pas déjà fait et recherchez Anaconda Prompt sur la barre de recherche).

Ensuite, après avoir basculer dans le nouvel environnement python, téléchargez les modules présents dans le fichier ``requirements.txt`` via une commande ``pip``. Par exemple, pour le premier module compilez :

.. code:: bash

         $ conda install - n atm_env download=0.3.5

Ces packages sont importants pour le bon fonctionnement du programme. Après toutes ces manipulations vous pourrez enfin installer notre module avec la commande ``pip`` comme fait précédemment, et ainsi le lancer et l'utiliser comme bon vous semble. 

.. code:: python

         import asltam as atm

Structure des données
=======================

La plupart des fonctions et algorithmes de ``asltam`` utilisent des variables de type DataFrame ``pandas`` qui ont une structure bien particulière pour bien fonctionner.
On appellera alors matrice des distances/prix, un tableau de donnée symétrique à coefficients positifs, de diagonale nulle. Il sera donc nécessaire avant d'utiliser les fonctions du package, de veiller à ce que les données utilisées soient rangées de cette manière. Il faudra aussi veiller à ce que les données soient compatibles dans le sens ou la position des distances et des prix soit rangée dans le même ordre. Il sera également possible d'utiliser des données géographique, en particulier dans le module ``map``, pour l'affichage de cartes par exemple. Une classe pour chacun de ces types de données ont été conçu pour les charger et les manipuler.




.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. toctree::
   usage/asltam.rst

.. toctree::
   usage/Construction_des_données.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
