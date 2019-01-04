import math

class MathOperation:
    def __init__(self, radius, names):
        self.radius = radius
        self.names = names

    def area(self):
        return self.circleArea(self.radius)

    @staticmethod
    def circleArea(r):
        return r ** 2 * math.pi

p = MathOperation(8, ['piechart', 'barchart'])
print(p.area())
print(p.circleArea(6))