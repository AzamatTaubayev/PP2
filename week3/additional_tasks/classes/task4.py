import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, p):
        dx = p.x - self.x
        dy = p.y - self.y
        return dx, dy

x1 = int(input())
y1 = int(input())
pt = Point(x1, y1)
print(pt.show())