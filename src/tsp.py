# tsp.py
# Contain all function and procedure to execute TSP
# Using reduced cost matrix

from graph import *
from visualizer import *
from complexVisualizer import *

# function CopyMatriks (input A: Matriks) -> Matriks
# Mengembalikan matriks yang merupakan hasil salinan dari matriks A
def CopyMatriks (A, length):
    M = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            M[i][j] = A[i][j]
    return M

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
    MTemp = CopyMatriks(M, length)
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
    MCopy = CopyMatriks(M, length)
    for k in range (length):
        MCopy[i][k] = -999
    for k in range (length):
        MCopy[k][j] = -999
    MCopy[j][i] = -999
    MCopy[j][BaseCity] = -999
    return GetReducedMatrix(MCopy, length)

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

# Calculate the cost of the route
def CalculateRouteCost(route, MRoot):
    total = 0
    for i in range (len(route)-1):
        total += MRoot[i][i+1]
    return total

# Is there a road
def IsStreetAvailable(origin, destination, MRoot):
    return (MRoot[origin][destination] != -999)

# Driver for TSP
maps = {}
fileNode = input("Masukkan nama file koordinat  : ")
fileEdge = input("Masukkan nama file jalanan    : ")
maps = LoadCoordinate(fileNode)
streets = LoadStreet(fileEdge)
PrintCoordinateInfo(maps)
PrintStreetInfo(streets)
length = len(maps)

# Visualize the Map
VisualizeComplexGraph(0, streets, [], maps, length)

graphMatrix = ConvertStreetsIntoGraph(streets, length)
PrintMatrix(graphMatrix, length)

MBase, rootcost = GetReducedMatrix(graphMatrix, length)
MFirst = CopyMatriks(MBase, length)
PrintMatrix(MBase, length)
print("Reduced root cost =", rootcost)
print("Start here")

routeParent = [0]
QueueRoute = []
StartingCity = 0
BaseCity = StartingCity
count = 0
while (not(IsAllVisited(MBase, length))):
    for j in range(length):
        route = []
        route = route + routeParent
        if (MBase[StartingCity][j] != -999):
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
            QueueRoute.append([finalcost, M, count, route])
            input()

    QueueRoute.sort()
    if (len(QueueRoute) == 0):
        print("Rute perjalanan bolak-balik tidak ditemukan!")
        break

    nextState = QueueRoute.pop(0)
    MBase = nextState[1]
    StartingCity = nextState[3][-1]
    routeParent = nextState[3]
    rootcost = nextState[0]

if (IsAllVisited):
    print("Rute telah ditemukan!")
    routeParent.append(BaseCity)
    print("Rute perjalanan terpendek TSP adalah ",end=" ")
    PrintRoute(routeParent)
    print("Jarak tempuh perjalanan =", rootcost, "km")
else:
    print("Tidak ada rute perjalanan terpendek TSP yang tersedia!")

VisualizeGraph(streets, routeParent, length, fileNode)
VisualizeComplexGraph(BaseCity, streets, routeParent, maps, length)