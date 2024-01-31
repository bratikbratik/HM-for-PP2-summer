class Shape:
    def area(self):
        print(0)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(self.width * self.length)

shape = Shape()
shape.area()

rec = Rectangle(2, 5)
rec.area()