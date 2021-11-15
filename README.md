# Project_2021_HAX712X
Ensemble du projet fait dans le cadre du module HAX7121X par CARVAILLO Thomas, BOUARROUDJ Abdelmalek et CAPEL Alexandre.


## Programme des tâches à effectuer

Nous allons commencer par construire les tableaux de données sur les prix des portions d'autoroute, et sur la distance séparant deux gares de péages successives. On utilisera pour le prix le fichier pdf fourni dans le git de la présentation du projet (HAX172X/Projet) et pour la distance nous avons reçu l'aide de M. CHARLIER pour trouver les données les contenant.

Le projet va être accès sur trois grands axes : 

- le développement d'une carte intéractive qui a pour but d'afficher le prix, la distance et le prix moyen au kilomètre d'une portion de route, accessible en cliquant sur la route correspondante : les packages ```plotly```, ```folium``` et ```osmnx``` seront très solicités dans cette partie.
- pour l'affichage de la distribution des prix, nous comptons identifier, en fixant une portion de route, la densité de probabilité du prix au kilomètre à l'aide d'une estimation par noyau : le but sera de trouver les prix au kilomètre de toutes les routes possibles, dans la portion sélectionné et d'en déduire une distribution de probabilité. On pourra aussi faire une étude générale sur les portions de route à l'aide de boxplot par exemple... Si cet objectif devient finalement trop ambitieux, on se limitera à la distribution générale sur tout le tableau de donnée. Nous utiliserons ```pandas``` pour faire ces visualisations (voire même ```ipywidgets``` si tout se passe bien).
- l'algorithme final sera fait en s'inspirant d'algorithmes de théorie des graphes (i.e. Kruskal) pour pouvoir donner une variante à des algorithmes du plus court chemin dans le but de répondre au problème. On utilisera donc sûrement beaucoup le module ```networkx``` pour cette partie.


Chaque partie donnera lieu à plusieurs programmes contenus dans notre package final. Une description détaillé de chaque programme sera aussi centrale dans notre travail et sera construite dans un documentation à part, disponible sur ce git. Enfin, une vidéo explicative générale sera aussi disponible à la fin de notre projet pour une prise en main rapide et efficace du package.

## Répartition des tâches

Le projet étant réparti en trois grands axes, nous allons séparé grossièrement le travail de la sorte : Thomas s'occupera de la carte intéractive, Alexandre devra afficher les "distribution" et enfin Abdelmalek s'occupera de la partie graphe. Bien sûr, les parties étant intrinsèquement liées, certaines choses faites dans une partie seront peut-être utilisées dans une autre : tout le monde aura donc une part de son travail dans chaque axe.


