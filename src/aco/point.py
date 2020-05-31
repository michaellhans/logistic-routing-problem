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
        return "(" + str(self.x) + ", " + str(self.y) + ")"

# Driver for Point
# P1 = Point(2,4)
# P2 = Point(4,8)
# P3 = Point(6,4)
# P4 = Point(2,-2)
# P5 = Point(0,0)
# P6 = Point(6,0)
# P7 = Point(12,8)
# P8 = Point(10,6)
# P9 = Point(10,2)
# P10 = Point(8,2)
# P11 = Point(9,-1)
# print(P6.distanceTo(P10))
# print(P3.distanceTo(P10))
# print(P9.distanceTo(P11))
# print(P10.distanceTo(P11))
# print(P10.distanceTo(P9))
# print(P10.distanceTo(P8))
# print(P8.distanceTo(P9))
# print(P8.distanceTo(P2))
# print(P8.distanceTo(P7))
# print(P7.distanceTo(P9))
# print(P2.distanceTo(P7))