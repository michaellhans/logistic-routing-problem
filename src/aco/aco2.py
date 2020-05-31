# aco.py
# Ant-Colony Optimization

import random
from ant import *

class AntColony:
    # Create AntColony class
    def __init__(self, numOfCities):
        self.c = 1.0
        self.alpha = 1.0
        self.beta = 5.0
        self.evaporation = 0.5
        self.Q = 500
        self.antFactor = 0.8
        self.randomFactor = 0.01

        self.maxIterations = 1000

        self.numOfCities = numOfCities
        self.numOfAnts = int(numOfCities * self.antFactor)
        self.G = self.generateRandomMatrix(numOfCities)
        self.trails = [[None for i in range(numOfCities)] for j in range(numOfCities)]
        self.probabilities = [None for i in range(numOfCities)]
        
        self.currentIndex = -1
        self.ants = []
        for i in range(self.numOfAnts):
            self.ants.append(Ant(numOfCities))

        self.bestTourOrder = []
        self.bestTourLength = 99999

    # Generate random graph
    def generateRandomMatrix(self, numOfCities):
        randomMatrix = []
        for i in range(numOfCities):
            randomRow = []
            for j in range(numOfCities):
                randomRow.append(random.randint(0,99)+1)
            randomMatrix.append(randomRow)
        return randomMatrix

    # Perform ant optimization
    def startAntOptimization(self):
        for i in range(3):
            print("Attempt #"+str(i+1))
            self.solve()

    # Use this method to run the main logic
    def solve(self):
        print(self.G)
        self.setupAnts()
        self.clearTrails()
        for i in range(self.maxIterations):
            self.moveAnts()
            self.updateTrails()
            self.updateBest()
        print("Best tour length\t: ", self.bestTourLength - self.numOfCities)
        print("Best tour order\t: ", self.bestTourOrder)
        return self.bestTourOrder

    # Prepare ants for the simulation
    def setupAnts(self):
        for i in range(self.numOfAnts):
            for ant in self.ants:
                ant.clear()
                ant.visitCity(-1, random.randint(0, self.numOfCities-1))
        self.currentIndex = 0

    # At each iteration, move ants
    def moveAnts(self):
        temp = self.currentIndex
        for i in range(temp, self.numOfCities-1):
            for ant in self.ants:
                nextCity = self.selectNextCity(ant)
                if (nextCity != None):
                    ant.visitCity(self.currentIndex, nextCity)
            self.currentIndex += 1

    # Select next city for each ant
    def selectNextCity(self, ant):
        temp = self.numOfCities - self.currentIndex - 1
        if (temp == 0):
            t = 0
        else:
            t = random.randint(0, temp)
        if (random.random() < self.randomFactor):
            cityIndex = -1
            for i in range(self.numOfCities):
                if ((i == t) and (not(ant.isVisited(i)))):
                    cityIndex = i
                    break
            if (cityIndex != -1):
                return cityIndex

        self.calculateProbabilities(ant)
        r = random.random()
        total = 0
        for i in range(self.numOfCities):
            total += self.probabilities[i]
            if (total >= r):
                return i


    # Calculate the next city picks probabilities
    def calculateProbabilities(self, ant):
        i = ant.trail[self.currentIndex]
        pheromone = 0
        for l in range(self.numOfCities):
            if not(ant.isVisited(l)):
                pheromone += (self.trails[i][l] ** self.alpha) * ((1.0 / self.G[i][l]) ** self.beta)
        for j in range(self.numOfCities):
            if (ant.isVisited(j)):
                self.probabilities[j] = 0
            else:
                numerator = (self.trails[i][l] ** self.alpha) * ((1.0 / self.G[i][l]) ** self.beta)
                self.probabilities[j] = numerator / pheromone

    # Update trails that ants used
    def updateTrails(self):
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.trails[i][j] = self.trails[i][j] * self.evaporation
        
        for ant in self.ants:
            contribution = self.Q / ant.trailLength(self.G)
            for i in range(self.numOfCities-1):
                self.trails[ant.trail[i]][ant.trail[i+1]] += contribution
            self.trails[ant.trail[self.numOfCities - 1]][ant.trail[0]] += contribution

    # Update the best solution
    def updateBest(self):
        if (self.bestTourOrder == None):
            self.bestTourOrder = ants.get(0).trail
            self.bestTourLength = ants.get(0).trailLength(self.G)
        for ant in self.ants:
            if (ant.trailLength(self.G) < self.bestTourLength):
                self.bestTourLength = ant.trailLength(self.G)
                self.bestTourOrder = ant.trail

    # Clear trails after simulation
    def clearTrails(self):
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.trails[i][j] = self.c

# Driver for ACO
antTSP = AntColony(5)
antTSP.solve()