import ipywidgets as widgets
from ipywidgets import interactive
from functools import partial
import matplotlib.pyplot as plt

import sys
import os
sys.path.insert(0,  os.path.abspath(os.path.join(os.getcwd(), "../..")))
from corpora import achP

def ashMenu(data):
 distance=widgets.Dropdown(description="distance :",options=["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", "dice", "euclidean", "hamming", "jaccard", "jensenshannon", "kulczynski1", "mahalanobis", "matching", "minkowski", "rogerstanimoto", "russellrao", "seuclidean", "sokalmichener", "sokalsneath", "sqeuclidean", "yule"],value="euclidean")
 method=widgets.Dropdown(description="méthode :",options=["single","complete","average","weighted","centroid","median","ward"],value="ward")
 button = widgets.Button(description='Run')
 nbclasse=widgets.IntText(description="nb classes :",value="3")

 display(distance)
 display(method)
 display(nbclasse)
 display(button)
 print("heoo")

 button.on_click(achP(data=data, method=method.value, distance=distance.value, nbclasse=nbclasse.value))
