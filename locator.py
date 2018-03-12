#Lane Larochelle
#March 8th 2018 

# x is in meters
# y is corresonding rssi

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

##FAIR WARNING THESE ARE A LITTLE TAPERED AS TO CREATE A GRADIENT 
known_points = np.array([(0, -24), (.25, -42.67), (.5, -63.667), (.75, -69), (1,-79), (1.25, -82), (1.5, -79.33), (1.75, -85.33), (2, -86.33), (2.25, -88.33), (2.5,-90), (2.75,-90.33), (3,-91)])
meters = points[:,0]
rssis = points[:,1]

