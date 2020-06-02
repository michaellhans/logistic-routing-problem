# route.py
# Contain every module about routing

from ant_colony import *
import more_itertools as mit
import random

# Create list of destination coordinates
def CreateListCoordinate(cities, maps):
    listCoordinate = []
    for city in cities:
        listCoordinate.append([city, maps[city]])
    return listCoordinate

# Convert from List of Path based on Matrix into the real route
def ConvertIntoRoute(listOfPath):
    route = []
    startcity = listOfPath[0][0][0]
    route.append(startcity)
    for path in listOfPath[0]:
        route.append(path[1])
    return route

# Divide a graph into numOfSalesman subgraph
def splitCities(cities, numOfSalesman, originCity, maps):
    listCoordinate = CreateListCoordinate(cities, maps)
    listCoordinate.sort(key = lambda x : x[1])
    listCoordinate.remove([originCity, maps[originCity]])
    citiesNoOrigin = [listCoordinate[i][0] for i in range(len(listCoordinate))]
    partition = [list(c) for c in mit.divide(numOfSalesman, citiesNoOrigin)]
    listOfSubCities = []
    for i in range(numOfSalesman):
        listOfSubCities.append([originCity])
        listOfSubCities[i] = listOfSubCities[i] + partition[i]
    return listOfSubCities 

# Print the real route
def PrintRoute(route):
    for i in range (len(route)-1):
        print(route[i],"->", end=" ")
    print(route[len(route)-1])

# Print the salesman destination
def PrintDestination(dest, k):
    if (k == 0):
        print("Daftar destinasi yang akan dikunjungi: ",end="")
    else:
        print("Daftar destinasi yang akan dikunjungi sales ke-"+str(k+1)+": ",end="")
    for i in range (len(dest)-1):
        print(dest[i]+",",end=" ")
    print(dest[len(dest)-1])
    if (k == 0):
        print("Cabang pusat logistik berada pada kota "+dest[i])
    print()


# Milestone 2 : Print all every route solution
# Print the route solution and its distance length
def PrintAllSolution(solution, numOfSalesman):
    totalDistance = 0
    for i in range(numOfSalesman):
        print(str(i+1)+". Perjalanan sales ke-"+str(i+1)+": ")
        print("Jarak tempuh untuk sales ke-"+str(i+1)+" adalah "+str(solution[i][2])+" km.")
        print("Rute sederhana perjalanan untuk sales ke-"+str(i+1)+" adalah :")
        PrintRoute(solution[i][0])
        print("Rute asli perjalanan untuk sales ke-"+str(i+1)+" adalah :")
        PrintRoute(solution[i][1])
        print()
        totalDistance += solution[i][2]

    print ("Jarak tempuh total setiap salesman adalah "+str(totalDistance)+" km.")

# Validize the route into the real route
def raw_into_simple_route(rawRoute, subcities):
    simple_route = []
    for i in range(len(rawRoute)):
        simple_route.append(subcities[rawRoute[i]])
    return simple_route

# Convert from raw route from A* Matrix into the real route from the maps
def raw_into_real_route(trail, routes):
    realPath = []
    originCity = trail[0]
    realOriginCity = routes[int(originCity)][1][0]
    for i in range(len(trail)-1):
        realPath = realPath + routes[int(originCity)][int(trail[i+1])]
        realPath.pop()
        originCity = trail[i+1]
    realPath.append(realOriginCity)
    return realPath

# Apply every route to be visualized with different color according to which salesman it is
def apply_route_on_streets(all_real_path, boolStreets):
    for i in range(len(all_real_path)):
        for j in range(len(all_real_path[i])-1):
            label = str(all_real_path[i][j]) + '-' + str(all_real_path[i][j+1])
            value = boolStreets.get(label)
            if (value == None):
                label = str(all_real_path[i][j+1]) + '-' + str(all_real_path[i][j])
            boolStreets[label] = i