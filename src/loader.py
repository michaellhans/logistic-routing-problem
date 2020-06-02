# loader.py
# Contain of all module to generate graph

from point import *
import numpy as np

# Load Coordinate of the City
def LoadCoordinate(fileName):
    f = open("../test/"+fileName, "r")
    text = f.read()
    f.close()
    maps = {}
    x = text.split("\n")
    for node in x:
        city = []
        city = node.split(" ")
        coordinate = Point(city[1], city[2])
        maps.update({city[0] : coordinate})
    return maps

# Load every street or edge of the map
def LoadStreet(fileName):
    f = open("../test/"+fileName, "r")
    text = f.read()
    f.close()
    streets = []
    x = text.split("\n")
    for edge in x:
        streetInfo = edge.split(" ")
        streets.append(streetInfo)
    return streets

# Convert from streets info into Graph
def ConvertStreetsIntoGraph(streets, numOfCity):
    graphMatrix = [[np.inf for j in range(numOfCity)] for i in range(numOfCity)]
    for edge in streets:
        graphMatrix[int(edge[1])-1][int(edge[2])-1] = float(edge[3])
        graphMatrix[int(edge[2])-1][int(edge[1])-1] = float(edge[3])
    return graphMatrix

# Print matrix into screen
def PrintMatrix (A, numOfCity):
    print("Graph Representation: ")
    for i in range (0,numOfCity):
        print("|", end="")
        for j in range (0,numOfCity):
            if (A[i][j] == np.inf):
                print(" ~inf~\t\t|",end="")
            else:
                print(" {:0.4f}".format(A[i][j])+"\t|",end="")
        print()
    print()

# Print each coordinate of the node from the maps
def PrintCoordinateInfo(maps):
    print("Coordinate Maps: ")
    for node in maps:
        print(node, "->", maps[node].printInfo())
    print()

# Print each coordinate of the destination from the maps
def PrintCoordinateInfoFromDestination(maps, destination):
    print("Depot Coordinate Maps: ")
    for city in destination:
        print(city, "->", maps[city].printInfo())
    print()

# Print each street info and its distance from the streets
def PrintStreetInfo(streets):
    print("Streets of the Maps: ")
    for edge in streets:
        print(edge[0], ":", edge[1], "->", edge[2], "=", edge[3])
    print()

# Get boolean streets, will be used on visualizing
def GetBooleanStreets(streets):
    boolStreets = {}
    for i in range(len(streets)):
        label = streets[i][1] + '-' + streets[i][2]
        boolStreets.update({label:-1})
    return boolStreets

# Test the routed street on boolStreets
def TestRoutedStreet(boolStreets):
    for key in boolStreets:
        if (boolStreets[key] > -1):
            print(key,"->","HeyTayo!")