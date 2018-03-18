#Lane Larochelle
#March 8th 2018 

# x is in meters
# y is corresonding rssi
#i get a compilation error about plotly I just left it

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import scipy

##FAIR WARNING THESE ARE A LITTLE TAPERED AS TO CREATE A GRADIENT 
known_points = np.array([(0, -24), (.25, -42.67), (.5, -63.667), (.75, -69), (1,-79), (1.25, -82), (1.5, -79.33), (1.75, -85.33), (2, -86.33), (2.25, -88.33), (2.5,-90), (2.75,-90.33), (3,-91)])
meters = known_points[:,0]
rssis = known_points[:,1]


#these values are with respect tothe bottom left corner (0,0,0)->(x,y,z) in meters
#p1 has to be (0,0,0) 
#p2 is (d,0)
#p3 is (i,j)
# THIS IS AS FAR AS WIKI SAYS

class trilatBoy():
    p1=(0,0,0)
    p2=(0,0,0)
    p3=(0,0,0)
    d=0
    i=0
    j=0
    def __init__(self,p1,p2,p3,d,i,j):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.d=d
        self.i=i
        self.j=j

    def clear(self):
        self.p1=(0,0,0)
        self.p2=(0,0,0)
        self.p3=(0,0,0)
        self.d=0
        self.i=0
        self.j=0

cal = [0.2254, -3.964, 24.994, -71.136, 96.131, 23.408]

def convert(rssi):
    if rssi > 0:
        return None
    cal[-1] = cal[-1] + rssi
    vals = np.roots(cal)
    while vals[-1].imag != 0:
        vals = vals[:-1]
    dist = vals[-1].real
    return dist

def rssi_to_meter(rssi0, rssi1, rssi2):
    #use the equation so meter[0] = rssi0 etc, return the whole fucking unit
    rssi = [rssi0, rssi1, rssi2]
    meter = []
    for i in range(3):
        meter.append(convert(rssi[i]))
    return meter

def trilatterate(boy, rssis):
    meter = rssi_to_meter(rssis[0], rssis[1], rssis[2])
    print(str(meter[0]) +" "+  str(meter[1]) +" "+  str(meter[2])
    xpos=((meter[0]**2) - (meter[1]**2)+(boy.d**2))/(2*boy.d)
    ypos=(((meter[0]**2)-(meter[2]**2)+(boy.i**2)+(boy.j**2))/(2*boy.j))-((boy.i/boy.j)*xpos)
    zpos1=((meter[0]**2)-(xpos**2)-(ypos**2))**(1/2)
    zpos2=(((meter[0]**2)-(xpos**2)-(ypos**2))**(1/2))*(-1)
    ### needs a way to select the correct z value from the 2 or we can just discard z as we can assume there are all on the same plane

    xpos = xpos * 100
    ypos = ypos * 100
    return (xpos,ypos)

