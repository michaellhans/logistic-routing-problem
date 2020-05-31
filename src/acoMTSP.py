# aco.py
# Calculate mTSP route with ant colony optimization

from graph import *
from complexVisualizer import *
from visualizer import *
from ant_colony import *
import more_itertools as mit
import random

# Crosscheck if the city of i has already visited
def ApplyVisitedCity(M, length, i):
    for k in range(length):
        M[i][k] = np.inf
        M[k][i] = np.inf 

# Convert from List of Path into Route
def ConvertIntoRoute(listOfPath):
    route = []
    startcity = listOfPath[0][0][0]
    route.append(startcity)
    for path in listOfPath[0]:
        route.append(path[1])
    return route

def SubGraph(G, subCities, totalCities):
    iterable = [i+1 for i in range(totalCities)]
    print(iterable)
    for i in range(len(subCities)):
        iterable.remove(subCities[i])
    print(iterable)
    SubG = []
    subCities.sort()
    print(subCities)
    i = 0
    while (i < totalCities):
        if (i+1 not in iterable):
            Row = []
            j = 0
            while (j < totalCities):
                print(i,",",j,"->",G[i][j])
                if (j+1 not in iterable):
                    Row.append(G[i][j])
                j += 1
            SubG.append(Row)
        i += 1
    PrintMatrix(SubG, len(subCities))
    return SubG

# Create all sub graphs according to list of sub cities
def CreateAllSubGraphs(G, listOfSubCities, numOfCities):
    TotalMaps = []
    for i in range(len(listOfSubCities)):
        TotalMaps.append(SubGraph(G, listOfSubCities[i], numOfCities))
        input()
    return TotalMaps

# Divide a graph into n subgraph
def CitiesIntoSubCities(numOfCity, numOfSalesman, baseCity):
    cities = []
    for i in range(numOfCity):
        cities.append(int(i+1))
    print(cities)
    random.shuffle(cities)
    print(cities)
    cities.remove(baseCity)
    partition = [list(c) for c in mit.divide(numOfSalesman, cities)]
    listOfSubCities = [[baseCity], [baseCity]]
    for i in range(numOfSalesman):
        listOfSubCities[i] = listOfSubCities[i] + partition[i]
    return listOfSubCities 

# Validize the route into the real route
def ValidizeRoute(rawRoute, subcities):
    for i in range(len(rawRoute)):
        rawRoute[i] = subcities[rawRoute[i]]

# Print route
def PrintRoute(route):
    for i in range (len(route)-1):
        print(route[i],"->", end=" ")
    print(route[len(route)-1])

# Driver for TSP with ACO
maps = {}
# fileNode = input("Masukkan nama file koordinat\t: ")
# fileEdge = input("Masukkan nama file jalanan\t: ")
# numOfSalesman = int(input("Masukkan jumlah salesman\t: "))
# baseCity = int(input("Masukkan kota depot / asal\t: "))
fileNode = "MTSPNode2.txt"
fileEdge = "MTSPEdge2.txt"
numOfSalesman = 2
baseCity = 1
maps = LoadCoordinate(fileNode)
streets = LoadStreet(fileEdge)
PrintCoordinateInfo(maps)
PrintStreetInfo(streets)
length = len(maps)

# Visualize the Map
VisualizeComplexGraph(0, streets, [], maps, length)
ListOfSubCities = CitiesIntoSubCities(length, numOfSalesman, baseCity)
print(ListOfSubCities)


MBase = ConvertStreetsIntoGraph(streets, length)
PrintMatrix(MBase, length)

for j in range(10):
    MSub = []
    MSub = CreateAllSubGraphs(MBase, ListOfSubCities, length)
    routes = []
    for i in range(numOfSalesman):
        ant_colony = AntColony(np.array(MSub[i]), 1, 1, 100, 0.95, alpha=1, beta=1)
        shortest_path = ant_colony.run()
        print ("Shortest path: {}".format(shortest_path))
        routeParent = ConvertIntoRoute(shortest_path)
        ValidizeRoute(routeParent, ListOfSubCities[i])
        print ("Jarak tempuh untuk sales ke-"+str(i+1)+" adalah "+str(shortest_path[1])+" km")
        PrintRoute(routeParent)
        routes.append(routeParent)
        input()
    # VisualizeGraph(streets, routeParent, length, fileNode)
    # VisualizeComplexGraph(shortest_path[0][0][0], streets, routeParent, maps, length)
    VisualizeComplexGraphMTSP(shortest_path[0][0][0], streets, routes, maps, length)
