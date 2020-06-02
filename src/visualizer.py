# visualizer.py
# Module to visualize the map and the streets in complex way
# The visualization is using matplotlib library

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

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

    # If Point P is the station city
    elif (k == 3):
        plt.plot([x], [y], 'ro', color = "red")

    # If Point P is the unvisited city
    else :
        plt.plot([x], [y], 'ro', color = "silver")

    # label = "%d(%d,%d)" % (name, x, y)
    if ((k == 1) or (k == 3)):
        label = "%d" % (name)
        plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# Connect two points
def ConnectPointsRandomColor(maps, origin, destination, cost, k, colors):
    x1, x2 = float(maps[origin].getX()), float(maps[destination].getX())
    y1, y2 = float(maps[origin].getY()), float(maps[destination].getY())
    if (k >= 0):
        thecolor = colors[k]
        rgb = (thecolor[0], thecolor[1], thecolor[2])
        plt.plot([x1,x2],[y1,y2],'k-', color = rgb)
    else:
        plt.plot([x1,x2],[y1,y2],'k-', color = "silver")

# Generate about numOfRoute random color to distinguish every salesman route
def GenerateRandomColors(numOfRoute):
    colors = []
    for i in range(numOfRoute):
        r = random.random()
        g = random.random()
        b = random.random()
        colors.append([r,g,b])
    return colors

# Visualize the graph from street, route, and length of the map information for Multiple TSP Problem
def VisualizeComplexGraph(baseCity, streets, boolStreets, listOfRoute, maps, length, destination):
    colors = GenerateRandomColors(len(listOfRoute))
    # Visualize every street in the map
    for street in streets:
        # streetRoute = -1
        # for i in range(len(listOfRoute)):
        #     if ((CheckStreetInRoute(street[1], street[2], listOfRoute[i])) or (CheckStreetInRoute(street[2], street[1], listOfRoute[i]))):
        #         streetRoute = i
        #         break
        label = street[1] + '-' + street[2]
        value = boolStreets.get(label)
        streetRoute = boolStreets[label]

        ConnectPointsRandomColor(maps, street[1], street[2], street[3], streetRoute, colors)

    # Visualize every city in the map with black color
    for city in maps:
        Plotting(maps[city], float(city), 4)

    # Visualize every city in the route with blue color
    for route in listOfRoute:
        for city in route:
            P = maps[str(city)]
            Plotting(P, city, 2)

    # Visualize every city in the destination with red color
    for city in destination:
        P = maps[str(city)]
        Plotting(P, city, 3)

    # Visualize origin city with green color
    P = maps[str(baseCity)]
    Plotting(P, baseCity, 1)

    # Create legend information based on the number of salesman
    personLegend = []
    for i in range(len(colors)):
        personLabel = 'Sales ke-' + str(i+1)
        personLegend.append(mpatches.Patch(color=colors[i], label=personLabel))
    plt.legend(handles=personLegend)

    plt.axis('equal')
    plt.title('Logistic Routing Problem')
    plt.show()