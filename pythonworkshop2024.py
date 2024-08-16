import os
import csv
import requests
import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib_venn

print("all packages have been imported successfully!")

#define the data
groupone = set(["oak", "oak", "pecan", "walnut","bald cypress","sycamore"])
grouptwo = set(["pecan","walnut","black locust","elm"])

#create venn diagram
matplotlib_venn.venn2((groupone, grouptwo), ("Park 1 Trees", "Park 2 Trees"))


#show figure
plt.show()






