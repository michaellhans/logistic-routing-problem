# complexVisualizer.py
# Module to visualize the map and the streets in complex way

import matplotlib.pyplot as plt
from visualizer import CheckStreetInRoute

# Plot a point on workspace
def Plotting(P, name, flag):
    x = int(P.getX())
    y = int(P.getY())
    if flag:
        plt.plot([x], [y], 'ro', color = "green")
    else:
        plt.plot([x], [y], 'ro', color = "blue")
    label = "%d(%d,%d)" % (name, x, y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# Connect two points
def ConnectPoints(maps, origin, destination, cost, flag):
    x1, x2 = int(maps[origin].getX()), int(maps[destination].getX())
    y1, y2 = int(maps[origin].getY()), int(maps[destination].getY())
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

    for city in route:
        P = maps[str(city+1)]
        Plotting(P, city+1, False)

    P = maps[str(basecity+1)]
    Plotting(P, basecity+1, True)

    plt.axis('equal')
    plt.title('Logistic Routing Problem')
    plt.show()