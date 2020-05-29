# mtsp.py
# Contain all procedure and function to execute multiple TSP
# Basic : Reduced cost matrix TSP

from tsp import *

# Crosscheck if the city of i has already visited
def ApplyVisitedCity(QueueRoute, i, length, visitedCities):
    visitedCities[i] = 1
    for routeP in QueueRoute:
        for k in range(length):
            routeP[1][i][k] = -999
            routeP[1][k][i] = -999 

def IsAllVisitedV2(visitedCities):
    for node in visitedCities:
        if (node == 0):
            return False
    return True

# Driver for TSP
maps = {}
fileNode = input("Masukkan nama file koordinat  : ")
fileEdge = input("Masukkan nama file jalanan    : ")
numOfPerson = input("Masukkan banyaknya salesman    : ")
maps = LoadCoordinate(fileNode)
streets = LoadStreet(fileEdge)
PrintCoordinateInfo(maps)
PrintStreetInfo(streets)
length = len(maps)
visitedCities = [0 for i in range (length)]

# Visualize the Map
VisualizeComplexGraph(0, streets, [], maps, length)

graphMatrix = ConvertStreetsIntoGraph(streets, length)
PrintMatrix(graphMatrix, length)

MBase, rootcost = GetReducedMatrix(graphMatrix, length)
PrintMatrix(MBase, length)
print("Reduced root cost =", rootcost)
print("Start here")
input()

QueueRoute = [[] for i in range(numOfPerson)]
DeadEnd = []
BaseCity = 0
routeParent = [BaseCity]
count = 0
for i in range(numOfPerson):
    QueueRoute[i].append([rootcost, MBase, count, routeParent])
for i in range(numOfPerson):
    DeadEnd.append(0)
lastVisit = 0

while (not(IsAllVisitedV2(visitedCities))):
    penalty = 0
    for i in range(numOfPerson):
        if (not(DeadEnd[i])):
            if (len(QueueRoute[i]) == 0):
                print("Rute perjalanan bolak-balik tidak ditemukan!")
                DeadEnd[i] = 1
                break

            nextState = QueueRoute[i].pop(0)
            MBase = nextState[1]
            StartingCity = nextState[3][-1]
            routeParent = nextState[3]
            visitedCities[routeParent] = 1
            rootcost = nextState[0]
            if (lastVisit > 0):
                ApplyVisitedCity(QueueRoute, lastVisit, length, visitedCities)

            for j in range(length):
                route = []
                route = route + routeParent
                if ((MBase[StartingCity][j] != -999) and (visitedCities[j] != 1)):
                    count += 1
                    temp = MBase[StartingCity][j]
                    print("Simpul",count,":",StartingCity, "->", j)
                    PrintMatrix(MBase, length)
                    M, cost = CalculateCost(MBase, length, StartingCity, j, BaseCity)
                    PrintMatrix(M, length)
                    finalcost = rootcost + temp + cost
                    print("Reduced total cost = "+str(rootcost)+" + "+"M["+str(StartingCity)+","+str(j)+"] + "+str(cost)+" = "+str(finalcost))
                    route.append(j)
                    print("Route for node",count,"==>",end=" ")
                    PrintRoute(route)
                    QueueRoute[i].append([finalcost, M, count, route])
                    input()

            QueueRoute[i].sort()
            lastVisit = QueueRoute[i][0][3][-1]
            
        else:
            penalty += 1
    if (penalty == numOfPerson):
        print("Newman, you're done!")

if (IsAllVisited):
    print("Rute telah ditemukan!")
    routeParent.append(BaseCity)
    print("Rute perjalanan terpendek TSP adalah ",end=" ")
    PrintRoute(routeParent)
    print("Jarak tempu perjalanan =", rootcost, "km")
else:
    print("Tidak ada rute perjalanan terpendek TSP yang tersedia!")

VisualizeGraph(streets, routeParent, length, fileNode)
VisualizeComplexGraph(BaseCity, streets, routeParent, maps, length)