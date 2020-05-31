# aco.py
# Ant-Colony Optimization

from graph import *

# Create Ants
# Visit the city and add it to the trail
def visitCity(currentIndex, city):
    trail[currentIndex+1] = city
    visited[city] = True

# Check if the city i is already visited
def isVisited(int i):
    return visited[city]

# Compute total distance of the trail
def trailLength(graph):
    length = graph[trail[len(trail)-1]][trail[0]]
    for i in range(len(trail)-1):
        length = length + graph[trail[i]][trail[i+1]]
    return length
    
# ACO Parameter
c = 1.0
alpha = 1
beta = 5
evaporation = 0.5
Q = 500
antFactor = 0.8
randomFactor = 0.01

# Driver for TSP with ACO
maps = {}
fileNode = "MTSPNode2.txt"
fileEdge = "MTSPEdge2.txt"
baseCity = 0
maps = LoadCoordinate(fileNode)

# Setup Ants
graph = LoadStreet(fileEdge)
PrintCoordinateInfo(maps)
PrintStreetInfo(graph)
numOfCities = len(maps)
numOfAnts = int(numOfCities * antFactor)





# class ACO:
#     # Create new ACO (Ant-Colony Optimization) class
#     def __init__(self, c = 1.0, alpha = 1, beta = 5, evaporation = 0.5, Q = 500, antFactor = 0.8, randomFactor = 0.01):
#         self.c = c
#         self.alpha = alpha
#         self.beta = beta
#         self.evaporation = evaporation
#         self.Q = Q
#         self.antFactor = antFactor
#         self.randomFactor = randomFactor
    
    