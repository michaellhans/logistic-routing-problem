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
    for j in range (length):
        if (M[i][j] == 0):
            return True
    return False

# Check if there are at least one zero in column j
def CheckZeroInColumn(M, j, length):
    for i in range (length):
        if (M[i][j] == 0):
            return True
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

    PrintMatrix(MTemp, length)
    # Make at least one zero in every column
    for j in range (length):
        if (not(CheckZeroInColumn(MTemp, j, length))):
            min = MinColumn(MTemp, j, length)
            cost += min
            ReducedCertainColumn(MTemp, j, length, min)

    PrintMatrix(MTemp, length)
    return MTemp, cost

maps = {}
maps = LoadCoordinate("SthyrelestNode.txt")
PrintCoordinateInfo(maps)
streets = LoadStreet("SthyrelestEdge.txt")
PrintStreetInfo(streets)
graphMatrix = ConvertStreetsIntoGraph(streets, len(maps))
PrintMatrix(graphMatrix, len(maps))

MTemp, cost = GetReducedMatrix(graphMatrix, len(maps))
PrintMatrix(MTemp, len(maps))
print("Reduced cost =", cost)