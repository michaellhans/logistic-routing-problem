# tsp.py
# Contain all function and procedure to execute TSP
# Using reduced cost matrix

from graph import *

# Get minimum value of the row i
def MinRow(M, i, length):
    min = 999999
    for j in range (length):
        if (M[i][j] != -999):
            if (M[i][j] < min):
                min = M[i][j]
    return min

# Get minimum value of the column j
def MinColumn(M, j, length):
    min = 999999
    for i in range (length):
        if (M[i][j] != -999):
            if (M[i][j] < min):
                min = M[i][j]
    return min

# Reduced row i on M with k value
def ReducedCertainRow(M, i, length, k):
    for j in range (length):
        if (M[i][j] != -999):
            M[i][j] = M[i][j] - k

# Reduced column j on M with k value
def ReducedCertainColumn(M, j, length, k):
    for i in range (length):
        if (M[i][j] != -999):
            M[i][j] = M[i][j] - k

# Check if there are at least one zero in row i
def CheckZeroInRow(M, i, length):
    count = 0
    for j in range (length):
        if (M[i][j] == 0):
            return True
        if (M[i][j] == -999):
            count += 1
    if (count == length):
        return True
    else:
        return False

# Check if there are at least one zero in column j
def CheckZeroInColumn(M, j, length):
    count = 0
    for i in range (length):
        if (M[i][j] == 0):
            return True
        if (M[i][j] == -999):
            count += 1
    if (count == length):
        return True
    else:
        return False

# Get Reduced Matrix using Reduced Cost Matrix
def GetReducedMatrix(M, length):
    MTemp = M
    cost = 0
    # Make at least one zero in every row
    for i in range (length):
        if (not(CheckZeroInRow(MTemp, i, length))):
            min = MinRow(MTemp, i, length)
            cost += min
            ReducedCertainRow(MTemp, i, length, min)

    # Make at least one zero in every column
    for j in range (length):
        if (not(CheckZeroInColumn(MTemp, j, length))):
            min = MinColumn(MTemp, j, length)
            cost += min
            ReducedCertainColumn(MTemp, j, length, min)

    return MTemp, cost

# Applying three golden rules for reduced cost matrix
def CalculateCost(M, length, i, j, BaseCity):
    MTemp = M
    for k in range (length):
        MTemp[i][k] = -999
    for k in range (length):
        MTemp[k][j] = -999
    MTemp[j][i] = -999
    MTemp[j][BaseCity] = -999
    return GetReducedMatrix(MTemp, length)

# Applying three golden rules for reduced cost matrix
def ApplyTheRules(M, length, i, j):
    for k in range (length):
        M[i][k] = -999
    for k in range (length):
        M[k][j] = -999
    M[j][i] = -999

# Check if all city is visited
def IsAllVisited(M, length):
    for i in range(length):
        for j in range(length):
            if (M[i][j] != -999):
                return False
    return True

# Print route
def PrintRoute(route):
    for i in range (len(route)-1):
        print(route[i],"->", end=" ")
    print(route[len(route)-1])

# Driver for TSP
maps = {}
maps = LoadCoordinate("SthyrelestNode.txt")
PrintCoordinateInfo(maps)
streets = LoadStreet("SthyrelestEdge.txt")
PrintStreetInfo(streets)
length = len(maps)
graphMatrix = ConvertStreetsIntoGraph(streets, length)
PrintMatrix(graphMatrix, length)

MTemp, rootcost = GetReducedMatrix(graphMatrix, length)
PrintMatrix(MTemp, length)
print("Reduced root cost =", rootcost)
print("Start here")
# ApplyTheRules(MTemp, length, 0, 1)
# PrintMatrix(MTemp, length)

routeParent = [0]
QueueRoute = []
StartingCity = 0
BaseCity = StartingCity
count = 0
while (not(IsAllVisited(MTemp, length))):
    for j in range(length):
        route = routeParent
        if (MTemp[StartingCity][j] != -999):
            count += 1
            temp = MTemp[StartingCity][j]
            print("Simpul",count,":",StartingCity, "->", j)
            M, cost = CalculateCost(MTemp, length, StartingCity, j, BaseCity)
            PrintMatrix(M, length)
            finalcost = rootcost + temp + cost
            print("Reduced total cost = "+str(rootcost)+" + "+"M["+str(StartingCity)+","+str(j)+"] + "+str(cost)+" = "+str(finalcost))
            route.append(j)
            print("Route for node",count,"==>",end=" ")
            PrintRoute(route)
            QueueRoute.append([count, M, finalcost, route])
            input()
    QueueRoute.sort()

    if (len(QueueRoute) == 0):
        print("Rute perjalanan bolak-balik tidak ditemukan!")
        break

    nextState = QueueRoute.pop()
    MTemp = nextState[1]
    StartingCity = nextState[3][-1]
    routeParent = nextState[3]
    rootcost = nextState[2]

if (IsAllVisited):
    print("Rute telah ditemukan!")
    routeParent.append(BaseCity)
    print("Rute perjalanan terpendek TSP adalah ",end=" ")
    PrintRoute(routeParent)
    print("Jarak tempu perjalanan =", rootcost, "km")
else:
    print("Tidak ada rute perjalanan terpendek TSP yang tersedia!")