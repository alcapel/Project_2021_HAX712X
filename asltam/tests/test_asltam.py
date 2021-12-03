import sys
import os.path
import download
import pandas as pd
import networkx as nx
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)
import asltam as atm
from asltam.io.pricedist import *
from asltam.graph.graph import get_subgraph_under_k


def test_get_index():
    a = atm.load_price().save_as_price(index=' ')
    assert get_index(data=a, name='SETE') == 1


def test_get_index():
    a = atm.load_price().save_as_price(index=' ')
    assert get_index(data=a, name='SETE') == 1


def test_get_index_list():
    a = atm.load_price().save_as_price(index=' ')
    assert get_index(data=a, name=['SETE', 'LEZIGNAN']) == [1, 13]


def test_get_way():
    a = atm.load_dist().save_as_dist(index=' Nom gare ')
    assert get_way(data_dist=a, start='MONTPELLIER', target='AGDE') == ['MONTPELLIER', 'SETE', 'AGDE']


def test_average_cost():
    a = atm.load_price().save_as_price(index=' ')
    b = atm.load_dist().save_as_dist(index=' Nom gare ')
    assert np.allclose(average_cost(data_price=atm.load_price.subdata_price(a, [0, 1]),
    data_dist=atm.load_dist.subdata_dist(b, [0,1])),
    np.array([[0, 1.6/17.0], [1.6/17.0, 0]]))


def test_average_cost_list():
    a = atm.load_price().save_as_price(index=' ')
    b = atm.load_dist().save_as_dist(index=' Nom gare ')
    assert np.allclose(
                       average_cost_list(data_price=atm.load_price.subdata_price(a, [0, 1]),
                       data_dist=atm.load_dist.subdata_dist(b, [0, 1])),
                       np.array([1.6/17.0]))


def test_get_subgraph_under_k():
    a = atm.load_price().save_as_price(index=' ')
    g = get_subgraph_under_k(atm.load_price.subdata_price(a, range(4)), 1)
    assert [tuple(g[0].nodes), tuple(g[1].nodes), tuple(g[2].nodes)] == [('MONTPELLIER', 'BEZIERS CABRIALS (SORTIE)'),
                                                                        ('MONTPELLIER', 'SETE', 'BEZIERS CABRIALS (SORTIE)'),
                                                                        ('MONTPELLIER', 'AGDE', 'BEZIERS CABRIALS (SORTIE)')]


def test_kmin_cost_out():
    a = atm.load_price().save_as_price(index=' ')
    b = atm.load_dist.save_as_dist(index=' Nom gare ')
    assert atm.kmin_cost_out(data_price=a,
                            data_dist=b,
                            start='MONTPELLIER',
                            target='BEZIERS CABRIALS (SORTIE)', k=1) == (['MONTPELLIER', 'AGDE', 'BEZIERS CABRIALS (SORTIE)'], 4.6)
