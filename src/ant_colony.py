# ant_colony.py
# Contain AntColony class to find the shortest path for TSP
# Modified ant_colony.py for incomplete graph and multiple TSP
# Reference for original source code : https://github.com/Akavall/AntColonyOptimization

import random as rn
import numpy as np
from numpy.random import choice as np_choice

class AntColony(object):
    # Constructor to create an AntColony object
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            n_ants (int): Number of ants running per iteration
            n_best (int): Number of best ants who deposit pheromone
            n_iteration (int): Number of iterations
            decay (float): Rate it which pheromone decays. The pheromone value is multiplied by decay, so 0.95 will lead to decay, 0.5 to much faster decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight. Default=1
            beta (int or float): exponent on distance, higher beta give distance more weight. Default=1

        Example:
            ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    # Execute ant-colony optimization algorithm to get shortest TSP route
    def run(self):
        # Initialize shortest path parameter
        shortest_path = None
        found = False
        all_time_shortest_path = ("placeholder", np.inf)
        most_cities = ("placeholder", np.inf)

        # Finding the shortest path by n_iteration
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)

            # Choose the shortest path and most city visited
            for path in all_paths:
                if (path[1] != np.inf):
                    if (shortest_path == None):
                        shortest_path = path
                    if (len(path[0]) == len(shortest_path[0])):
                        if (path[1] < shortest_path[1]):
                            shortest_path = path
                    elif (len(path[0]) > len(shortest_path[0])):
                        shortest_path = path

            # The shortest path will be considered if it is None
            if (shortest_path != None):
                if (shortest_path[0] != None):
                    # print (shortest_path)
                    
                    # The path is return to the origin city
                    if (shortest_path[0][-1][1] == 0):
                        found = True
                        if ((shortest_path[1] < all_time_shortest_path[1]) and (shortest_path[1] != np.inf)):
                            all_time_shortest_path = shortest_path

                    # Sometime, the path is not return to the origin city
                    else:
                        if ((shortest_path[1] < all_time_shortest_path[1]) and (shortest_path[1] != np.inf)):
                            most_cities = shortest_path       

            # Evaporation and decay every iteration   
            self.pheromone * self.decay

        # From n_iteration, we found the shortest path, then return the shortest path
        if (found):            
            return all_time_shortest_path

        # From n_iteration, we didn't found the shortest path, then we return the path with the most city visited
        else:
            return most_cities

    # Spread the pheromone on the n_best paths based on all paths and latest shortest path
    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    # Return distance of the path based on the distance matrix
    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    # Generate all random path for each ant
    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    # Generate a random path for an ant based on the probability
    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            if (move == -1):
                break
            path.append((prev, move))
            prev = move
            visited.add(move)
        if (move != -1):
            path.append((prev, start)) # going back to where we started    
        return path

    # Select the next city to visit
    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0
        
        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)
        
        if (row.sum() == 0):
            return -1
        else:
            norm_row = row / row.sum()
            move = np_choice(self.all_inds, 1, p=norm_row)[0]
            return move