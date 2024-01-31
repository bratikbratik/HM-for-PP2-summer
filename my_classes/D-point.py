import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def dist(self, other: 'Point'):
        self.answ = (math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))
        print(self.answ)

p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()
p2.show()
print(p1.dist(p2))
