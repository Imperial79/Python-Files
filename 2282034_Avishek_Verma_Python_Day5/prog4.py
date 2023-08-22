'''
4. Create a class to represent a point in two-dimensional geometric coordinates. Initialize the
position of a new point. In the initializer, the x and y coordinates can be specified. If they
are not, the point defaults to the origin. Write methods to i) move the point to a new
location in 2D space, ii) reset a point back to the geometric origin (0, 0), iii) calculate the
Euclidean distance from a point to a second point passed as an argument. Instantiate
objects of the point class and test the methods on the created objects.
'''

import math


class Geo:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveToNew(self):
        self.x2 = int(input("enter new x coordinate: "))
        self.y2 = int(input("enter new y coordinate: "))

    def reset(self):
        self.x = 0
        self.y = 0

    def euclidean(self):
        a = (self.x2 - self.x) ** 2 + (self.y2 - self.y)**2
        return math.sqrt(a)


g = Geo(2, 3)
print("Initial coordinates -> (2,3)")
g.moveToNew()
print("The Eulidean distance ", g.euclidean())
g.reset()
