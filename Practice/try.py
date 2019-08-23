import math

#Fill in the Line class methods to accept coordinates as a pair of tuples 
# and return the slope and distance of the line.

class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        dist = (((x2-x1) ** 2) - ((y2 -y1) **2)) ** 0.5
        print(dist)
        return dist

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        sl = (x2-x1 / y2-y1)
        print(sl)
        return sl





cob = (9,2)
nob = (4,4)

line = Line(cob,nob)
line.distance()
line.slope()


#CYlinder
#vol = (pi * (self.radius ** 2) * self.height)
#sa = (2 * pi * self.radius * self.height) + (2 * pi * (self.radius ** 2))
# from math import pi
class cylinder:
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius

    def volume(self):
        pi = 3.142
        vol = (pi * (self.radius ** 2) * self.height)
        print(vol)
        return vol

    def surface_area(self):
        pi = 3.142
        sa = (2 * pi * self.radius * self.height) + (2 * pi * (self.radius ** 2))
        print(sa)
        return sa


box = cylinder(1,1)
box.volume()
box.surface_area


