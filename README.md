# Projet ASLTAM

## Introduction
Le nom ``asltam`` provient de l'acronyme ASL (une mauvaise lecture de ASF, pour Autoroute du Sud de la France) et des premières lettres des créateurs du package : Thomas CARVAILLO, Alexandre CAPEL et Abdelmalk BOUARROUDJI (appelé aussi Malek). Ce module python a été conçu pour répondre à une problématique sur l'étude de la politique des prix de la compagnie Vinci, en particulier dans la région Occitanie.

## Procédure d'installation
Pour utiliser pleinement ``asltam``, il faut faire plusieurs installations intermédiaires. Vous pourriez par exemple commencer par créer un environnement anaconda qui contiendra tous les modules nécessaire au bon fonctionnement du package, avec la commande :
```bash
$ conda create --name atm_env
```
dans un terminal python (sous Windows, installer Anaconda3 si ce n'est pas déjà fait et recherchez Anaconda Prompt sur la barre de recherche).

Ensuite, après avoir basculer dans le nouvel environnement python avec la commande ``conda activate atm_env``, compilez les commandes suivantes : 
```bash
$ pip install numpy
$ pip install matplotlib
$ pip install pandas
$ pip install seaborn
$ pip install folium
$ pip install networkx
$ pip install download
$ pip install ipywidgets
$ pip install openrouteservice
à finaliser
```
Ces packages sont importants pour le bon fonctionnement du programme. Après toutes ces manipulations vous pourrez enfin installer notre module avec la commande ``pip`` comme fait précédemment, et ainsi le lancer et l'utiliser comme bon vous semble. 

```python
import asltam as atm
```

## Structure des données

La plupart des fonctions et algorithmes de ``asltam`` utilisent des variables de type DataFrame ``pandas`` qui ont une structure bien particulière pour bien fonctionner.
On appellera alors matrice des distances/prix, un tableau de donnée symétrique à coefficients positifs, de diagonale nulle. Il sera donc nécessaire avant d'utiliser les fonctions du package, de veiller à ce que les données utilisées soient rangées de cette manière. Il sera également possible d'utiliser des données géographique, en particulier dans le module ``map``, pour l'affichage de cartes par exemple. Une classe pour chacun de ces types de données ont été conçu pour les charger et les manipuler.

## Présentation des modules 

### ``asltam.map``
Le but principal de ce module est l'affichage d'une carte folium, affichant le trajet entre deux gares, ainsi que des descriptions de la route les séparant comme le prix, ou la distance totale. La fonction principale permettant d'afficher la carte peut s'appeler directement après importation de ``asltam`` comme fait ci-dessus, ainsi avec le code suivant :

```python
import asltam as atm
geo = 
dist = atm.load_dist().save_as_dist(index=' Nom gare ')
price = atm.load_price().save_as_price(index=' ')
start = 'MONTPELLIER'
target = 'SETE'
atm.trajet(geo, dist, price, start, target)

```
permettant d'afficher la carte suivante : 




Une démonstration de cette fonction est faite dans le fichier ``script.py`` si vous voulez le lancez vous même, ou dans la documentation :

### ``astlam.plot_distribution``

Dans ce module, des outils d'analyse sont mis à disposition pour faire de la visualisation des données. Par exemple, nous pouvons utiliser la fonction ``kde_gare`` de ce module, directement callable après importation du package, pour pouvoir faire une "kernel distribution estimation" sur la distribution des prix au kilomètre. Par exemple, le script suivant :

```python
import asltam as atm
dist = atm.load_dist().save_as_dist(index=' Nom gare ')
prix = atm.load_price().save_as_price(index=' ')

atm.kde_gare(all=True, prix, dist, bw=1)

```
permet d'afficher la distribution des prix au kilomètre selon tout le réseau routier que nous avions à disposition :

![alt text](https://github.com/Eldohrim/Project_2021_HAX712X/blob/main/Doc/kde.pdf?raw=true)

Une démonstration plus complète (avec des widgets !) de cette fonction est faite dans ``script.py``, ou dans la documentation.

### ``asltam.graph``

Ce dernier module s'appuie sur deux gros algorithmes issus de la théorie des graphes (i.e. Dijkstra et Kruskal) dans le but de produire un algorithme minimisant le coût d'un trajet en s'autorisant k sortie d'autoroute durant le trajet. Le problème étant combinatoire (voire même NP difficile), il est conseillé de l'utiliser dans des conditions viables : soit avec un trajet assez court, soit avec une contrainte k assez petite ou très grande.

## Construction des données





## README du projet mid-term
### Programme des tâches à effectuer

Nous allons dans un premier temps construire les données de base sur lesquelles notre module va s'appuyer. Nos tableaux de données décriront les prix des portions d'autoroute, et  les distances séparant deux gares de péages. On utilisera pour le prix le fichier pdf répertoriant la totalité des prix des portions d'autoroutes de Vinci (link : https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf, nos données se limiteront à la page 3). Pour la distance, nous avons utiliser des données géographiques fournies dans le site du gouvernement (link: https://www.data.gouv.fr/en/datasets/gares-de-peage-du-reseau-routier-national-concede/).

Le projet sera partitionné en trois grands axes : 

- le développement d'une carte interactive qui a pour but d'afficher le prix, la distance et le prix moyen au kilomètre d'une portion de route, accessible en cliquant sur la route correspondante : les packages ```plotly```, ```folium``` et ```osmnx``` seront très solicités dans cette partie.
- pour l'affichage de la distribution des prix, nous comptons identifier, en fixant une portion de route, la densité de probabilité du prix au kilomètre à l'aide d'une estimation par noyau : le but sera de trouver les prix au kilomètre de toutes les routes possibles, dans la portion sélectionnée et d'en déduire une distribution de probabilité. On pourra aussi faire une étude générale sur les portions de route à l'aide de boxplots par exemple... Si cet objectif devient finalement trop ambitieux, on se limitera à la distribution générale sur tout le tableau de donnée. Nous utiliserons ```pandas``` et ``seaborn`` pour faire ces visualisations (voire même ```ipywidgets``` si tout se passe bien).
- l'algorithme final sera fait en s'inspirant d'algorithmes de théorie des graphes (e.g. Kruskal) pour pouvoir donner une variante à des algorithmes du plus court chemin dans le but de répondre au problème. On utilisera donc sûrement beaucoup le module ```networkx``` pour cette partie.


Chaque partie donnera lieu à plusieurs programmes contenus dans notre package final. Une description détaillé de chaque programme sera aussi centrale dans notre travail et sera construite dans un documentation à part, disponible sur ce git. Enfin, une vidéo explicative générale sera aussi disponible à la fin de notre projet pour une prise en main rapide et efficace du package.

### Répartition des tâches

Le projet étant réparti en trois grands axes, nous allons séparé grossièrement le travail de la sorte : Thomas s'occupera de la carte interactive, Alexandre devra afficher les distributions et enfin Abdelmalek s'occupera de la partie graphe. Bien sûr, les parties étant intrinsèquement liées, certaines choses faites dans une partie seront peut-être utilisées dans une autre : tout le monde aura donc une part de son travail dans chaque axe.
