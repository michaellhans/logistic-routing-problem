# complexVisualizer.py
# Module to visualize the map and the streets in complex way

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
from visualizer import CheckStreetInRoute

# Plot a point on workspace
def Plotting(P, name, k):
    x = float(P.getX())
    y = float(P.getY())
    if (k == 1):
        plt.plot([x], [y], 'ro', color = "green")
    elif (k == 2):
        plt.plot([x], [y], 'ro', color = "blue")
    else :
        plt.plot([x], [y], 'ro', color = "black")
    label = "%d(%d,%d)" % (name, x, y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# Connect two points
def ConnectPoints(maps, origin, destination, cost, flag):
    x1, x2 = float(maps[origin].getX()), float(maps[destination].getX())
    y1, y2 = float(maps[origin].getY()), float(maps[destination].getY())
    if (flag):
        plt.plot([x1,x2],[y1,y2],'k-', color = "red")
    else:
        plt.plot([x1,x2],[y1,y2],'k-', color = "black")

# Visualize the graph from street, route, and length of the map information
def VisualizeComplexGraph(basecity, streets, route, maps, length):
    for street in streets:
        if ((CheckStreetInRoute(street[1], street[2], route)) or (CheckStreetInRoute(street[2], street[1], route))):
            ConnectPoints(maps, street[1], street[2], street[3], True)
        else:
            ConnectPoints(maps, street[1], street[2], street[3], False)

    for city in maps:
        Plotting(maps[city], float(city), 3)

    for city in route:
        P = maps[str(city+1)]
        Plotting(P, city+1, 2)

    P = maps[str(basecity+1)]
    Plotting(P, basecity+1, 1)

    plt.axis('equal')
    plt.title('Logistic Routing Problem')
    plt.show()

# Connect two points
def ConnectPointsRandomColor(maps, origin, destination, cost, k, colors):
    x1, x2 = float(maps[origin].getX()), float(maps[destination].getX())
    y1, y2 = float(maps[origin].getY()), float(maps[destination].getY())
    if (k >= 0):
        thecolor = colors[k]
        rgb = (thecolor[0], thecolor[1], thecolor[2])
        plt.plot([x1,x2],[y1,y2],'k-', color = rgb)
    else:
        plt.plot([x1,x2],[y1,y2],'k-', color = "black")

def generateRandomColor(numOfRoute):
    colors = []
    for i in range(numOfRoute):
        r = random.random()
        g = random.random()
        b = random.random()
        colors.append([r,g,b])
    return colors

# Visualize the graph from street, route, and length of the map information
def VisualizeComplexGraphMTSP(basecity, streets, listOfRoute, maps, length):
    colors = generateRandomColor(len(listOfRoute))
    for street in streets:
        streetRoute = -1
        for i in range(len(listOfRoute)):
            if ((CheckStreetInRoute(street[1], street[2], listOfRoute[i])) or (CheckStreetInRoute(street[2], street[1], listOfRoute[i]))):
                streetRoute = i
                break

        if (streetRoute != -1):
            ConnectPointsRandomColor(maps, street[1], street[2], street[3], streetRoute, colors)
        else:
            ConnectPoints(maps, street[1], street[2], street[3], False)

    for city in maps:
        Plotting(maps[city], float(city), 3)

    for route in listOfRoute:
        for city in route:
            P = maps[str(city+1)]
            Plotting(P, city+1, 2)

    P = maps[str(basecity+1)]
    Plotting(P, basecity+1, 1)

    plt.axis('equal')
    plt.title('Logistic Routing Problem')

    personLegend = []
    for i in range(len(colors)):
        personLabel = 'Sales ke-' + str(i)
        personLegend.append(mpatches.Patch(color=colors[i], label=personLabel))
        
    plt.legend(handles=personLegend)
    plt.show()