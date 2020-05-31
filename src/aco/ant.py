# ant.py
# Class for ant

class Ant:
    def __init__(self, tourSize):
        self.trailSize = tourSize
        self.trail = [None for i in range(tourSize)]
        self.visited = [False for i in range(tourSize)]

    def visitCity(self, currentIndex, city):
        self.trail[currentIndex + 1] = city
        self.visited[city] = True

    def isVisited(self, i):
        return self.visited[i]

    def trailLength(self, G):
        totalDistance = G[self.trail[self.trailSize - 1]][self.trail[0]]
        for i in range(self.trailSize-1):
            totalDistance = totalDistance + G[self.trail[i]][self.trail[i+1]]
        return totalDistance
    
    def clear(self):
        for i in range(self.trailSize):
            self.visited[i] = False