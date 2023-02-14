import linecache


class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

l1 = int(input())
theSquare = Square(l1)
print(theSquare.area())