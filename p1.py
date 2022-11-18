from cmath import pi
import numpy as npx
import time
from ezGraph import *

dx = 1
x=0
y=4

# Graph
graph = ezGraph(xmin=0, xmax=100, xLabel="Time (s)", yLabel="Height (cm)")
graph.add(0,y) #add


for i in range(5):
    slope = x/5
    x = x +dx
    dy = slope * dx
    y = y + dy
    print(x,y)
    graph.add(x, y)

graph.keepOpen() 