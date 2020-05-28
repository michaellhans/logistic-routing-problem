# Graph.py
# Contain of all module to generate graph

from point import *

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

# Print each coordiante of the node from the maps
def PrintCoordinateInfo(maps):
    for node in maps:
        print(node, "->", maps[node].printInfo())

# Driver for Graph
maps = {}
maps = LoadCoordinate("SthyrelestNode.txt")
PrintCoordinateInfo(maps)