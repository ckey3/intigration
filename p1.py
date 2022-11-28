from cmath import pi
import numpy as np
import time
from ezGraph import *

dx = 1
x=0
y=4
nsteps = 5

# Graph
graph = ezGraph(xmin=0, xmax=6, ymin = 0, ymax=20, xLabel="x", yLabel="y")
graph.add(x,y) #add


for i in range(nsteps):
    x = x + dx
    slope = x/5
    dy = slope * dx
    y = y + dy
    print(x,y)
    graph.add(x, y)

graph.keepOpen() 