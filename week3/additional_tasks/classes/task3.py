class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
a1 = int(input())
b1 = int(input())
rec = Rectangle(a1, b1)
print(rec.area())