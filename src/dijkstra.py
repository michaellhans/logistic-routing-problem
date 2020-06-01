# Dijkstra.py
# Dijkstra Algorithm for Pathfinding
# Reference : Rinaldi Munir

import numpy as np

# Get the nearest vertex with minimum distance
def minDistance(dist, S, n):
    # Initialize minimum distance for next node 
    min = np.inf
    # Choose v from among those vertices not in S such that dist[u] is minimum

    min_index = 0
    for v in range(n): 
        if ((dist[v] < min) and (S[v] == False)): 
            min = dist[v] 
            min_index = v 

    return min_index 

# Dijkstra Algorithm to return all shortest path fro a to n-1 cities
def dijkstra(G, a, n):
    # Initialize S and Distance
    S = []
    dist = []
    parent = []

    for i in range(n):
        S.append(False)
        dist.append(np.inf)
        parent.append(-1)

    S[a] = True
    dist[a] = 0

    # Search for minimum distance from a to every node
    for num in range(2,n):
        # Determine n-1 paths from v
        # Choose u from among those vertices not in S such that dist[u] is minimum
        u = minDistance(dist, S, n)

        S[u] = True  # Put u in S
        for w in range(n):
            if ((S[w] == False) and (dist[w] > dist[u] + G[u][w])):
                dist[w] = dist[u] + G[u][w]
                parent[w] = u

    return dist, parent

# Print the path for all solution for dijkstra
def getPath(parent, v):
    path = []
    if (parent[v] == -1):
        path = [v]
    else:
        path = getPath(parent, parent[v]) + [v]
    return path

# Print all solution for dijkstra
def printSolution(solution, parent): 
    print("Vertex \tDistance \t\tPath")
    for node in range(len(solution)): 
        print(node, "\t", solution[node], "\t\t", getPath(parent, node)) 