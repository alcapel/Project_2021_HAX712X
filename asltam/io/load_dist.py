import pandas as pd
from download import download
from asltam.io import url_dist, path_dist

class load_dist :
	def __init__(self, url = url_dist, target = path_dist):
		download(url, target, replace = False)

	def save_as_dist():
		df_dist = pd.read_csv(path_dist)
		return df_dist