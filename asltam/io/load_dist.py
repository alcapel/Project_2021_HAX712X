import pandas as pd
from download import download
from asltam.io import url_dist, path_dist

class load_dist :
	def __init__(self, url = url_dist, target = path_dist):
		download(url, target, replace = False)

	def save_as_dist(index=None):
		df_dist = pd.read_csv(path_dist, index_col=index)
		return df_dist
	def subdata_dist(data, index):
        	return data.iloc[index][data.columns[index]]
	
