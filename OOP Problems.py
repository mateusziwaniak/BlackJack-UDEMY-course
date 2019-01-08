"""
class Cylinder:



    def __init__(self, height = 1, radius = 1):
        self.pi = 3.14
        self.height = height
        self.radius = radius


    def volume(self,):
        result = self.pi * self.radius * self.radius * self.height
        return result


    def surface_area(self):
        result = (self.pi * self.radius * self.radius) * 2 + (self.height * 2 * self.pi * self.radius)
        return result

walec = Cylinder(2,3)

print(round(walec.volume()),2)
print(round(walec.surface_area()),2)
"""

import math

class Line:

    def __init__(self, coor1, coor2):
        self.pi = 3.14
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2


    def distance(self):
        result = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        return result

    def slope(self):
        top = self.y2 - self.y1
        bottom = self.x2 - self.x1
        result = top / bottom
        return result


coordinate1 = (3, 2)
coordinate2 = (8, 10)


walec = Line(coordinate1, coordinate2)
print(walec.distance())
print(walec.slope())


