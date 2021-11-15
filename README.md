# Project_2021_HAX712X
Descriptif du package ``asltam``,  le projet fait dans le cadre du module HAX7121X par CARVAILLO Thomas, BOUARROUDJ Abdelmalek et CAPEL Alexandre.


## Programme des tâches à effectuer

Nous allons dans un premier temps construire les données de base sur lesquelles notre module va s'appuyer. Nos tableaux de données décriront les prix des portions d'autoroute, et  les distances séparant deux gares de péages. On utilisera pour le prix le fichier pdf répertoriant la totalité des prix des portions d'autoroutes de Vinci (link : https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf, nos données se limiteront à la page 3). Pour la distance, nous avons utiliser des données géographiques fournies dans le site du gouvernement (link: https://www.data.gouv.fr/en/datasets/gares-de-peage-du-reseau-routier-national-concede/).

Le projet sera partitionné en trois grands axes : 

- le développement d'une carte interactive qui a pour but d'afficher le prix, la distance et le prix moyen au kilomètre d'une portion de route, accessible en cliquant sur la route correspondante : les packages ```plotly```, ```folium``` et ```osmnx``` seront très solicités dans cette partie.
- pour l'affichage de la distribution des prix, nous comptons identifier, en fixant une portion de route, la densité de probabilité du prix au kilomètre à l'aide d'une estimation par noyau : le but sera de trouver les prix au kilomètre de toutes les routes possibles, dans la portion sélectionnée et d'en déduire une distribution de probabilité. On pourra aussi faire une étude générale sur les portions de route à l'aide de boxplots par exemple... Si cet objectif devient finalement trop ambitieux, on se limitera à la distribution générale sur tout le tableau de donnée. Nous utiliserons ```pandas``` et ``seaborn`` pour faire ces visualisations (voire même ```ipywidgets``` si tout se passe bien).
- l'algorithme final sera fait en s'inspirant d'algorithmes de théorie des graphes (e.g. Kruskal) pour pouvoir donner une variante à des algorithmes du plus court chemin dans le but de répondre au problème. On utilisera donc sûrement beaucoup le module ```networkx``` pour cette partie.


Chaque partie donnera lieu à plusieurs programmes contenus dans notre package final. Une description détaillé de chaque programme sera aussi centrale dans notre travail et sera construite dans un documentation à part, disponible sur ce git. Enfin, une vidéo explicative générale sera aussi disponible à la fin de notre projet pour une prise en main rapide et efficace du package.

## Répartition des tâches

Le projet étant réparti en trois grands axes, nous allons séparé grossièrement le travail de la sorte : Thomas s'occupera de la carte interactive, Alexandre devra afficher les distributions et enfin Abdelmalek s'occupera de la partie graphe. Bien sûr, les parties étant intrinsèquement liées, certaines choses faites dans une partie seront peut-être utilisées dans une autre : tout le monde aura donc une part de son travail dans chaque axe.
