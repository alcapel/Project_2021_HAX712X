.. ASLTAM documentation master file, created by
   sphinx-quickstart on Sun Nov 21 12:21:22 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation du programme ASLTAM
==================================

Bienvenu dans la documentation du programme ASLTAM ! Un package très utile de modélisation statistique. 

Présentation
=============

   .. image:: ./usage/img/Autoroute.png
    :width: 300
    :align: center


Le nom ``asltam`` provient de l'acronyme ASL (une mauvaise lecture de ASF, pour Autoroute du Sud de la France) et des premières lettres des créateurs du package : Thomas CARVAILLO, Alexandre CAPEL et Abdelmalk BOUARROUDJI (appelé aussi Malek). Ce module python a été conçu pour répondre à une problématique sur l'étude de la politique des prix de la compagnie Vinci, en particulier dans la région Occitanie.
Cependant, il est possible pour vous d'utiliser ce package à votre guise, pour répondre à un de vos problèmes. Cependant, il faut commencer par l'installer.

Procédure d'installation
=========================
Pour utiliser pleinement ``asltam``, il faut faire plusieurs installations intermédiaires. Vous pourriez par exemple commencer par créer un environnement anaconda qui contiendra tous les modules nécessaire au bon fonctionnement du package, avec la commande :

.. code:: bash

         $ conda create --name atm_env

dans un terminal python (sous Windows, installer Anaconda3 si ce n'est pas déjà fait et recherchez Anaconda Prompt sur la barre de recherche).

Ensuite, après avoir basculé dans le nouvel environnement python, téléchargez le dossier du `git <https://github.com/Eldohrim/Project_2021_HAX712X>`_.
Enfin, placez vous dans le dossier correspondant, et téléchargez les modules présents dans le fichier ``requirements.txt`` via la commande ``pip`` :

.. code:: bash

         $ pip install -r /path/to/requirements.txt

Ces packages sont importants pour le bon fonctionnement du programme. Après toutes ces manipulations, vous pourrez enfin installer notre module avec la commande :

.. code:: bash

         $ pip install -i https://test.pypi.org/simple/ asltam==1.1.0

et ainsi le lancer et l'utiliser comme bon vous semble. Idée d'importation :

.. code:: python

         >>> import asltam as atm

Démonstrations de ``asltam``
=============================
Les possibilités avec ``asltam`` sont multiples. Il est possible avec notre package de faire des études statistiques avec des outils
de visualitation 

* affichage d'un "kernel density estimation" avec la fonction ``kde_gare`` (issu du code dans :ref:`Module price_distribution`)

.. image:: ./usage/img/kde.jpg
   :width: 400
   :align: center

* affichage d'un swarmplot des prix en fonction des gares d'arrivée (code issu de la même section que celui ci-dessus):

.. image:: ./usage/img/swarm.jpg
   :width: 400
   :align: center

mais aussi d'afficher des cartes intéractives avec des serveurs très performants (fait avec le code de :ref:`Module map`): 

.. image:: ./usage/img/carte-gif.gif
   :width: 400
   :align: center

Il y a aussi un algorithme d'optimisation de coût de trajet, mais nous vous laissons le plaisir de le découvrir par vous même dans le :ref:`Module graph`.

Table des matières
=====================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

.. tabs::
   
   .. tab:: ASLTAM

      Pour accéder à toute la documentation concernant ``asltam``, aller ici :

      .. toctree::
         usage/asltam.rst
   
   .. tab:: Construction des données

      Dans ces sections, nous expliquons d'où proviennent les données, et comment nous les avons traités pour répondre au problème. Ce sont les données à titre d'exemple pour les programmes.
      
      .. toctree::
         usage/Construction_des_données.rst
   
   .. tab:: Structure des données

      Pour avoir des résultats cohérents, et un bonne utilisation du package, il est nécessaire d'avoir connaissance du type et format des données.
      Une série de définitions et d'explications sur les données est réunie ici :

      .. toctree::
         usage/Structure_des_données.rst

   .. tab:: Guide installation clef API

      Pour une optimiser votre usage de ``asltam``, il est conseillé d'avoir une clef API personnelle. Voici un court guide pour en obtenir une :

      .. toctree::
         usage/installation_clef.rst      

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
