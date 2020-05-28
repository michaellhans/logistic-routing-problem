# Point.py
# Contain of all module to generate execute the point

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self, P):
        return ((self.getX() - P.getX())**2 + (self.getY() - P.getY())**2)**0.5

    def printInfo(self):
        return "(" + self.x + ", " + self.y + ")"

# Driver for Point
# P1 = Point(0,3)
# P2 = Point(4,0)
# print(P1.distanceTo(P2))