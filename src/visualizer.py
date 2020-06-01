# complexVisualizer.py
# Module to visualize the map and the streets in complex way
# The visualization is using matplotlib library

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

# Check if the street is in route
def CheckStreetInRoute(origin, destination, route):
    for i in range (len(route)-1):
        if ((route[i] == int(origin)) and (route[i+1] == int(destination))):
            return True
    return False

# Plot a point on workspace
def Plotting(P, name, k):
    x = float(P.getX())
    y = float(P.getY())

    # If Point P is the origin city
    if (k == 1):
        plt.plot([x], [y], 'ro', color = "green")

    # If Point P is the visited city
    elif (k == 2):
        plt.plot([x], [y], 'ro', color = "blue")

    # If Point P is the unvisited city
    else :
        plt.plot([x], [y], 'ro', color = "black")
    label = "%d(%d,%d)" % (name, x, y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# Connect two points between origin point and destination point
def ConnectPoints(maps, origin, destination, cost, flag):
    x1, x2 = float(maps[origin].getX()), float(maps[destination].getX())
    y1, y2 = float(maps[origin].getY()), float(maps[destination].getY())

    # If the edge between origin and destination is on the route
    if (flag):
        plt.plot([x1,x2],[y1,y2],'k-', color = "red")
    
    # The edge between origin and destination is not on the route
    else:
        plt.plot([x1,x2],[y1,y2],'k-', color = "yellow")

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

# Generate about numOfRoute random color to distinguish every salesman route
def generateRandomColor(numOfRoute):
    colors = []
    for i in range(numOfRoute):
        r = random.random()
        g = random.random()
        b = random.random()
        colors.append([r,g,b])
    return colors

# Visualize the graph from street, route, and length of the map information for Multiple TSP Problem
def VisualizeComplexGraph(basecity, streets, listOfRoute, maps, length):
    colors = generateRandomColor(len(listOfRoute))
    # Visualize every street in the map
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

    # Visualize every city in the map with black color
    for city in maps:
        Plotting(maps[city], float(city), 3)

    # Visualize every city in the route with another color
    for route in listOfRoute:
        for city in route:
            P = maps[str(city)]
            Plotting(P, city, 2)

    # Visualize origin city with green color
    P = maps[str(basecity+1)]
    Plotting(P, basecity+1, 1)

    # Create legend information based on the number of salesman
    personLegend = []
    for i in range(len(colors)):
        personLabel = 'Sales ke-' + str(i+1)
        personLegend.append(mpatches.Patch(color=colors[i], label=personLabel))
    plt.legend(handles=personLegend)

    plt.axis('equal')
    plt.title('Logistic Routing Problem')
    plt.show()