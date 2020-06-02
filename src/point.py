# Point.py
# Contain class of point to create a point object

class Point:
    # Constructor to create new point(x,y) object
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Get the x-value of the point
    def getX(self):
        return self.x

    # Get the y-value of the point
    def getY(self):
        return self.y

     # Get the distance value between the point and P point
    def distanceTo(self, P):
        return ((self.getX() - P.getX())**2 + (self.getY() - P.getY())**2)**0.5

    # Print the information of the point
    def printInfo(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # Comparison for object of point
    def __lt__(self, other):
        if (self.x == other.x):
            return self.y < other.y
        else:
            return self.x < other.x