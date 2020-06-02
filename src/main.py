# main.py
# Main Program for Command-Based Application
# Logistic Routing Problem

from astar import *
from route import *
from loader import *
from visualizer import *

# Main Program or Driver for Multiple TSP with Ant-Colony Optimization
print("Sthyrelest Enterprise - Logistic Routing Problem (SE-LRP)")
print("Multiple Traveling Salesperson Problem")
print("Created by: 13518056 - Michael Hans", end='\n\n')

print("Algorithm provided in this application")
print("1. Pathfinding\t: A* Algorithm")
print("2. TSP Problem\t: Ant-Colony Optimization", end='\n\n')

print("Selamat datang di aplikasi SE-LRP!", end='\n\n')

# ==============================================================================================
# Section 1 : Input and loading node and edge data
# ==============================================================================================
print("Section 1 : Input and loading node and edge data", end='\n\n')
maps = {}
isSuccess = False
while (not(isSuccess)):
    try:
        fileNode = input("Masukkan nama file koordinat\t: ")
        fileEdge = input("Masukkan nama file jalanan\t: ")
        maps = LoadCoordinate(fileNode)
        streets = LoadStreet(fileEdge)
        boolStreets = GetBooleanStreets(streets)
        numOfCities = len(maps)
        isSuccess = True
    except IndexError:
        print("Terjadi kesalahan dalam pembacaan file!")
        print("Harap masukkan file yang valid dengan format yang benar.")
    except FileNotFoundError:
        print("File tidak ditemukan!")
    except PermissionError:
        print("Harap memasukkan nama file data!")

numOfSalesman = int(input("Masukkan jumlah salesman\t: "))
while (numOfSalesman >= numOfCities):
    print("Jumlah salesman tidak boleh melebihi banyaknya kota.",end=" ")
    print("Banyaknya kota adalah",numOfCities, end="\n\n")
    numOfSalesman = int(input("Masukkan jumlah salesman\t: "))

print("Metode penentuan depot logistik:")
print("1. Masukkan pengguna dari file")
print("2. Random depot factor")
choice = int(input("Pilih metode penentuan depot yang diinginkan: "))
if (choice == 1):
    # User-defined station with one origin depot on index 0
    print("Masukkan ID depot minimal "+str(numOfSalesman*3)+"dan dipisahkan spasi:")
    depotUser = input()
    destination = depotUser.split(' ')
else:
    # Generate random station depends on depotFactor with one origin depot on index 0
    print("Masukkan angka sembarang dibawah "+str(numOfCities - 500)+": ",end="")
    depotFactor = int(input())
    destination = [str(depotFactor + i * 20 + random.randint(0,70)) for i in range(numOfSalesman * 3)]
print()

# ==============================================================================================
# Section 2 : Create Main Graph, Divide into M Tour (Milestone 1)
# ==============================================================================================
print("Section 2 : Create Main Graph, Divide into M Tour (Milestone 1)", end='\n\n')

# Create a graph
graph = Graph()

# Create graph connections (Actual distance)
graph.streetsToGraph(streets)

# Make graph undirected, create symmetric connections
graph.make_undirected()

# Generate list of destination for each salesman
PrintDestination(destination, 0)
listOfSubDestination = splitCities(destination, numOfSalesman, destination[0], maps)

# Convert from string into Int for visualization purposes
destinationInt = [int(destination[i]) for i in range(numOfSalesman * 3)]
input("Click ENTER to proceed for multiple TSP solving!")

# Prepare solution and all path variable to contain all solution in mTSP process
all_real_path = []
solution = []
print()

# ================================================================================================
# Section 3 : Pathfinding, Create Distance Matrix based on Pathfinding, and multiple TSP solving
# ================================================================================================
print("Section 3 : Pathfinding, Create Distance Matrix based on Pathfinding, and multiple TSP solving", end='\n\n')

for i in range(numOfSalesman):
    # Preparation of Cost Matrix and Route Matrix variable for each salesman destination
    MCost = []
    MRoute = []
    print(str(i+1)+". Tur salesman ke-"+str(i+1)+": ")
    print("Loading for generate pathfinding matrix ...")
    MCost, MRoute = generateAStarParameter(listOfSubDestination[i], maps, graph)
    PrintDestination(listOfSubDestination[i], i)
    PrintMatrix(MCost, len(listOfSubDestination[i]))
    input("Click ENTER to proceed for TSP solver!")
    print()

    # Execute TSP process for salesman i+1
    ant_colony = AntColony(np.array(MCost), 10, 5, 100, 0.95, alpha=1, beta=1)
    shortest_path = ant_colony.run()
    print ("Shortest path: {}".format(shortest_path))

    # If we found the shortest path
    if (shortest_path[0] != 'placeholder'):
        raw_path = ConvertIntoRoute(shortest_path)
        real_path = raw_into_real_route(raw_path, MRoute)
        simple_path = raw_into_simple_route(raw_path, listOfSubDestination[i])

        # Print route information: cost, raw path, simple path, real path
        print("Jarak tempuh untuk sales ke-"+str(i+1)+" adalah "+str(shortest_path[1])+" km")
        print("Rute perjalanan dari matriks untuk sales ke-"+str(i+1)+" adalah ", end="")
        PrintRoute(raw_path)
        print("Rute sederhana perjalanan untuk sales ke-"+str(i+1)+" adalah ", end="")
        PrintRoute(simple_path)
        print("Rute asli perjalanan untuk sales ke-"+str(i+1)+" adalah ", end="")
        PrintRoute(real_path)

        # Add simple path, real path, and cost information to the solution
        all_real_path.append(real_path)
        solution.append([simple_path, real_path, shortest_path[1]])

    # If we didn't find shortest path
    else:
        print("Tidak terdapat rute yang memungkinkan untuk sales ke-"+str(i+1))
        solution.append([[0], -999])

    print()
    input("Click ENTER to proceed for next salesman tour!")
    print()

# ================================================================================================
# Section 4 : Reconstruct all solution and visualize both map and route
# ================================================================================================
print("Section 4 : Reconstruct all solution and visualize both map and route", end='\n\n')

# Apply route on streets to make different color of each salesman path
apply_route_on_streets(all_real_path, boolStreets)

# Printing all solution (Milestone 2)
PrintAllSolution(solution, numOfSalesman)
input("Click ENTER to proceed to visualizer")
print()

# Visualize the route for every salesman (Milestone 3)
print("Please wait ...")
VisualizeComplexGraph(destinationInt[0], streets, boolStreets, all_real_path, maps, len(maps), destinationInt)