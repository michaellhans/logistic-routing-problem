# astar.py
# A* Algorithm for Pathfinding (Modified)
# Reference : https://www.annytab.com/a-star-search-algorithm-in-python/

from graph import *
from node import *
import numpy as np

# Calculate heuristic value : distance from every city to destination city
def heuristics(cities, destination):
    h = {}
    for i in range(len(cities)):
        g = cities.get(str(i)).distanceTo(destination)
        h.update({str(i):g})
    return h

# A* search
def astar_search(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    open = []
    closed = []

    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:

        # Sort the open list to get the node with the lowest cost first
        open.sort()

        # Get the node with the lowest cost
        current_node = open.pop(0)

        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append([current_node.name, current_node.g])
                current_node = current_node.parent
            path.append([start_node.name, start_node.g])
            # Return reversed path
            return path[::-1]

        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop neighbors
        for key, value in neighbors.items():

            # Create a neighbor node
            neighbor = Node(key, current_node)

            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue

            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)

    # Return None, no path is found
    return None

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

# Return the route information of the path
def getRoute(path):
    route = []
    for i in range(len(path)):
        route.append(int(path[i][0]))
    return route

# Return the cost infromation of the path
def getCost(path):
    return path[-1][1]

# Generate distance matrix based on distance of the A* path
# Milestone 1 : Get Complete Graph of all depot and station
def generateAStarParameter(destination, maps, graph):
    heuristicList = []
    for i in range(len(destination)):
        h = {}
        h = heuristics(maps, maps.get(destination[i]))
        heuristicList.append(h)

    distance = [[np.inf for j in range(len(destination))] for i in range(len(destination))]
    routes = [['placeholder' for j in range(len(destination))] for i in range(len(destination))]
    for i in range(len(destination)):
        for j in range(len(destination)):
            if (i != j):
                # Run the search algorithm
                path = astar_search(graph, h, destination[i], destination[j])
                route = getRoute(path)
                routes[i][j] = route
                distance[i][j] = getCost(path)

    return distance, routes