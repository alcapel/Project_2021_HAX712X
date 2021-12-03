import pandas as pd
from download import download
from asltam.io import url_price, path_price

class load_price :
	def __init__(self, url = url_price, target = path_price):
		download(url, target, replace = False)

	@staticmethod
	def save_as_price(index=None):
		df_price = pd.read_csv(path_price, index_col=index)
		return df_price
	
	def subdata_price(data, index):
        	return data.iloc[index][data.columns[index]]
