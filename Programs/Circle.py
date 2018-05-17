

import math

class circle:
    def __init__(self,radius=1):
        self.radius=radius
    def getParameter(self):
        return 2*self.radius*math.pi
    def getArea(self):
        return self.radius*self.radius*math.pi
   

