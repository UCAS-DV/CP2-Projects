import math

class circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    def circumference(self):
        return math.pi * self.radius * 2
    
    def compare_area(self):