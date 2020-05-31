import numpy as np

from ant_colony import AntColony

distances = np.array([[np.inf, 4.472, 4.0, 6.0, 4.472, np.inf, np.inf, np.inf, np.inf, 6.325, np.inf],
                    [4.472, np.inf, 4.472, np.inf, np.inf, np.inf, 8.0, 6.324, np.inf, np.inf, np.inf],
                    [4.0, 4.472, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 2.828, np.inf],
                    [6.0, np.inf, np.inf, np.inf, 2.824, 4.472, np.inf, np.inf, np.inf, np.inf, np.inf],
                    [4.472, np.inf, np.inf, 2.824, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                    [np.inf, np.inf, np.inf, 4.472, np.inf, np.inf, np.inf, np.inf, np.inf, 2.828, np.inf],
                    [np.inf, 8.0, np.inf, np.inf, np.inf, np.inf, np.inf, 2.828, 6.324, np.inf, np.inf],
                    [np.inf, 6.324, np.inf, np.inf, np.inf, np.inf, 2.828, np.inf, 4.0, 4.472, np.inf],
                    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 6.324, 4.0, np.inf, 2.0, 3.162],
                    [6.325, np.inf, 2.828, np.inf, np.inf, 2.828, np.inf, 4.472, 2.0, np.inf, 3.162],
                    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 3.162, 3.162, np.inf]])

ant_colony = AntColony(distances, 10, 5, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("shorted_path: {}".format(shortest_path))