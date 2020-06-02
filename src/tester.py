# tester.py
# Driver to test every module in src folder

from astar import *
from route import *
from loader import *
from visualizer import *
from point import *

# Point Test
def PointTest():
    P1 = Point(2,4)
    P2 = Point(4,8)
    P3 = Point(6,4)
    P4 = Point(2,-2)
    P5 = Point(0,0)
    P6 = Point(6,0)
    P7 = Point(12,8)
    P8 = Point(10,6)
    P9 = Point(10,2)
    P10 = Point(8,2)
    P11 = Point(9,-1)
    print(P6.distanceTo(P10))
    print(P3.distanceTo(P10))
    print(P9.distanceTo(P11))
    print(P10.distanceTo(P11))
    print(P10.distanceTo(P9))
    print(P10.distanceTo(P8))
    print(P8.distanceTo(P9))
    print(P8.distanceTo(P2))
    print(P8.distanceTo(P7))
    print(P7.distanceTo(P9))
    print(P2.distanceTo(P7))

# Loader Test
def LoaderTest():
    maps = {}
    boolStreet = {}
    maps = LoadCoordinate("SthyrelestNode.txt")
    PrintCoordinateInfo(maps)
    streets = LoadStreet("SthyrelestEdge.txt")
    PrintStreetInfo(streets)
    graphMatrix = ConvertStreetsIntoGraph(streets, len(maps))
    PrintMatrix(graphMatrix, len(maps))
    boolStreets = GetBooleanStreets(streets)
    TestRoutedStreet(boolStreets)

# Ant-Colony Testing
def AntColonyTest():
    distances = np.array([[np.inf, 4.472, np.inf, np.inf, np.inf],
    [4.472, np.inf, 8.0  , 6.324, np.inf],
    [np.inf, 8.0  , np.inf, 2.828, 6.324],
    [np.inf, 6.324, 2.828, np.inf, 4.0],
    [np.inf, np.inf, 6.324, 4.0  , np.inf]])

    ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
    shortest_path = ant_colony.run()
    print ("shorted_path: {}".format(shortest_path))

# A* Algorithm Testing
def AStarTest():
    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
    graph.connect('Frankfurt', 'Wurzburg', 111)
    graph.connect('Frankfurt', 'Mannheim', 85)
    graph.connect('Wurzburg', 'Nurnberg', 104)
    graph.connect('Wurzburg', 'Stuttgart', 140)
    graph.connect('Wurzburg', 'Ulm', 183)
    graph.connect('Mannheim', 'Nurnberg', 230)
    graph.connect('Mannheim', 'Karlsruhe', 67)
    graph.connect('Karlsruhe', 'Basel', 191)
    graph.connect('Karlsruhe', 'Stuttgart', 64)
    graph.connect('Nurnberg', 'Ulm', 171)
    graph.connect('Nurnberg', 'Munchen', 170)
    graph.connect('Nurnberg', 'Passau', 220)
    graph.connect('Stuttgart', 'Ulm', 107)
    graph.connect('Basel', 'Bern', 91)
    graph.connect('Basel', 'Zurich', 85)
    graph.connect('Bern', 'Zurich', 120)
    graph.connect('Zurich', 'Memmingen', 184)
    graph.connect('Memmingen', 'Ulm', 55)
    graph.connect('Memmingen', 'Munchen', 115)
    graph.connect('Munchen', 'Ulm', 123)
    graph.connect('Munchen', 'Passau', 189)
    graph.connect('Munchen', 'Rosenheim', 59)
    graph.connect('Rosenheim', 'Salzburg', 81)
    graph.connect('Passau', 'Linz', 102)
    graph.connect('Salzburg', 'Linz', 126)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['Basel'] = 204
    heuristics['Bern'] = 247
    heuristics['Frankfurt'] = 215
    heuristics['Karlsruhe'] = 137
    heuristics['Linz'] = 318
    heuristics['Mannheim'] = 164
    heuristics['Munchen'] = 120
    heuristics['Memmingen'] = 47
    heuristics['Nurnberg'] = 132
    heuristics['Passau'] = 257
    heuristics['Rosenheim'] = 168
    heuristics['Stuttgart'] = 75
    heuristics['Salzburg'] = 236
    heuristics['Wurzburg'] = 153
    heuristics['Zurich'] = 157
    heuristics['Ulm'] = 0

    # Run the search algorithm
    pathDetail = astar_search(graph, heuristics, 'Frankfurt', 'Ulm')
    print(pathDetail)