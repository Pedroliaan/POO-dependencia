import math


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2