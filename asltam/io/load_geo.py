import pandas as pd
from download import download
from asltam.io import url_geo, path_geo

class load_geo :
	"""
	Une classe utile pour charger les données géographiques.
	Pour le bon fonctionnement du module veillez à ce que 
	les données soient bien sous le bon format (voir documentation
	pour plus d'informations).
	
	Voir aussi
	----------
	load_price : Classe pour le chargement de données des prix.
	
	load_dist : Classe pour le chargement de données des distances.
	"""
	def __init__(self, url = url_geo, target = path_geo):
		""" 
		Télécharge des données issu d'un url, dans un repertoire
		target.
		
		Paramètres
		----------
		url : str.
			url d'origine de vos données. Le paramètre
			par défaut est celui utilisé en guise 
			d'illustration du package. Il télécharge les 
			données géographiques du réseau autoroutier 
			de la région Occitanie, en France.
		
		target : str.
			Chemin d'accès pour télécharger votre
			DataFrame. Par défaut, la classe téléchargera 
			le fichier dans le repertoire courant sous le 
			nom de 'data_geo.csv'.
		"""
		download(url, target, replace = False)

	@staticmethod
	def save_as_geo(path=path_geo, index=None):
		"""
		Méthode pour le chargement des données dans un DataFrame pandas.
		
		Paramètres
		----------
		path : str.
			Chemin d'accès pour lire votre DataFrame. Par
			défaut, il s'agit du chemin utilisé lors du téléchargement 
			des données en ayant utilisé le paramètre par défaut.
		
		index : str.
			Indique quel colonne vous voulez mettre en index 
			(si vous le désirez). Il ne sera pas utilisé par défaut.
		
		Return
		------
		df_geo : pandas.DataFrame.
			Renvoie un pandas DataFrame avec vos données géographiques.
		"""
		df_geo = pd.read_csv(path_geo, index_col=index)
		return df_geo

