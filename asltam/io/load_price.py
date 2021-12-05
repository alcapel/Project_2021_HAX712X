import pandas as pd
import numpy as np
from download import download
from asltam.io import url_price, path_price

class load_price :
	"""
	Une classe utile pour charger les données des prix.
	Pour le bon fonctionnement du module veillez à ce que 
	les données soient bien sous le bon format (voir documentation
	pour plus d'informations). Une méthode pour savoir si votre
	DataFrame est bien un tableau de prix est disponible en
	cas de doute.
	
	Voir aussi
	----------
	load_geo : Classe pour le chargement de données géographiques.
	
	load_dist : Classe pour le chargement de données des distances.
	"""
	def __init__(self, url = url_price, target = path_price):
		""" 
		Télécharge des données issu d'un url, dans un repertoire
		target.
		
		Paramètres
		----------
		url : str.
			url d'origine de vos données. Le paramètre
			par défaut est celui utilisé en guise 
			d'illustration du package. Il télécharge les
			données des prix entre les différentes gares 
			de péage du réseau autoroutier de la région 
			Occitanie, en France.
		
		target : str.
			Chemin d'accès pour télécharger votre DataFrame. 
			Par défaut, la classe téléchargera le fichier
			dans le repertoire courant sous le nom de 
			'data_price.csv'.
		"""
		download(url, target, replace = False)

	@staticmethod
	def save_as_price(path=path_price, index=None):
		"""
		Méthode pour le chargement des données dans un DataFrame pandas.
		
		Paramètres
		----------
		path : str.
			Chemin d'accès pour lire votre DataFrame. Par
			défaut, il s'agit du chemin utilisé lors du téléchargement 
			des données en ayant utilisé le paramètre par défaut.
		
		index : str, 
			Indique quel colonne vous voulez mettre en index 
			(si vous le désirez). Il ne sera pas utilisé par défaut.
		
		Return
		------
		df_price : pandas.DataFrame
			Renvoie un pandas DataFrame avec vos données des prix.
		"""
		df_price = pd.read_csv(path, index_col=index)
		return df_price
	
	def subdata_price(data_price, index):
		"""
		Méthode donnant un sous tableau des prix à partir d'un
		tableau de prix initial et d'une liste d'index donnée.
		
		Paramètres
		----------
		data_dist : pandas.DataFrame.
			Une matrice de prix.
		
		index : list.
			Liste d'index utilisé pour extraire le 
			sous tableau.
		
		Return
		------
		d : pandas.DataFrame.
			Renvoie un pandas DataFrame qui est un sous 
			tableau de prix de data_price.
		"""
		return data_price.iloc[index][data_price.columns[index]]
		
	def is_price(data_price):
		"""
		Méthode qui vérifie si data_price est bien un tableau
		de prix.
		
		Paramètres
		----------
		data_price : DataFrame.
			Tableau de donnée à tester.
		
		Voir définition matrice de prix sur la documentation.
		"""
		n = len(data_price)
		P = np.array(data_price)
		c1 = sum(sum(P == P.T))
		c2 = sum(np.diag(P) == np.zeros(n))
		if c1 != n**2 :
			print("Attention, votre tableau n'est pas symétrique")
		elif c2 != n :
			print("Attention, un élément de la diagonale est non nul")

