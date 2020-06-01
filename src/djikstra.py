# djikstra.py
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
    for i in range(n):
        S.append(False)
        dist.append(np.inf)
    
    S[a] = True
    dist[a] = 0

    # Search for minimum distance from a to every node
    for num in range(n):
        # Determine n-1 paths from v
        # Choose u from among those vertices not in S such that dist[u] is minimum
        u = minDistance(dist, S, n)

        S[u] = True  # Put u in S
        for w in range(n):
            if ((S[w] == False) and (dist[w] > dist[u] + G[u][w])):
                dist[w] = dist[u] + G[u][w]

    return dist

# Print all solution for dijkstra
def printSolution(solution): 
    print("Vertex \tDistance from Source")
    for node in range(len(solution)): 
        print(node, "\t", solution[node]) 

Graph = [[np.inf, 4, np.inf, np.inf, np.inf, np.inf, np.inf, 8, np.inf], 
        [4, np.inf, 8, np.inf, np.inf, np.inf, np.inf, 11, np.inf], 
        [np.inf, 8, np.inf, 7, np.inf, 4, np.inf, np.inf, 2], 
        [np.inf, np.inf, 7, np.inf, 9, 14, np.inf, np.inf, np.inf], 
        [np.inf, np.inf, np.inf, 9, np.inf, 10, np.inf, np.inf, np.inf], 
        [np.inf, np.inf, 4, 14, 10, np.inf, 2, np.inf, np.inf], 
        [np.inf, np.inf, np.inf, np.inf, np.inf, 2, np.inf, 1, 6], 
        [8, 11, np.inf, np.inf, np.inf, np.inf, 1, np.inf, 7], 
        [np.inf, np.inf, 2, np.inf, np.inf, np.inf, 6, 7, np.inf] 
        ]; 

Origin = 0
Solution = dijkstra(Graph, 0, 9)
printSolution(Solution)