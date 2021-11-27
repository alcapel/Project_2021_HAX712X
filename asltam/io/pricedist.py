import numpy as np
import pandas as pd


def average_cost(data_price, data_dist):
    """
    Retourne la matrice des prix moyens.
    """
    n = len(data_price)
    p = np.array(data_price)
    d = np.array(data_dist)
    return p/d


def average_cost_list(data_price, data_dist):
    """
    Retourne la liste des prix moyens.
    """
    n = len(data_price)
    p = np.array(data_price)[np.triu_indices(n, k=1)]
    d = np.array(data_dist)[np.triu_indices(n, k=1)]
    return p/d
  
