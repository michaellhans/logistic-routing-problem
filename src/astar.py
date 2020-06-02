# astar.py
# A* Algorithm for Pathfinding (Modified)
# Reference : https://www.annytab.com/a-star-search-algorithm-in-python/

from graph import *
from node import *
from loader import *
from visualizer import *
from ant_colony import *
from mtsp import *

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

# Convert from path detail into path route for visualization
def detailToSimple(path):
    route = []
    for i in range(len(path)):
        route.append(int(path[i][0]))
    return route

# Return the cost of the path
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
                print(path)
                route = detailToSimple(path)
                routes[i][j] = route
                distance[i][j] = getCost(path)

    return distance, routes

# Convert from simple route from A* Matrix into the real route from the maps
def simple_into_real_route(trail, routes):
    realPath = []
    originCity = trail[0]
    realOriginCity = routes[int(originCity)][1][0]
    for i in range(len(trail)-1):
        realPath = realPath + routes[int(originCity)][int(trail[i+1])]
        realPath.pop()
        originCity = trail[i+1]
    realPath.append(realOriginCity)
    return realPath

# Change correspondent route into True
def apply_route_on_streets(all_real_path, boolStreets):
    for i in range(len(all_real_path)):
        for j in range(len(all_real_path[i])-1):
            label = str(all_real_path[i][j]) + '-' + str(all_real_path[i][j+1])
            value = boolStreets.get(label)
            if (value == None):
                label = str(all_real_path[i][j+1]) + '-' + str(all_real_path[i][j])
            boolStreets[label] = i

# The main entry point for this module
def main():
    # Quick test for quick debugging
    fileNode = "OL.cnode.txt"
    fileEdge = "OL.cedge.txt"
    numOfSalesman = 2

    maps = LoadCoordinate(fileNode)
    streets = LoadStreet(fileEdge)
    boolStreets = GetBooleanStreets(streets)

    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
    graph.streetsToGraph(streets)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    all_real_path = []
    solution = []
    destination = [str(2000 + i * 10 + random.randint(0,70)) for i in range(numOfSalesman * 3)]
    listOfSubDestination = splitCities(destination, numOfSalesman, destination[0], maps)
    destinationInt = [int(destination[i]) for i in range(numOfSalesman * 3)]
    
    print(destination)

    input()
    for i in range(numOfSalesman):
        MCost = []
        MRoute = []
        MCost, MRoute = generateAStarParameter(listOfSubDestination[i], maps, graph)
        PrintMatrix(MCost, len(listOfSubDestination[i]))
        print(listOfSubDestination[i])
        print(MRoute)
        input()

        # Execute numOfSalesman TSP process and return numOfSalesman route
        ant_colony = AntColony(np.array(MCost), 10, 5, 100, 0.95, alpha=1, beta=1)
        shortest_path = ant_colony.run()
        print ("Shortest path: {}".format(shortest_path))
        if (shortest_path[0] != 'placeholder'):
            routeParent = ConvertIntoRoute(shortest_path)
            # ValidizeRoute(routeParent, destination)
            print("Jarak tempuh untuk sales ke-"+str(i+1)+" adalah "+str(shortest_path[1])+" km")
            print("Rute perjalanan untuk sales ke-"+str(i+1)+" adalah ", end="")
            PrintRoute(routeParent)
            real_path = simple_into_real_route(routeParent, MRoute)
            print("Rute asli perjalanan untuk sales ke-"+str(i+1)+" adalah ", end="")
            PrintRoute(real_path)
            all_real_path.append(real_path)
            solution.append([real_path, shortest_path[1]])
        else:
            print("Tidak terdapat rute yang memungkinkan untuk sales ke-"+str(i+1))
            solution.append([[0], -999])
        input()

    apply_route_on_streets(all_real_path, boolStreets)
    PrintAllSolution(solution, numOfSalesman)
    input("Next.. to visualizer")

    # Visualize the route for every salesman
    VisualizeComplexGraph(destinationInt[0], streets, boolStreets, all_real_path, maps, len(maps), destinationInt)

# Tell python to run main method
if __name__ == "__main__": main()

