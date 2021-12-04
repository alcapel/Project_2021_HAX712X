import pandas as pd
from download import download
from asltam.io import url_geo, path_geo

class load_geo :
	def __init__(self, url = url_geo, target = path_geo):
		download(url, target, replace = False)

	@staticmethod
	def save_as_geo(index=None):
		df_geo = pd.read_csv(path_geo, index_col=index)
		return df_geo
	def subdata_geo(data, index):
        	return data.iloc[index][data.columns[index]]