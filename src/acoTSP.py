# aco.py
# Calculate mTSP route with ant colony optimization

from graph import *
from complexVisualizer import *
from visualizer import *
from ant_colony import *

# Convert from List of Path into Route
def ConvertIntoRoute(listOfPath):
    route = []
    startcity = listOfPath[0][0][0]
    route.append(startcity)
    for path in listOfPath[0]:
        route.append(path[1])
    return route

# Driver for TSP with ACO
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

MBase = ConvertStreetsIntoGraph(streets, length)
ant_colony = AntColony(np.array(MBase), 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("Shortest path: {}".format(shortest_path))
routeParent = ConvertIntoRoute(shortest_path)
VisualizeGraph(streets, routeParent, length, fileNode)
VisualizeComplexGraph(shortest_path[0][0][0], streets, routeParent, maps, length)