import numpy as np

from ant_colony import AntColony

distances = np.array([[np.inf, 4.472, np.inf, np.inf, np.inf],
[4.472, np.inf, 8.0  , 6.324, np.inf],
[np.inf, 8.0  , np.inf, 2.828, 6.324],
[np.inf, 6.324, 2.828, np.inf, 4.0],
[np.inf, np.inf, 6.324, 4.0  , np.inf]])

ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("shorted_path: {}".format(shortest_path))