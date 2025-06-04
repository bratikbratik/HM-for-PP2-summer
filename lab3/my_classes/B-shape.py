class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


shape = Shape()
shape.area()

square = Square(4)
square.area()
