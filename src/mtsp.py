# acoMTSP.py
# Calculate mTSP route with ant colony optimization

from loader import *
from visualizer import *
from ant_colony import *
from astar import *
import more_itertools as mit
import random

# Create list of destination coordinates
def CreateListCoordinate(cities, maps):
    listCoordinate = []
    for city in cities:
        listCoordinate.append([city, maps[city]])
    return listCoordinate

# Crosscheck if the city of i has already visited
def ApplyVisitedCity(M, numOfCities, i):
    for k in range(numOfCities):
        M[i][k] = np.inf
        M[k][i] = np.inf 

# Convert from List of Path based on Matrix into the real route
def ConvertIntoRoute(listOfPath):
    route = []
    startcity = listOfPath[0][0][0]
    route.append(startcity)
    for path in listOfPath[0]:
        route.append(path[1])
    return route

# Create a subgraph of G based on subCities
def SubGraph(G, subCities, totalCities):
    allCities = [i+1 for i in range(totalCities)]
    print(allCities)
    for i in range(len(subCities)):
        allCities.remove(subCities[i])
    print(allCities)
    SubG = []
    subCities.sort()
    print(subCities)
    i = 0
    while (i < totalCities):
        if (i+1 not in allCities):
            Row = []
            j = 0
            while (j < totalCities):
                print(i,",",j,"->",G[i][j])
                if (j+1 not in allCities):
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
    return TotalMaps

# Divide a graph into numOfSalesman subgraph
def CitiesIntoSubCities(numOfCity, numOfSalesman, originCity):
    cities = []
    for i in range(numOfCity):
        cities.append(int(i+1))
    print(cities)
    random.shuffle(cities)
    print(cities)
    cities.remove(originCity)
    partition = [list(c) for c in mit.divide(numOfSalesman, cities)]
    listOfSubCities = []
    for i in range(numOfSalesman):
        listOfSubCities.append([originCity])
        listOfSubCities[i] = listOfSubCities[i] + partition[i]
    return listOfSubCities 

# Divide a graph into numOfSalesman subgraph
def splitCities(cities, numOfSalesman, originCity, maps):
    listCoordinate = CreateListCoordinate(cities, maps)
    # for coordinate in listCoordinate:
    #     print(coordinate[0], "->", coordinate[1].printInfo())
    listCoordinate.sort(key = lambda x : x[1])
    # print("remove")
    listCoordinate.remove([originCity, maps[originCity]])
    # for coordinate in listCoordinate:
    #     print(coordinate[0], "->", coordinate[1].printInfo())
    citiesNoOrigin = [listCoordinate[i][0] for i in range(len(listCoordinate))]
    partition = [list(c) for c in mit.divide(numOfSalesman, citiesNoOrigin)]
    listOfSubCities = []
    for i in range(numOfSalesman):
        listOfSubCities.append([originCity])
        listOfSubCities[i] = listOfSubCities[i] + partition[i]
    return listOfSubCities 

# Validize the route into the real route
def ValidizeRoute(rawRoute, subcities):
    for i in range(len(rawRoute)):
        rawRoute[i] = subcities[rawRoute[i]]

# Print the real route
def PrintRoute(route):
    for i in range (len(route)-1):
        print(route[i],"->", end=" ")
    print(route[len(route)-1])

# Milestone 2 : Print all every route solution
# Print the route solution and its distance length
def PrintAllSolution(solution, numOfSalesman):
    totalDistance = 0
    for i in range(numOfSalesman):
        print(str(i+1)+". Perjalanan sales ke-"+str(i+1)+": ")
        print("Jarak tempuh untuk sales ke-"+str(i+1)+" adalah "+str(solution[i][1])+" km.")
        print("Rute perjalanan untuk sales ke-"+str(i+1)+" adalah ", end="")
        PrintRoute(solution[i][0])
        print()
        totalDistance += solution[i][1]

    print ("Jarak tempuh total setiap salesman adalah "+str(totalDistance)+" km.")

# # Main Program or Driver for Multiple TSP with Ant-Colony Optimization
# maps = {}
# isSuccess = False
# while (not(isSuccess)):
#     try:
#         fileNode = input("Masukkan nama file koordinat\t: ")
#         fileEdge = input("Masukkan nama file jalanan\t: ")
#         maps = LoadCoordinate(fileNode)
#         streets = LoadStreet(fileEdge)
#         numOfCities = len(maps)
#         isSuccess = True
#     except IndexError:
#         print("Terjadi kesalahan dalam pembacaan file!")
#         print("Harap masukkan file yang valid dengan format yang benar.")
#     except FileNotFoundError:
#         print("File tidak ditemukan!")

# numOfSalesman = int(input("Masukkan jumlah salesman\t: "))
# originCity = int(input("Masukkan kota depot / asal\t: "))
# # Quick test for quick debugging
# # fileNode = "MTSPNode2.txt"
# # fileEdge = "MTSPEdge2.txt"
# # numOfSalesman = 2
# # originCity = 1
# # maps = LoadCoordinate(fileNode)
# # streets = LoadStreet(fileEdge)

# # Print all information about maps coordinate and streets
# PrintCoordinateInfo(maps)
# PrintStreetInfo(streets)

# # Visualize the initial Map
# VisualizeComplexGraph(0, streets, [], maps, numOfCities)

# # Create distance matrix based on the streets information
# MBase = ConvertStreetsIntoGraph(streets, numOfCities)
# PrintMatrix(MBase, numOfCities)

# # Execute ten iterations to get the best route for all salesman
# for j in range(10):
#     ListOfMSub = []
#     ListOfSubCities = []
#     ListOfSubCities = CitiesIntoSubCities(numOfCities, numOfSalesman, originCity)
#     print(ListOfSubCities)
#     ListOfMSub = CreateAllSubGraphs(MBase, ListOfSubCities, numOfCities)
#     routes = []
#     solution = []

#     # Execute numOfSalesman TSP process and return numOfSalesman route
#     for i in range(numOfSalesman):
#         ant_colony = AntColony(np.array(ListOfMSub[i]), 1, 1, 100, 0.95, alpha=1, beta=1)
#         shortest_path = ant_colony.run()
#         print ("Shortest path: {}".format(shortest_path))
#         if (shortest_path[0] != 'placeholder'):
#             routeParent = ConvertIntoRoute(shortest_path)
#             ValidizeRoute(routeParent, ListOfSubCities[i])
#             print("Jarak tempuh untuk sales ke-"+str(i+1)+" adalah "+str(shortest_path[1])+" km")
#             print("Rute perjalanan untuk sales ke-"+str(i+1)+" adalah ", end="")
#             PrintRoute(routeParent)
#             routes.append(routeParent)
#             solution.append([routeParent, shortest_path[1]])
#         else:
#             print("Tidak terdapat rute yang memungkinkan untuk sales ke-"+str(i+1))
#             solution.append([[0], -999])
#         input()

#     # Print all solution route for every salesman and their total distance
#     PrintAllSolution(solution, numOfSalesman)

#     # Visualize the route for every salesman
#     VisualizeComplexGraph(shortest_path[0][0][0], streets, routes, maps, numOfCities)
