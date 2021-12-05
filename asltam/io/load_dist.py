import pandas as pd
import numpy as np
from download import download
from asltam.io import url_dist, path_dist

class load_dist :
	"""
	Une classe utile pour charger les données des distances.
	Pour le bon fonctionnement du module veillez à ce que 
	les données soient bien sous le bon format (voir documentation
	pour plus d'informations). Une méthode pour savoir si votre
	DataFrame est bien un tableau des distances est disponible en
	cas de doute.
	
	Voir aussi
	----------
	load_geo : Classe pour le chargement de données géographiques.
	load_price : Classe pour le chargement de données des prix.
	"""
	def __init__(self, url = url_dist, target = path_dist):
		""" 
		Télécharge des données issu d'un url, dans un repertoire
		target.
		
		Paramètres
		----------
		url : str.
			url d'origine de vos données. Le paramètre
			par défaut est celui utilisé en guise d'illustration
			du package. Il télécharge les données des distances 
			entre les différentes gares de péage du réseau 
			autoroutiers de	la région Occitanie, en France.
		
		target : str.
			Chemin d'accès pour télécharger votre DataFrame.
			Par défaut, la classe téléchargera le fichier
			dans le repertoire courant sous le nom de 
			'data_dist.csv'.
		"""
		download(url, target, replace = False)

	@staticmethod
	def save_as_dist(path=path_dist, index=None):
		"""
		Méthode pour le chargement des données dans un DataFrame pandas.
		
		Paramètres
		----------
		path : str.
			Chemin d'accès pour lire votre DataFrame. Par
			défaut, il s'agit du chemin utilisé lors du 
			téléchargement des données en ayant utilisé 
			le paramètre par défaut.
		
		index : str.
			Indique quel colonne vous voulez mettre en index 
			(si vous le désirez). Il ne sera pas utilisé par 
			défaut.
		
		Return
		------
		df_dist : pandas.DataFrame.
			Renvoie un pandas DataFrame avec vos données 
			des distances.
		"""
		df_dist = pd.read_csv(path, index_col=index)
		return df_dist
	
	def subdata_dist(data_dist, index):
		"""
		Méthode donnant un sous tableau des distances à partir d'un
		tableau de distance initial et d'une liste d'index donnée.
		
		Paramètres
		----------
		data_dist : pandas.DataFrame
			Une matrice de distance.
		
		index : list.
			Liste d'index utilisé pour extraire le 
			sous tableau.
		
		Return
		------
		Renvoie un pandas DataFrame qui est un sous tableau de
		distances de data_dist.
		"""
		return data_dist.iloc[index][data_dist.columns[index]]
	
	def is_dist(data_dist):
		"""
		Méthode qui vérifie si data_dist est bien un tableau
		de distances.
		
		Paramètres
		----------
		data_dist : DataFrame.
			Tableau de donnée à tester.
		
		Return
		------
		b : bool. 
			True si c'est bien un talbeau de distance,
			False sinon.
		
		Voir définition matrice de distance sur la documentation.
		"""
		n = len(data_dist)
		D = np.array(data_dist)
		c1 = sum(sum(D == D.T))
		c2 = sum(np.diag(D) == np.zeros(n))
		if c1 != n**2 :
			print("Attention, votre tableau n'est pas symétrique")
		elif c2 != n :
			print("Attention, un élément de la diagonale est non nul")
		
		
		
		
		
		
		
		
		
		
		
