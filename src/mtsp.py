# mtsp.py
# Contain all procedure and function to execute multiple TSP
# Basic : Reduced cost matrix TSP

from tsp import *

# Crosscheck if the city of i has already visited
def ApplyVisitedCity(QueueRoute, i, length, visitedCities, person):
    visitedCities[i] = 1
    for m in range(len(QueueRoute)):
        if (m != person):
            for k in range(length):
                QueueRoute[m][0][1][i][k] = -999
                QueueRoute[m][0][1][k][i] = -999 

def IsAllVisitedV2(visitedCities):
    for node in visitedCities:
        if (node == 0):
            return False
    return True

# Driver for TSP
maps = {}
fileNode = input("Masukkan nama file koordinat  : ")
fileEdge = input("Masukkan nama file jalanan    : ")
numOfPerson = int(input("Masukkan banyaknya salesman    : "))
maps = LoadCoordinate(fileNode)
streets = LoadStreet(fileEdge)
PrintCoordinateInfo(maps)
PrintStreetInfo(streets)
length = len(maps)
visitedCities = [0 for i in range (length)]

# # Visualize the Map
# VisualizeComplexGraph(0, streets, [], maps, length)

graphMatrix = ConvertStreetsIntoGraph(streets, length)
PrintMatrix(graphMatrix, length)

MBase, rootcost = GetReducedMatrix(graphMatrix, length)
MRoot = CopyMatriks(MBase, length)
PrintMatrix(MBase, length)
print("Reduced root cost =", rootcost)
print("Start here")
input()

QueueRoute = [[] for i in range(numOfPerson)]
DeadEnd = []
BaseCity = 0
visitedCities[BaseCity] = 1
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
        print("Orang ke-"+str(i+1))
        if (not(DeadEnd[i])):
            if (len(QueueRoute[i]) == 0):
                print("Rute perjalanan bolak-balik tidak ditemukan!")
                DeadEnd[i] = 1
                break

            if (lastVisit > 0):
                ApplyVisitedCity(QueueRoute, lastVisit, length, visitedCities, (i-1) % numOfPerson)

            nextState = QueueRoute[i].pop(0)
            MBase = nextState[1]
            StartingCity = nextState[3][-1]
            routeParent = nextState[3]
            rootcost = nextState[0]

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
        break
    for i in range(numOfPerson):
        PrintRoute(QueueRoute[i][0][3])

if (IsAllVisited):
    print("Rute telah ditemukan!")
    listOfRoute = []
    totalCost = 0
    for i in range(numOfPerson):
        print(str(i+1)+" Rute Sales ke-"+str(i+1))
        result = QueueRoute[i][0]
        if (IsStreetAvailable(result[3][-1], BaseCity, MRoot)):
            result[3].append(BaseCity)
            print("Rute perjalanan memenuhi Traveling Salesperson Problem!")
            costPerson = result[0]
        else:
            print("Rute perjalanan tidak kembali ke tempat asal!")
            costPerson = CalculateRouteCost(result[3], MRoot)
        totalCost += costPerson
        print("Rute perjalanan orang ke-"+str(i+1)+" adalah ",end=" ")
        PrintRoute(result[3])
        print("Jarak tempuh perjalanan =", totalCost, "km")
        listOfRoute.append(result[3])
    print("Total jarak tempuh setiap salesman adalah", totalCost, "km")
else:
    print("Tidak ada rute perjalanan terpendek TSP yang tersedia!")

# VisualizeGraphMTSP(streets, routeParent, length, fileNode)
VisualizeComplexGraphMTSP(BaseCity, streets, listOfRoute, maps, length)