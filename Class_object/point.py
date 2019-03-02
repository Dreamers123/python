import math

class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def make_them_same(self,other_point):
        self.x=other_point.x
        self.y=other_point.y
    def reset(self):
        self.move(0, 0)
    def calculate_distance(self, other_point):
        return math.sqrt(
                        (self.x - other_point.x)**2 +
                        (self.y - other_point.y)**2)


# how to use it:
point1 = Point()
point2 = Point()
point1.move(4,5)
point2.move(4,6)
print(point1.calculate_distance(point2))
point2.reset()
print(point1.calculate_distance(point2))
point1.make_them_same(point2)
print(point1.calculate_distance(point2))
print(point2.calculate_distance(point1))
point2.move(5,5)
print(point1.calculate_distance(point2))
point1.make_them_same(point2)
print(point1.y)
